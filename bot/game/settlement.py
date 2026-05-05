"""
Game settlement — Phase 3: process game end, update memory, prepare for next game.

Structured analysis pipeline:
  1. Extract death cause (DZ / guardian / agent / monster)
  2. Record combat metrics (damage dealt/taken, fights won/lost, items used)
  3. Track resource efficiency (healing efficiency, sMoltz per kill)
  4. Update opponent profiles from brain's _known_agents
  5. Generate adaptive StrategyRules from lesson patterns
  6. Migrate legacy string lessons to structured CombatLesson format
"""

from bot.memory.agent_memory import (
    AgentMemory,
    CombatLesson,
    StrategyRule,
    OpponentProfile,
)
from bot.utils.logger import get_logger

log = get_logger(__name__)


def _extract_death_cause(result: dict, last_view: dict | None = None) -> str:
    """Determine what killed the agent: death_zone, agent_kill, guardian_kill,
    monster_kill, or ranked_out (survived to end but didn't win).

    Priority order: last_view currentRegion DZ → result details → inference from context.
    """
    # 1. Check if agent died in a death zone (from last_view)
    if last_view:
        region = last_view.get("currentRegion", {})
        if isinstance(region, dict) and region.get("isDeathZone"):
            return "death_zone"

    # 2. Check result-level death cause if provided by the API
    death_info = result.get("deathCause") or result.get("death") or {}
    if isinstance(death_info, dict):
        cause_type = death_info.get("type", "")
        if cause_type == "death_zone":
            return "death_zone"
        if cause_type == "guardian":
            return "guardian_kill"
        if cause_type == "monster":
            return "monster_kill"
        if cause_type == "agent":
            return "agent_kill"

    # 3. Infer from result context
    is_winner = result.get("isWinner", False)
    kills = result.get("kills", 0)
    rank = result.get("finalRank", 0)

    if is_winner:
        return "none"  # survived and won — no death
    if rank == 0 or kills > 0:
        # Had kills but lost — likely killed by agent or zone
        return "agent_kill"
    if kills == 0 and rank > 1:
        # No kills, didn't win — likely died early to environment
        return "unknown"

    return "ranked_out"


def _extract_death_details(
    result: dict,
    death_cause: str,
    last_view: dict | None = None,
    stats: dict | None = None,
) -> dict:
    """Build a details dict with contextual information about the death."""
    details: dict[str, object] = {
        "death_cause": death_cause,
    }

    # HP at time of death (from last_view if available)
    if last_view:
        self_data = last_view.get("self", {})
        if isinstance(self_data, dict):
            details["hp_at_death"] = self_data.get("hp", "unknown")
            details["ep_at_death"] = self_data.get("ep", "unknown")
            details["weapon_equipped"] = (
                self_data.get("equippedWeapon", {}).get("typeId", "fist")
                if isinstance(self_data.get("equippedWeapon"), dict)
                else "fist"
            )
            details["region_at_death"] = (
                last_view.get("currentRegion", {}).get("name", "unknown")
                if isinstance(last_view.get("currentRegion"), dict)
                else "unknown"
            )

    # Killer identity if available (prefer tracked stats, then result)
    if stats and stats.get("killer_name"):
        details["killer_id"] = stats.get("killer_name") or str(
            stats.get("killer_id", "")
        )
    else:
        death_info = result.get("deathCause") or result.get("death") or {}
        if isinstance(death_info, dict):
            killer = (
                death_info.get("killerId")
                or death_info.get("killedBy")
                or death_info.get("attackerName")
            )
            if killer:
                details["killer_id"] = str(killer)
            killer_hp = death_info.get("killerHp") or death_info.get("attackerHp")
            if killer_hp is not None:
                details["killer_hp_remaining"] = int(killer_hp)

    return details


