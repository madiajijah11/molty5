"""
Agent memory — persistent cross-game learning via molty-royale-context.json.
Two sections: `overall` (persistent) and `temp` (per-game).

New structured learning types (backward-compatible with existing JSON):
  - OpponentProfile: per-agent tracking across games
  - CombatLesson: structured lesson from game analysis
  - StrategyRule: adaptive threshold/decision rules
"""

import json
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional
from bot.config import MEMORY_DIR, MEMORY_FILE
from bot.utils.logger import get_logger

log = get_logger(__name__)

DEFAULT_MEMORY = {
    "overall": {
        "identity": {"name": "", "playstyle": "adaptive guardian hunter"},
        "strategy": {
            "deathzone": "move inward before turn 5",
            "guardians": "engage immediately — highest sMoltz value",
            "weather": "avoid combat in fog or storm",
            "ep_management": "rest when EP < 4 before engaging",
        },
        "history": {
            "totalGames": 0,
            "wins": 0,
            "avgKills": 0.0,
            "lessons": [],
        },
    },
    "temp": {},
}


# ═══════════════════════════════════════════════════════════════════
# Structured Learning Data Types
# ═══════════════════════════════════════════════════════════════════


@dataclass
class OpponentProfile:
    """Cross-game tracking of a specific opponent agent."""

    name: str
    games_faced: int = 0
    wins_against: int = 0  # games we outranked them
    losses_to: int = 0  # games they outranked us
    kill_count: int = 0  # times we killed them
    killed_by_count: int = 0  # times they killed us
    avg_hp_left: float = 0.0  # their avg HP when we last saw them alive
    threat_rating: float = 0.0  # 0.0 = harmless, 1.0 = extremely dangerous
    last_seen: str = ""  # game ID

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "OpponentProfile":
        return cls(
            name=d.get("name", ""),
            games_faced=d.get("games_faced", 0),
            wins_against=d.get("wins_against", 0),
            losses_to=d.get("losses_to", 0),
            kill_count=d.get("kill_count", 0),
            killed_by_count=d.get("killed_by_count", 0),
            avg_hp_left=d.get("avg_hp_left", 0.0),
            threat_rating=d.get("threat_rating", 0.0),
            last_seen=d.get("last_seen", ""),
        )


@dataclass
class CombatLesson:
    """Structured lesson extracted from game outcome analysis."""

    game_id: str
    lesson_type: str  # "win" | "loss" | "death" | "combat" | "resource" | "movement"
    cause: str  # "death_zone" | "agent_kill" | "guardian_kill" | "monster_kill" | "ranked_out"
    details: Dict[str, Any] = field(default_factory=dict)  # context-specific info
    metrics: Dict[str, float] = field(
        default_factory=dict
    )  # numeric data: hp, damage, sMoltz, etc.
    created_at: float = field(default_factory=time.time)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["created_at"] = self.created_at
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "CombatLesson":
        return cls(
            game_id=d.get("game_id", ""),
            lesson_type=d.get("lesson_type", "loss"),
            cause=d.get("cause", "unknown"),
            details=d.get("details", {}),
            metrics=d.get("metrics", {}),
            created_at=d.get("created_at", 0.0),
        )


@dataclass
class StrategyRule:
    """Adaptive rule that modifies decision thresholds based on learned experience."""

    rule_type: str  # "threshold" | "disengage" | "farm" | "engage" | "avoid"
    condition: Dict[str, Any] = field(
        default_factory=dict
    )  # e.g. {"hp_below": 35, "enemy_type": "guardian"}
    action: str = ""  # description of what to do
    confidence: float = 0.5  # 0.0-1.0, how confident we are this rule is correct
    source_game: str = ""  # game ID where this rule was learned
    created_at: float = field(default_factory=time.time)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["created_at"] = self.created_at
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "StrategyRule":
        return cls(
            rule_type=d.get("rule_type", "threshold"),
            condition=d.get("condition", {}),
            action=d.get("action", ""),
            confidence=d.get("confidence", 0.5),
            source_game=d.get("source_game", ""),
            created_at=d.get("created_at", 0.0),
        )