def _build_combat_metrics(
    result: dict, last_view: dict | None = None, stats: dict | None = None
) -> dict[str, float]:
    """Extract numeric combat metrics from the game result + tracked stats."""
    # Use tracked stats (preferred) or fall back to result fields
    kills = (stats or {}).get("kills", result.get("kills", 0))
    rank = result.get("finalRank", 0)
    is_winner = result.get("isWinner", False)
    rewards = result.get("rewards", {})
    smoltz_earned = rewards.get("sMoltz", 0)

    metrics: dict[str, float] = {
        "kills": float(kills),
        "final_rank": float(rank),
        "smoltz_earned": float(smoltz_earned),
        "is_winner": 1.0 if is_winner else 0.0,
    }

    # Damage metrics: tracked stats first, then result fields
    if stats:
        metrics["damage_dealt"] = float(stats.get("damage_dealt", 0))
        metrics["damage_taken"] = float(stats.get("damage_taken", 0))
        metrics["fights_won"] = float(stats.get("fights_won", 0))
        metrics["fights_lost"] = float(stats.get("fights_lost", 0 if kills > 0 else 1))
    else:
        combat_stats = result.get("combatStats") or result.get("damage") or {}
        if isinstance(combat_stats, dict):
            metrics["damage_dealt"] = float(
                combat_stats.get("damageDealt", combat_stats.get("dealt", 0))
            )
            metrics["damage_taken"] = float(
                combat_stats.get("damageTaken", combat_stats.get("taken", 0))
            )
            metrics["fights_won"] = float(
                combat_stats.get("fightsWon", combat_stats.get("wins", kills))
            )
            metrics["fights_lost"] = float(
                combat_stats.get("fightsLost", 0 if kills > 0 else 1)
            )

    # Items used during game
    item_stats = result.get("itemStats") or result.get("itemsUsed") or {}
    if isinstance(item_stats, dict):
        metrics["healing_items_used"] = float(item_stats.get("healingUsed", 0))
        metrics["items_collected"] = float(item_stats.get("collected", 0))

    # Last-view metrics
    if last_view:
        self_data = last_view.get("self", {})
        if isinstance(self_data, dict):
            metrics["final_hp"] = float(self_data.get("hp", 0))
            metrics["final_ep"] = float(self_data.get("ep", 0))
            inventory = self_data.get("inventory", [])
            if isinstance(inventory, list):
                metrics["inventory_remaining"] = float(len(inventory))

    # Kill/death ratio
    fights_lost = metrics.get("fights_lost", 0)
    if kills > 0 and fights_lost == 0:
        metrics["kill_death_ratio"] = float(kills)
    else:
        metrics["kill_death_ratio"] = float(kills) / max(fights_lost, 1.0)

    return metrics


def _analyze_resource_efficiency(
    metrics: dict[str, float], death_cause: str
) -> CombatLesson | None:
    """Generate a resource-efficiency CombatLesson from game metrics."""
    smoltz_earned = metrics.get("smoltz_earned", 0)
    kills = metrics.get("kills", 0)
    healing_used = metrics.get("healing_items_used", 0)

    # sMoltz per kill — efficiency metric
    smoltz_per_kill = smoltz_earned / max(kills, 1)

    details: dict[str, object] = {
        "smoltz_per_kill": round(smoltz_per_kill, 1),
        "healing_items_used": int(healing_used),
        "analysis": "",
    }

    if kills == 0 and smoltz_earned == 0:
        details["analysis"] = (
            "No kills and no sMoltz — failed to engage with guardians or monsters"
        )
    elif smoltz_per_kill < 100:
        details["analysis"] = (
            f"Low sMoltz per kill ({smoltz_per_kill:.0f}) — may need more guardian targeting"
        )
    elif smoltz_per_kill >= 120:
        details["analysis"] = (
            f"High sMoltz per kill ({smoltz_per_kill:.0f}) — good guardian farming"
        )

    if healing_used > 0 and kills == 0:
        details["analysis"] = (
            str(details.get("analysis", ""))
            + ". Used healing items but got no kills — wasted resources"
        )

    return CombatLesson(
        game_id="",
        lesson_type="resource",
        cause=death_cause,
        details=details,
        metrics={
            "smoltz_per_kill": smoltz_per_kill,
            "healing_efficiency": 1.0 if healing_used > 0 and kills > 0 else 0.0,
        },
    )


def _analyze_combat_performance(
    metrics: dict[str, float], death_cause: str
) -> CombatLesson | None:
    """Generate a combat-performance CombatLesson."""
    kills = metrics.get("kills", 0)
    damage_dealt = metrics.get("damage_dealt", 0)
    damage_taken = metrics.get("damage_taken", 0)
    kd_ratio = metrics.get("kill_death_ratio", 0)

    if kills == 0 and damage_dealt == 0:
        return None  # No combat occurred

    damage_diff = damage_dealt - damage_taken

    details: dict[str, object] = {
        "damage_dealt": int(damage_dealt),
        "damage_taken": int(damage_taken),
        "damage_differential": int(damage_diff),
        "kill_death_ratio": round(kd_ratio, 2),
        "analysis": "",
    }

    if damage_diff > 50:
        details["analysis"] = (
            "Massive damage differential — overwhelming combat superiority"
        )
    elif damage_diff > 0:
        details["analysis"] = "Positive damage trade — effective combat"
    elif damage_diff < -50:
        details["analysis"] = (
            "Severe damage deficit — losing fights, need to avoid combat"
        )
    else:
        details["analysis"] = "Roughly even damage trade"

    return CombatLesson(
        game_id="",
        lesson_type="combat",
        cause=death_cause,
        details=details,
        metrics={
            "damage_dealt": damage_dealt,
            "damage_taken": damage_taken,
            "damage_differential": damage_diff,
            "kill_death_ratio": kd_ratio,
        },
    )


def _analyze_death(
    result: dict,
    death_cause: str,
    metrics: dict[str, float],
    last_view: dict | None = None,
    stats: dict | None = None,
) -> CombatLesson:
    """Generate the primary death-cause CombatLesson."""
    details = _extract_death_details(result, death_cause, last_view, stats)
    final_hp = metrics.get("final_hp", 0)
    killer_hp = (
        details.pop("killer_hp_remaining", None)
        if "killer_hp_remaining" in details
        else None
    )

    if death_cause == "agent_kill":
        killer_id = (
            details.pop("killer_id", "unknown") if "killer_id" in details else "unknown"
        )
        if killer_hp is not None:
            details["analysis"] = (
                f"Killed by agent {killer_id} (killer HP: {killer_hp}, our HP: {final_hp})"
            )
        else:
            details["analysis"] = f"Killed by agent {killer_id} (our HP: {final_hp})"
    elif death_cause == "guardian_kill":
        details["analysis"] = (
            f"Killed by guardian with HP {final_hp} — engaged while too weak"
        )
    elif death_cause == "death_zone":
        details["analysis"] = "Died to death zone — failed to evacuate in time"
    elif death_cause == "monster_kill":
        details["analysis"] = "Killed by monster — underestimated the threat"
    elif death_cause == "ranked_out":
        details["analysis"] = (
            "Survived to end but didn't win — lost on tiebreaker (rank)"
        )
    else:
        details["analysis"] = (
            f"Unknown death cause at rank {metrics.get('final_rank', 0)}"
        )

    lesson_type = "win" if death_cause == "none" else "death"

    return CombatLesson(
        game_id="",
        lesson_type=lesson_type,
        cause=death_cause,
        details=details,
        metrics=metrics,
    )