# ═══════════════════════════════════════════════════════════════════
# Memory Class
# ═══════════════════════════════════════════════════════════════════


class AgentMemory:
    """Read/write molty-royale-context.json with overall + temp sections.

    New structured fields (backward-compatible):
      - self.lessons: List[CombatLesson]
      - self.strategy_rules: List[StrategyRule]
      - self.known_agents: Dict[str, OpponentProfile]
    """

    def __init__(self):
        self.data: dict = dict(DEFAULT_MEMORY)
        self._loaded = False
        # Structured learning data (populated during load)
        self.lessons: List[CombatLesson] = []
        self.strategy_rules: List[StrategyRule] = []
        self.known_agents: Dict[str, OpponentProfile] = {}

    async def load(self):
        """Load memory from disk. Create default if missing."""
        MEMORY_DIR.mkdir(parents=True, exist_ok=True)
        if MEMORY_FILE.exists():
            try:
                raw = MEMORY_FILE.read_text(encoding="utf-8")
                self.data = json.loads(raw)
                self._loaded = True
                # Deserialize structured data from JSON
                self._deserialize_from_data()
                log.info(
                    "Memory loaded: %d games, %d lessons, %d strategy_rules, %d opponents",
                    self.data["overall"]["history"]["totalGames"],
                    len(self.lessons),
                    len(self.strategy_rules),
                    len(self.known_agents),
                )
            except (json.JSONDecodeError, KeyError) as e:
                log.warning("Memory file corrupt, using defaults: %s", e)
                self.data = dict(DEFAULT_MEMORY)
        else:
            log.info("No memory file — starting fresh")

    async def save(self):
        """Persist memory to disk, including structured learning data."""
        # Serialize structured data into JSON
        self._serialize_to_data()
        MEMORY_DIR.mkdir(parents=True, exist_ok=True)
        MEMORY_FILE.write_text(
            json.dumps(self.data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        log.debug("Memory saved to %s", MEMORY_FILE)

    # ── Serialization helpers (round-trip safe) ──────────────────────

    def _serialize_to_data(self):
        """Write structured fields into self.data for JSON persistence."""
        overall = self.data.setdefault("overall", {})
        overall["lessons"] = [l.to_dict() for l in self.lessons]
        overall["strategy_rules"] = [r.to_dict() for r in self.strategy_rules]
        overall["known_agents"] = {
            name: p.to_dict() for name, p in self.known_agents.items()
        }

    def _deserialize_from_data(self):
        """Read structured fields from self.data after JSON load."""
        overall = self.data.get("overall", {})
        # Structured lessons (new format)
        raw_lessons = overall.get("lessons", [])
        if raw_lessons:
            self.lessons = [CombatLesson.from_dict(l) for l in raw_lessons]
        # Migrate old string lessons to CombatLesson format
        old_lessons = overall.get("history", {}).get("lessons", [])
        if old_lessons and isinstance(old_lessons[0], str):
            for s in old_lessons:
                self.lessons.append(
                    CombatLesson(
                        game_id="legacy",
                        lesson_type="loss",
                        cause="unknown",
                        details={"legacy_lesson": s},
                    )
                )
            # Clear old string lessons after migration
            overall["history"]["lessons"] = []

        self.strategy_rules = [
            StrategyRule.from_dict(r) for r in overall.get("strategy_rules", [])
        ]
        self.known_agents = {
            name: OpponentProfile.from_dict(p)
            for name, p in overall.get("known_agents", {}).items()
        }

    # ── Accessors ────────────────────────────────────────────────────

    def set_agent_name(self, name: str):
        self.data["overall"]["identity"]["name"] = name

    def get_strategy(self) -> dict:
        return self.data.get("overall", {}).get("strategy", {})

    def get_lessons(self) -> list:
        return self.data.get("overall", {}).get("history", {}).get("lessons", [])

    # ── Structured learning accessors ─────────────────────────────────

    def get_adaptive_thresholds(self) -> Dict[str, Any]:
        """Return learned threshold values for brain.py decisions.

        Returns dict with keys like:
          - guardian_flee_hp: HP below which to flee guardians
          - combat_engage_hp: min HP to engage agents
          - critical_heal_hp: HP threshold for urgent healing
          - farm_guardian_hp: min HP to farm guardians
        Defaults are the current hardcoded values from brain.py.
        """
        defaults = {
            "guardian_flee_hp": 40,
            "combat_engage_hp_early": 40,
            "combat_engage_hp_late": 25,
            "critical_heal_hp": 30,
            "pre_heal_hp": 70,
            "farm_guardian_hp": 40,
        }
        # Apply strategy_rules that override thresholds
        for rule in self.strategy_rules:
            if rule.rule_type != "threshold":
                continue
            if rule.confidence < 0.3:
                continue  # not confident enough
            cond = rule.condition
            hp_val = cond.get("hp_below")
            if hp_val is None:
                continue
            key_map = {
                "guardian_flee": "guardian_flee_hp",
                "combat_engage": "combat_engage_hp_early",
                "combat_engage_late": "combat_engage_hp_late",
                "critical_heal": "critical_heal_hp",
                "pre_heal": "pre_heal_hp",
                "farm_guardian": "farm_guardian_hp",
            }
            override_key = cond.get("rule_key", "")
            mapped = key_map.get(override_key)
            if mapped:
                # Blend: move threshold toward learned value weighted by confidence
                old = defaults[mapped]
                learned = int(hp_val)
                defaults[mapped] = int(old + (learned - old) * rule.confidence)
        return defaults

    def get_opponent_profile(self, name: str) -> Optional[OpponentProfile]:
        """Get cross-game profile for a specific opponent."""
        return self.known_agents.get(name)

    def get_dangerous_opponents(self, min_threat: float = 0.4) -> List[OpponentProfile]:
        """Return opponents with threat_rating above threshold, sorted."""
        dangerous = [
            p for p in self.known_agents.values() if p.threat_rating >= min_threat
        ]
        dangerous.sort(key=lambda p: p.threat_rating, reverse=True)
        return dangerous

    # ── Temp (per-game) ───────────────────────────────────────────────

    def set_temp_game(self, game_id: str):
        self.data["temp"] = {
            "gameId": game_id,
            "currentStrategy": "adaptive",
            "knownAgents": [],
            "notes": "",
        }

    def update_temp_note(self, note: str):
        if "temp" not in self.data:
            self.data["temp"] = {}
        existing = self.data["temp"].get("notes", "")
        self.data["temp"]["notes"] = f"{existing}\n{note}".strip()

    def clear_temp(self):
        self.data["temp"] = {}

    # ── History update (after game end) ───────────────────────────────

    def record_game_end(
        self, is_winner: bool, final_rank: int, kills: int, smoltz_earned: int = 0
    ):
        history = self.data["overall"]["history"]
        history["totalGames"] += 1
        if is_winner:
            history["wins"] += 1

        # Rolling average kills
        total = history["totalGames"]
        old_avg = history["avgKills"]
        history["avgKills"] = round(((old_avg * (total - 1)) + kills) / total, 2)

    def add_lesson(self, lesson: str, max_lessons: int = 20):
        """Append a new lesson, keeping max_lessons most recent."""
        lessons = self.data["overall"]["history"]["lessons"]
        if lesson not in lessons:
            lessons.append(lesson)
            if len(lessons) > max_lessons:
                lessons.pop(0)

    # ── Structured lesson & opponent methods ──────────────────────────

    def add_combat_lesson(self, lesson: CombatLesson):
        """Add a structured combat lesson, capping at 50."""
        self.lessons.append(lesson)
        if len(self.lessons) > 50:
            self.lessons = self.lessons[-50:]

    def add_strategy_rule(self, rule: StrategyRule):
        """Add or update a strategy rule. Deduplicates by rule_type + condition."""
        # Check for existing similar rule
        for existing in self.strategy_rules:
            if (
                existing.rule_type == rule.rule_type
                and existing.condition == rule.condition
            ):
                # Update confidence with weighted average
                existing.confidence = (existing.confidence + rule.confidence) / 2.0
                existing.source_game = rule.source_game
                return
        self.strategy_rules.append(rule)
        if len(self.strategy_rules) > 30:
            self.strategy_rules = self.strategy_rules[-30:]

    def update_opponent_profile(self, name: str, **kwargs):
        """Update or create an opponent profile with new data."""
        profile = self.known_agents.get(name)
        if profile is None:
            profile = OpponentProfile(name=name)
            self.known_agents[name] = profile

        for key, value in kwargs.items():
            if hasattr(profile, key):
                current = getattr(profile, key)
                if isinstance(current, (int, float)):
                    # Accumulate numeric fields
                    setattr(profile, key, current + value)
                else:
                    setattr(profile, key, value)

    def recompute_threat_ratings(self):
        """Recalculate threat_rating for all opponents based on stats."""
        for profile in self.known_agents.values():
            if profile.games_faced == 0:
                profile.threat_rating = 0.0
                continue
            # Threat = weighted combination of kill rate and win rate
            kill_rate = profile.killed_by_count / max(profile.games_faced, 1)
            loss_rate = profile.losses_to / max(profile.games_faced, 1)
            profile.threat_rating = round(
                min(1.0, (kill_rate * 0.6 + loss_rate * 0.4)), 2
            )

    # ── Memory stats for dashboard ────────────────────────────────────

    def get_stats(self) -> Dict[str, Any]:
        """Return memory statistics for dashboard display."""
        total = self.data["overall"]["history"]["totalGames"]
        wins = self.data["overall"]["history"]["wins"]
        return {
            "total_games": total,
            "wins": wins,
            "win_rate": round(wins / max(total, 1), 3),
            "avg_kills": self.data["overall"]["history"]["avgKills"],
            "lessons_count": len(self.lessons),
            "rules_count": len(self.strategy_rules),
            "opponents_count": len(self.known_agents),
            # Full structured data for dashboard Learning tab
            "lessons": [
                {
                    "game_id": l.game_id,
                    "lesson_type": l.lesson_type,
                    "cause": l.cause,
                    "details": l.details,
                    "metrics": l.metrics,
                    "created_at": l.created_at,
                }
                for l in self.lessons[-20:]  # last 20 lessons
            ],
            "strategy_rules": [
                {
                    "rule_type": r.rule_type,
                    "condition": r.condition,
                    "action": r.action,
                    "confidence": r.confidence,
                    "source_game": r.source_game,
                    "created_at": r.created_at,
                }
                for r in self.strategy_rules[-15:]  # last 15 rules
            ],
            "opponents": [
                {
                    "name": p.name,
                    "threat": p.threat_rating,
                    "killed_by": p.killed_by_count,
                    "kills": p.kill_count,
                    "games": p.games_faced,
                    "wins_against": p.wins_against,
                    "losses_to": p.losses_to,
                    "avg_hp_left": p.avg_hp_left,
                }
                for p in sorted(
                    self.known_agents.values(),
                    key=lambda p: p.threat_rating,
                    reverse=True,
                )[:15]
            ],
            "dangerous_opponents": [
                {
                    "name": p.name,
                    "threat": p.threat_rating,
                    "killed_by": p.killed_by_count,
                    "games": p.games_faced,
                }
                for p in self.get_dangerous_opponents(0.3)
            ],
        }