def _update_opponent_profiles(memory: AgentMemory, result: dict, game_id: str):
    """Sync opponent profiles from brain's _known_agents into memory.

    For each agent encountered this game:
      - Increment games_faced
      - If we outranked them, increment wins_against (or losses_to if they outranked us)
      - Recalculate threat_rating
    """
    try:
        from bot.strategy.brain import _known_agents as brain_agents
    except ImportError:
        log.debug("brain._known_agents not available — skipping opponent profiling")
        return

    if not brain_agents:
        return

    our_rank = result.get("finalRank", 0)
    our_kills = result.get("kills", 0)
    is_winner = result.get("isWinner", False)

    for agent_id, agent_data in brain_agents.items():
        if not isinstance(agent_data, dict):
            continue

        name = agent_data.get("id", agent_id)
        is_guardian = agent_data.get("isGuardian", False)
        if is_guardian:
            continue  # Skip guardians — only track real agents

        # Get existing profile or create new
        profile = memory.known_agents.get(name)
        if profile is None:
            profile = OpponentProfile(name=name)
            memory.known_agents[name] = profile

        # Update basic tracking
        profile.games_faced += 1
        profile.last_seen = game_id

        # HP tracking — rolling average
        seen_hp = agent_data.get("hp", 100)
        if profile.avg_hp_left == 0:
            profile.avg_hp_left = float(seen_hp)
        else:
            # Exponential moving average
            profile.avg_hp_left = round(
                profile.avg_hp_left * 0.7 + float(seen_hp) * 0.3, 1
            )

        # Win/loss tracking — if we won, we outranked everyone
        # If we didn't win, we still outranked some (rank comparison not granular here)
        if is_winner:
            profile.wins_against += 1
        else:
            profile.losses_to += 1

    # If we were killed by a known agent, track that
    stats = result.get("_stats", {})
    killer = stats.get("killer_name")
    if killer:
        kp = memory.known_agents.get(killer)
        if kp is None:
            kp = OpponentProfile(name=killer)
            memory.known_agents[killer] = kp
        kp.games_faced += 1
        kp.killed_by_count += 1
        kp.last_seen = game_id
        log.info("  👤 Killer tracked: %s (killed_by=%d)", killer, kp.killed_by_count)

    # Recompute all threat ratings after updates
    memory.recompute_threat_ratings()


def _generate_strategy_rules(
    memory: AgentMemory,
    game_id: str,
    death_cause: str,
    metrics: dict[str, float],
    last_view: dict | None = None,
):
    """Generate adaptive StrategyRules from lesson patterns observed in this game.

    Rules are generated with initial confidence (0.5) and are reinforced or
    weakened by future games through add_strategy_rule's weighted average.
    """
    final_hp = metrics.get("final_hp", 100)
    kills = metrics.get("kills", 0)
    is_winner = metrics.get("is_winner", 0) > 0.5

    # ── Death cause rules ──────────────────────────────────────────
    if death_cause == "guardian_kill" and final_hp < 40:
        rule = StrategyRule(
            rule_type="threshold",
            condition={
                "hp_below": max(int(final_hp) + 5, 35),
                "enemy_type": "guardian",
                "rule_key": "guardian_flee",
            },
            action="flee guardians when HP below learned threshold",
            confidence=0.6,
            source_game=game_id,
        )
        memory.add_strategy_rule(rule)
        log.info(
            "  📋 Learned rule: flee guardians when HP < %d", rule.condition["hp_below"]
        )

    if death_cause == "agent_kill" and "killer_id" in metrics:
        killer_id = metrics.get("killer_id", "")
        rule = StrategyRule(
            rule_type="avoid",
            condition={"agent_name": str(killer_id), "reason": "killed_us"},
            action=f"avoid engaging agent {killer_id} — they killed us before",
            confidence=0.6,
            source_game=game_id,
        )
        memory.add_strategy_rule(rule)
        log.info("  📋 Learned rule: avoid agent %s", killer_id)

    if death_cause == "death_zone":
        rule = StrategyRule(
            rule_type="disengage",
            condition={"death_zone_proximity": 2, "rule_key": "dz_evacuate"},
            action="evacuate death zone earlier — died to DZ",
            confidence=0.7,
            source_game=game_id,
        )
        memory.add_strategy_rule(rule)
        log.info("  📋 Learned rule: evacuate death zone earlier")

    # ── Win reinforcement rules ──────────────────────────────────────
    if is_winner and kills >= 3:
        rule = StrategyRule(
            rule_type="engage",
            condition={"min_kills_before_win": kills, "rule_key": "combat_engage"},
            action="current aggressive strategy is working — reinforce thresholds",
            confidence=0.6,
            source_game=game_id,
        )
        memory.add_strategy_rule(rule)
        log.info("  📋 Reinforced: aggressive strategy with %d kills", kills)

    # ── Resource efficiency rules ────────────────────────────────────
    smoltz_per_kill = metrics.get("smoltz_per_kill", 0)
    if smoltz_per_kill > 200:
        rule = StrategyRule(
            rule_type="farm",
            condition={"guardian_value": "high", "rule_key": "farm_guardian"},
            action="guardian farming is highly efficient — prioritize guardians",
            confidence=0.5,
            source_game=game_id,
        )
        memory.add_strategy_rule(rule)
    elif smoltz_per_kill < 50 and kills > 0:
        rule = StrategyRule(
            rule_type="disengage",
            condition={"guardian_value": "low", "rule_key": "farm_guardian"},
            action="guardian farming not efficient — consider alternative sMoltz sources",
            confidence=0.4,
            source_game=game_id,
        )
        memory.add_strategy_rule(rule)

    # ── Healing rules ────────────────────────────────────────────────
    healing_used = metrics.get("healing_items_used", 0)
    if healing_used > 0 and not is_winner and kills == 0:
        rule = StrategyRule(
            rule_type="threshold",
            condition={"hp_below": 25, "rule_key": "critical_heal"},
            action="heal only when HP critically low if not securing kills",
            confidence=0.5,
            source_game=game_id,
        )
        memory.add_strategy_rule(rule)


def _migrate_legacy_lessons(memory: AgentMemory, game_id: str):
    """Convert old string-based lessons to structured CombatLesson format."""
    old_lessons = memory.data.get("overall", {}).get("history", {}).get("lessons", [])
    if not old_lessons:
        return

    migrated = []
    for lesson_str in old_lessons:
        if not isinstance(lesson_str, str):
            continue

        # Classify old lessons by keyword analysis
        if "Won with" in lesson_str or "Win" in lesson_str:
            lesson_type = "win"
            cause = "none"
        elif "Top" in lesson_str:
            lesson_type = "win"
            cause = "ranked_out"
        elif "Zero kills" in lesson_str:
            lesson_type = "loss"
            cause = "unknown"
        elif "guardian" in lesson_str.lower():
            lesson_type = "combat"
            cause = "guardian_kill"
        elif "died" in lesson_str.lower() or "killed" in lesson_str.lower():
            lesson_type = "death"
            cause = "agent_kill"
        else:
            lesson_type = "loss"
            cause = "unknown"

        structured = CombatLesson(
            game_id=game_id or "legacy",
            lesson_type=lesson_type,
            cause=cause,
            details={"legacy_lesson": lesson_str},
            metrics={},
        )
        migrated.append(structured)

    # Replace string lessons with structured ones
    if migrated:
        for lesson in migrated:
            memory.add_combat_lesson(lesson)
        memory.data["overall"]["history"]["lessons"] = []
        log.info("  Migrated %d legacy lessons to structured format", len(migrated))


# ══════════════════════════════════════════════════════════════════════════
# Main entry point
# ══════════════════════════════════════════════════════════════════════════


async def settle_game(
    game_result: dict,
    entry_type: str,
    memory: AgentMemory,
    last_view: dict | None = None,
    action_log: list | None = None,
):
    """
    Process game end with structured analysis pipeline:
    1. Extract final stats from game result + tracked in-game stats
    2. Analyze death cause from result + optional last_view
    3. Build structured CombatLesson objects (death, combat, resource)
    4. Update opponent profiles from brain._known_agents
    5. Generate adaptive StrategyRules from lesson patterns
    6. Migrate legacy string lessons to structured format
    7. Clear temp memory for next game
    """
    # The game_ended WebSocket message has attached _stats and _last_view
    # from the engine in-game tracking (raw message only has gameId + agentId).
    stats = game_result.get("_stats", {})
    last_view = last_view or game_result.get("_last_view")

    # Extract from tracked stats (preferred) or fall back to result fields
    kills = stats.get("kills", game_result.get("kills", 0))
    damage_dealt = stats.get("damage_dealt", 0)
    damage_taken = stats.get("damage_taken", 0)
    fights_won = stats.get("fights_won", 0)
    fights_lost = stats.get("fights_lost", 0)
    killer_name = stats.get("killer_name")

    # Try to derive is_winner from context
    result = game_result.get("result", game_result)
    is_winner = result.get(
        "isWinner", kills > 0 and fights_lost == 0 and not killer_name
    )

    final_rank = 0
    if last_view:
        final_rank = last_view.get("rank", last_view.get("finalRank", 0))
    if not final_rank:
        final_rank = result.get("finalRank", game_result.get("finalRank", 0))

    rewards = result.get("rewards", game_result.get("rewards", {}))
    smoltz_earned = rewards.get("sMoltz", game_result.get("sMoltz", 0))
    moltz_earned = rewards.get("moltz", game_result.get("moltz", 0))
    game_id = game_result.get("gameId", game_result.get("game_id", ""))

    log.info("═══ GAME SETTLEMENT ═══")
    log.info(
        "  Winner: %s | Rank: %d | Kills: %d",
        "YES" if is_winner else "No",
        final_rank,
        kills,
    )
    log.info("  Rewards: %d sMoltz, %d Moltz", smoltz_earned, moltz_earned)

    # ── Step 1: Record game end in memory history (backward compat) ──
    memory.record_game_end(
        is_winner=is_winner,
        final_rank=final_rank,
        kills=kills,
        smoltz_earned=smoltz_earned,
    )

    # ── Step 2: Analyze death cause ───────────────────────────────────
    death_cause = _extract_death_cause(result, last_view)
    metrics = _build_combat_metrics(result, last_view, stats)

    log.info(
        "  Death cause: %s | Final HP: %.0f | DMG dealt/taken: %.0f/%.0f",
        death_cause,
        metrics.get("final_hp", 0),
        metrics.get("damage_dealt", 0),
        metrics.get("damage_taken", 0),
    )

    # ── Step 3: Generate structured CombatLesson objects ──────────────
    # Primary death-analysis lesson
    death_lesson = _analyze_death(result, death_cause, metrics, last_view, stats)
    death_lesson.game_id = game_id
    memory.add_combat_lesson(death_lesson)
    log.info("  📝 Death lesson: %s", death_cause)

    # Combat performance lesson (only if combat occurred)
    combat_lesson = _analyze_combat_performance(metrics, death_cause)
    if combat_lesson:
        combat_lesson.game_id = game_id
        memory.add_combat_lesson(combat_lesson)
        log.info(
            "  📝 Combat lesson: K/D ratio %.2f", metrics.get("kill_death_ratio", 0)
        )

    # Resource efficiency lesson
    resource_lesson = _analyze_resource_efficiency(metrics, death_cause)
    if resource_lesson:
        resource_lesson.game_id = game_id
        memory.add_combat_lesson(resource_lesson)
        spk = metrics.get("smoltz_per_kill", 0)
        log.info("  📝 Resource lesson: %.0f sMoltz/kill", spk)

    # ── Step 4: Legacy string lesson (backward compat) ────────────────
    if is_winner:
        memory.add_lesson(f"Won with {kills} kills at rank {final_rank}")
    elif final_rank <= 3:
        memory.add_lesson(f"Top 3 finish (rank {final_rank}) with {kills} kills")
    elif kills == 0:
        memory.add_lesson(
            "Zero kills — need more aggressive guardian/monster targeting"
        )

    # ── Step 5: Update opponent profiles ──────────────────────────────
    _update_opponent_profiles(memory, result, game_id)
    if memory.known_agents:
        log.info("  👤 Updated %d opponent profiles", len(memory.known_agents))

    # ── Step 6: Generate adaptive strategy rules ──────────────────────
    _generate_strategy_rules(memory, game_id, death_cause, metrics, last_view)

    # ── Step 7: Migrate legacy string lessons to structured format ────
    _migrate_legacy_lessons(memory, game_id)

    # ── Step 8: Action log analysis (if available) ────────────────────
    if action_log and isinstance(action_log, list) and len(action_log) > 0:
        _analyze_action_log(memory, game_id, action_log, death_cause)

    # ── Step 9: Clear temp for next game and persist ──────────────────
    memory.clear_temp()
    await memory.save()

    log.info(
        "Settlement complete — %d lessons, %d rules, %d opponents. Ready for next game.",
        len(memory.lessons),
        len(memory.strategy_rules),
        len(memory.known_agents),
    )


# ══════════════════════════════════════════════════════════════════════════
# Action log analysis (when available)
# ══════════════════════════════════════════════════════════════════════════


def _analyze_action_log(
    memory: AgentMemory, game_id: str, action_log: list, death_cause: str
):
    """Analyze the game action log for patterns about what went wrong.

    Looks for:
      - Repeated failed actions (suggesting poor decision loop)
      - Healing timing relative to death
      - Movement patterns (entering/exiting DZ)
      - Missed opportunities (not picking up items)
    """
    if not action_log:
        return

    fail_count = 0
    action_types: dict[str, int] = {}
    last_heal_turn = -1
    dz_entries = 0
    total_turns = len(action_log)

    for i, entry in enumerate(action_log):
        if not isinstance(entry, dict):
            continue

        # Track action types
        atype = entry.get("type") or entry.get("action", "")
        if atype:
            action_types[atype] = action_types.get(atype, 0) + 1

        # Track failures
        success = entry.get("success", True)
        if not success:
            fail_count += 1

        # Track healing timing
        if atype in ("use_item",):
            data = entry.get("data", {})
            item = data.get("itemId", "")
            if "medkit" in str(item).lower() or "bandage" in str(item).lower():
                last_heal_turn = i

        # Track DZ entries
        if atype in ("move", "rest"):
            data = entry.get("data", {}) or entry.get("result", {})
            region_info = (
                data.get("region", {}) if isinstance(data.get("region"), dict) else {}
            )
            if region_info.get("isDeathZone"):
                dz_entries += 1

    # Generate findings as a CombatLesson
    findings: list[str] = []
    if fail_count > 0:
        findings.append(f"{fail_count} action(s) failed — possible invalid decisions")
    if dz_entries > 1:
        findings.append(
            f"Entered death zone {dz_entries} times — movement planning issue"
        )
    if last_heal_turn > 0 and total_turns - last_heal_turn <= 2:
        findings.append(f"Healed at turn {last_heal_turn} but died shortly after")
    if action_types.get("rest", 0) > 5 and death_cause != "none":
        findings.append(
            f"Rested {action_types['rest']} times — may have been too passive"
        )

    if findings:
        action_lesson = CombatLesson(
            game_id=game_id,
            lesson_type="movement" if dz_entries > 1 else "combat",
            cause=death_cause,
            details={
                "findings": findings,
                "total_turns": total_turns,
                "failed_actions": fail_count,
                "action_breakdown": action_types,
            },
            metrics={
                "fail_rate": round(fail_count / max(total_turns, 1), 2),
                "dz_entry_count": float(dz_entries),
            },
        )
        memory.add_combat_lesson(action_lesson)
        log.info("  🔍 Action log analysis: %d finding(s)", len(findings))
