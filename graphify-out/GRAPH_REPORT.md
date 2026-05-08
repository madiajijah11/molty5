# Graph Report - molty5  (2026-05-05)

## Corpus Check
- 39 files · ~51,624 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 650 nodes · 971 edges · 72 communities detected
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 137 edges (avg confidence: 0.62)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8a4cdce7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 67|Community 67]]
- [[_COMMUNITY_Community 68|Community 68]]
- [[_COMMUNITY_Community 69|Community 69]]
- [[_COMMUNITY_Community 70|Community 70]]
- [[_COMMUNITY_Community 71|Community 71]]
- [[_COMMUNITY_Community 72|Community 72]]
- [[_COMMUNITY_Community 73|Community 73]]
- [[_COMMUNITY_Community 74|Community 74]]
- [[_COMMUNITY_Community 75|Community 75]]
- [[_COMMUNITY_Community 76|Community 76]]
- [[_COMMUNITY_Community 77|Community 77]]
- [[_COMMUNITY_Community 78|Community 78]]

## God Nodes (most connected - your core abstractions)
1. `MoltyAPI` - 50 edges
2. `AgentMemory` - 36 edges
3. `APIError` - 31 edges
4. `ActionSender` - 27 edges
5. `Logger Utility` - 26 edges
6. `Agent Instructions Document` - 26 edges
7. `Skill` - 23 edges
8. `WebSocketEngine` - 21 edges
9. `decide_action()` - 21 edges
10. `Setup Guide Document` - 19 edges

## Surprising Connections (you probably didn't know these)
- `Agent Instructions Document` --references--> `Whitelist Setup Module`  [EXTRACTED]
  AGENTS.md → bot/setup/whitelist.py
- `Agent Instructions Document` --references--> `Strategy Brain Module`  [EXTRACTED]
  AGENTS.md → bot/strategy/brain.py
- `Agent Instructions Document` --references--> `EIP-712 Signer Module`  [EXTRACTED]
  AGENTS.md → bot/web3/eip712_signer.py
- `Agent Instructions Document` --references--> `Gas Checker Module`  [EXTRACTED]
  AGENTS.md → bot/web3/gas_checker.py
- `Agent Instructions Document` --references--> `Identity Contract Module`  [EXTRACTED]
  AGENTS.md → bot/web3/identity_contract.py

## Hyperedges (group relationships)
- **Heartbeat Lifecycle** — heartbeat_Heartbeat, state_router_determine_state, game_room_selector_select_room, game_websocket_engine_WebSocketEngine, game_settlement_settle_game [EXTRACTED 1.00]
- **Dashboard Data Flow** — dashboard_state_singleton, heartbeat_Heartbeat, game_websocket_engine_WebSocketEngine, dashboard_server_start_dashboard [INFERRED 0.80]
- **Setup Package Modules** — bot_setup_whitelist, bot_setup_init [EXTRACTED 1.00]
- **Strategy Package Modules** — bot_strategy_brain, bot_strategy_init [EXTRACTED 1.00]
- **Utils Package Modules** — bot_utils_logger, bot_utils_railway_sync, bot_utils_rate_limiter, bot_utils_version_check, bot_utils_init [EXTRACTED 1.00]
- **Web3 Package Modules** — bot_web3_contracts, bot_web3_eip712_signer, bot_web3_gas_checker, bot_web3_identity_contract, bot_web3_provider, bot_web3_wallet_manager, bot_web3_whitelist_contract, bot_web3_init [EXTRACTED 1.00]
- **Gameplay Flow** — skill, heartbeat, game-loop, concept_websocket-gameplay [INFERRED 0.85]
- **Wallet Setup Flow** — setup, concept_wallet-types, concept_agent-eoa, concept_owner-eoa, concept_molty-wallet [INFERRED 0.90]
- **Paid Room Flow** — paid-games, concept_eip712, concept_sMoltz, concept_Moltz, contracts [INFERRED 0.85]
- **Free Room Flow** — free-games, identity, concept_erc8004 [INFERRED 0.90]
- **Wallet Ecosystem** — setup_AgentEOA, setup_OwnerEOA, setup_MoltyRoyaleWallet [EXTRACTED 1.00]
- **Setup Flow** — setup_PostAccounts, setup_PutAccountsWallet, setup_PostWhitelistRequest, setup_PostCreateWallet [EXTRACTED 1.00]
- **Legacy Withdraw Flow** — setup_LegacyWalletFactory, setup_MoltzERC20, setup_CROSS, setup_OwnerEOA [EXTRACTED 1.00]

## Communities (79 total, 21 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (37): MoltyAPI, POST /accounts — create account, returns apiKey (shown once!)., GET /accounts/me — readiness check, state detection, balance., PUT /accounts/wallet — attach wallet to existing account., POST /create/wallet — create MoltyRoyale Wallet., POST /whitelist/request — request whitelist approval., POST /api/identity — register ERC-8004 identity., GET /api/identity — check current identity. (+29 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (32): Strategy Brain Module, ActionSender, Tracks cooldown state and builds action envelopes., Update state from action_result payload.         Per actions.md: canAct and cool, Update state from can_act_changed server push., Can we send a Group 1 (cooldown) action?, Build action envelope per actions.md spec.         Truncates thought fields to s, Per actions.md: requires megaphone item or broadcast_station facility.         S (+24 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (37): api_accounts(), api_accounts_post(), api_export(), api_import(), api_learning(), api_lessons(), api_opponents(), api_state() (+29 more)

### Community 3 - "Community 3"
Cohesion: 0.11
Nodes (38): Action Payload Reference, Agent Memory & Growth, API Summary, Combat & Items Spec Sheet, CROSS, Moltz, Agent EOA, molty-royale-context.json (+30 more)

### Community 4 - "Community 4"
Cohesion: 0.15
Nodes (26): $(), animateNum(), esc(), fetchAllLearning(), fmt(), itemName(), itemTag(), _logLine() (+18 more)

### Community 5 - "Community 5"
Cohesion: 0.14
Nodes (27): Agent EOA, CROSS (native token), EIP-712 Signing, ERC-8004 Identity, Legacy WalletFactory, Legacy Wallet Withdraw, MoltyRoyale Wallet (SC Wallet), MoltyRoyaleWallet Contract (+19 more)

### Community 6 - "Community 6"
Cohesion: 0.08
Nodes (10): AgentMemory, Read/write molty-royale-context.json with overall + temp sections.      New stru, Return learned threshold values for brain.py decisions.          Returns dict wi, Get cross-game profile for a specific opponent., Return opponents with threat_rating above threshold, sorted., Read/write molty-royale-context.json with overall + temp sections., Add a structured combat lesson, capping at 50., Add or update a strategy rule. Deduplicates by rule_type + condition. (+2 more)

### Community 7 - "Community 7"
Cohesion: 0.09
Nodes (20): MoltyAPI, bot/config.py, bot/dashboard/server.py, create_app(), Create the aiohttp web application., Start the dashboard server (non-blocking)., Create the aiohttp web application., Start the dashboard server (non-blocking). (+12 more)

### Community 8 - "Community 8"
Cohesion: 0.1
Nodes (13): DashboardState, Dashboard shared state — bridge between bot engine and web dashboard. Bot writes, Update learning data from AgentMemory., Full state snapshot for dashboard API., Full state snapshot for dashboard API., Singleton shared state between bot and dashboard., Singleton shared state between bot and dashboard., Update agent state from bot engine. (+5 more)

### Community 9 - "Community 9"
Cohesion: 0.13
Nodes (17): _filter_agents(), load_agents(), Configuration & constants for Molty Royale AI Agent. All env vars loaded here. N, Filter agents by AGENT_NAMES env var (comma-separated list of agent names)., Filter agents by AGENT_NAMES env var (comma-separated list of agent names)., Warn if multiple agents share the same SC wallet., Select only 1 agent per SC wallet (molty_royale_wallet).     If multiple agents, Warn if multiple agents share the same SC wallet. (+9 more)

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (16): Agent Instructions Document, Project Readme Document, Dashboard Index HTML, Setup Package Init, Strategy Package Init, Utils Package Init, Railway Sync Utility, Version Check Utility (+8 more)

### Community 11 - "Community 11"
Cohesion: 0.21
Nodes (11): APIError, Setup pipeline: wallet → whitelist → identity. Respects config flags., Setup pipeline: wallet → whitelist → identity. Respects config flags., Setup pipeline: wallet → whitelist → identity. Respects config flags., Setup pipeline: wallet → whitelist → identity. Respects config flags., Exception, ensure_molty_wallet(), MoltyRoyale Wallet (SC Wallet) setup — POST /create/wallet. Handles CONFLICT, WA (+3 more)

### Community 12 - "Community 12"
Cohesion: 0.22
Nodes (11): Gas Checker Module, get_w3(), Shared Web3 provider for Cross Network (PoA chain). All on-chain calls should us, Get Web3 instance with PoA middleware for Cross Network., approve_whitelist_onchain(), get_molty_wallet_address(), WalletFactory + MoltyRoyaleWallet on-chain calls for whitelist approval. Checks, Resolve MoltyRoyaleWallet address from WalletFactory.getWallets(). Returns None (+3 more)

### Community 13 - "Community 13"
Cohesion: 0.26
Nodes (11): _collection_upsert(), _get_railway_config(), is_railway(), is_setup_complete(), Railway Variables auto-sync. After account creation, saves API_KEY + private key, ONE-TIME sync of ALL variables to Railway after first-run.     Combines config +, Check if running on Railway., Check if first-run sync was already done (prevents redeploy loop). (+3 more)

### Community 14 - "Community 14"
Cohesion: 0.18
Nodes (9): Logger Utility, EIP-712 Signer Module, Action envelope builder + cooldown state tracker. Builds action messages per act, join_paid_game(), Paid game join — EIP-712 sign → POST /games/{id}/join-paid. Per paid-games.md: c, Join a paid room via EIP-712 signed flow.     Returns (game_id, agent_id) when r, EIP-712 typed data signing for paid room join. Signs JoinTournament typed data w, Sign EIP-712 typed data for paid room join.     eip712_data comes from GET /game (+1 more)

### Community 15 - "Community 15"
Cohesion: 0.22
Nodes (8): Heartbeat, Heartbeat loop — main orchestration per heartbeat.md. State machine: setup → joi, Main heartbeat loop — runs forever, manages the full agent lifecycle., Main heartbeat loop — runs forever, manages the full agent lifecycle., main(), Molty Royale AI Agent — Entry Point v2.0. Run: python -m bot.main Dashboard + Mu, Entry point for the bot., Whitelist Setup Module

### Community 16 - "Community 16"
Cohesion: 0.18
Nodes (10): _get_region_id(), learn_from_map(), Strategy brain — main decision engine with priority-based action selection. Impl, Called after Map is used — learn entire map layout.     Track all death zones, p, Extract region ID from either a string or dict entry., Reset per-game tracking state. Call when game ends., Extract region ID from either a string or dict entry., Reset per-game tracking state. Call when game ends. (+2 more)

### Community 17 - "Community 17"
Cohesion: 0.2
Nodes (8): Resume or start playing an active game.         Per game-loop.md: always connec, Run the WebSocket gameplay engine., Resume or start playing an active game.         Per game-loop.md: always connect, Resume or start playing an active game.         Per game-loop.md: always connect, Resume or start playing an active game.         Per game-loop.md: always connect, Run the WebSocket gameplay engine., Run the WebSocket gameplay engine., Run the WebSocket gameplay engine.

### Community 18 - "Community 18"
Cohesion: 0.2
Nodes (8): Web3 Contracts Module, Identity Contract Module, ensure_identity(), ERC-8004 Identity registration — on-chain register() + POST /api/identity. Never, Ensure ERC-8004 identity is registered.     Returns True if identity is set. Nev, ERC-8004 Identity Registry on-chain calls. register() from Owner EOA → returns t, Call register() on ERC-8004 Identity Registry from Owner EOA.     Returns tokenI, register_identity_onchain()

### Community 19 - "Community 19"
Cohesion: 0.22
Nodes (9): _build_combat_metrics(), _extract_death_cause(), Process game end:     1. Extract final stats     2. Update memory (overall his, Extract numeric combat metrics from the game result., Extract numeric combat metrics from the game result + tracked stats., Determine what killed the agent: death_zone, agent_kill, guardian_kill,     mons, Process game end with structured analysis pipeline:     1. Extract final stats f, Process game end with structured analysis pipeline:     1. Extract final stats f (+1 more)

### Community 20 - "Community 20"
Cohesion: 0.22
Nodes (8): _analyze_resource_efficiency(), _migrate_legacy_lessons(), Generate a resource-efficiency CombatLesson from game metrics., Generate a resource-efficiency CombatLesson from game metrics., Convert old string-based lessons to structured CombatLesson format., Convert old string-based lessons to structured CombatLesson format., CombatLesson, Structured lesson extracted from game outcome analysis.

### Community 21 - "Community 21"
Cohesion: 0.22
Nodes (7): Join a game based on room selection., Join a game based on room selection., Join a game based on room selection., Join a game based on room selection., join_free_game(), Free game join via matchmaking queue. POST /join (Long Poll ~15s) → assigned → o, Enter free matchmaking queue and wait for assignment.     Returns (game_id, agen

### Community 22 - "Community 22"
Cohesion: 0.22
Nodes (9): decide_action(), _find_energy_drink(), Use utility items immediately after pickup.     Map: reveals entire map → trigge, Main decision engine. Returns action dict or None (wait).      Priority chain, Main decision engine. Returns action dict or None (wait).      Priority chain pe, Find energy drink for EP recovery (+5 EP per combat-items.md)., Use utility items immediately after pickup.     Map: reveals entire map → trigg, Find energy drink for EP recovery (+5 EP per combat-items.md). (+1 more)

### Community 23 - "Community 23"
Cohesion: 0.28
Nodes (8): Web3 Provider Module, check_cross_balance(), Gas fee checker — check CROSS balance before any on-chain transaction. If insuff, Check if address has enough CROSS for gas.     Returns (has_enough, balance_wei), Check gas balance synchronously. If insufficient, log instructions and return Fa, Check gas balance. If insufficient, wait and retry every 2 minutes     until gas, require_gas_or_wait(), require_gas_or_wait_async()

### Community 24 - "Community 24"
Cohesion: 0.25
Nodes (9): Autonomous WebSocket Runner Mode, Cost Guidance, Heartbeat Mode, Runtime Modes Document, action messages, agent_view, heartbeat.md, ws/agent (+1 more)

### Community 25 - "Community 25"
Cohesion: 0.29
Nodes (7): _analyze_death(), _extract_death_details(), Game settlement — Phase 3: process game end, update memory, prepare for next gam, Generate the primary death-cause CombatLesson., Generate the primary death-cause CombatLesson., Build a details dict with contextual information about the death., Build a details dict with contextual information about the death.

### Community 26 - "Community 26"
Cohesion: 0.25
Nodes (6): Sync opponent profiles from brain's _known_agents into memory.      For each age, Sync opponent profiles from brain's _known_agents into memory.      For each age, _update_opponent_profiles(), OpponentProfile, Update or create an opponent profile with new data., Cross-game tracking of a specific opponent agent.

### Community 27 - "Community 27"
Cohesion: 0.29
Nodes (4): RateLimiter, Token-bucket rate limiter for REST (300/min) and WebSocket (120/min). Non-blocki, Async token-bucket rate limiter., Wait until tokens are available. Non-blocking via asyncio.sleep.

### Community 28 - "Community 28"
Cohesion: 0.29
Nodes (6): _generate_strategy_rules(), Generate adaptive StrategyRules from lesson patterns observed in this game., Generate adaptive StrategyRules from lesson patterns observed in this game., Agent memory — persistent cross-game learning via molty-royale-context.json. Two, Adaptive rule that modifies decision thresholds based on learned experience., StrategyRule

### Community 29 - "Community 29"
Cohesion: 0.33
Nodes (3): Persist memory to disk, including structured learning data., Write structured fields into self.data for JSON persistence., Persist memory to disk.

### Community 30 - "Community 30"
Cohesion: 0.33
Nodes (4): from_dict(), Load memory from disk. Create default if missing., Read structured fields from self.data after JSON load., Load memory from disk. Create default if missing.

### Community 31 - "Community 31"
Cohesion: 0.33
Nodes (4): Single heartbeat cycle: check state → route → act., Single heartbeat cycle: check state → route → act., Entry point — runs the heartbeat loop indefinitely., Entry point — runs the heartbeat loop indefinitely.

### Community 32 - "Community 32"
Cohesion: 0.33
Nodes (6): _check_pickup(), _pickup_score(), Smart pickup: weapons > healing stockpile > utility > Moltz (always).     Max i, Calculate dynamic pickup score based on current inventory state., Smart pickup: weapons > healing stockpile > utility > Moltz (always).     Max in, Calculate dynamic pickup score based on current inventory state.

### Community 33 - "Community 33"
Cohesion: 0.33
Nodes (6): _check_equip(), get_weapon_bonus(), Get ATK bonus from equipped weapon., Auto-equip best weapon from inventory., Auto-equip best weapon from inventory., Get ATK bonus from equipped weapon.

### Community 34 - "Community 34"
Cohesion: 0.33
Nodes (5): check_version(), get_version_header(), Version check — GET /api/version and X-Version header management. Returns 426 VE, Fetch current server version. Returns version string., Return X-Version header dict.

### Community 35 - "Community 35"
Cohesion: 0.33
Nodes (5): Whitelist Contract Module, ensure_whitelist(), Whitelist request + auto-approval (advanced mode). POST /whitelist/request → on-, Request whitelist + auto-approve if advanced mode.     Returns True if whitelist, Request whitelist + auto-approve if advanced mode.     Returns True if whitelist

### Community 36 - "Community 36"
Cohesion: 0.5
Nodes (3): determine_state(), State router — determines agent state from GET /accounts/me response. Routes per, Analyze /accounts/me response → return (state, context).     Context contains re

### Community 37 - "Community 37"
Cohesion: 0.67
Nodes (3): _analyze_combat_performance(), Generate a combat-performance CombatLesson., Generate a combat-performance CombatLesson.

### Community 38 - "Community 38"
Cohesion: 0.67
Nodes (3): _analyze_action_log(), Analyze the game's action log for patterns about what went wrong.      Looks for, Analyze the game action log for patterns about what went wrong.      Looks for:

### Community 40 - "Community 40"
Cohesion: 0.67
Nodes (3): Select target with lowest HP., Select target with lowest HP., _select_weakest()

### Community 41 - "Community 41"
Cohesion: 0.67
Nodes (3): Select best facility to interact with per game-systems.md.     Facilities: supp, Select best facility to interact with per game-systems.md.     Facilities: suppl, _select_facility()

### Community 42 - "Community 42"
Cohesion: 0.67
Nodes (3): _is_in_range(), Check if target is in weapon range.     Per combat-items.md: melee = same regio, Check if target is in weapon range.     Per combat-items.md: melee = same region

### Community 43 - "Community 43"
Cohesion: 0.67
Nodes (3): _find_safe_region(), Find nearest connected region that's NOT a death zone AND NOT pending DZ.     P, Find nearest connected region that's NOT a death zone AND NOT pending DZ.     Pe

### Community 44 - "Community 44"
Cohesion: 0.67
Nodes (3): _estimate_enemy_weapon_bonus(), Estimate enemy's weapon bonus from their equipped weapon., Estimate enemy's weapon bonus from their equipped weapon.

### Community 45 - "Community 45"
Cohesion: 0.67
Nodes (3): _choose_move_target(), Choose best region to move to.     CRITICAL: NEVER move into a death zone or pen, Choose best region to move to.     CRITICAL: NEVER move into a death zone or pe

### Community 46 - "Community 46"
Cohesion: 0.67
Nodes (3): Track observed agents for threat assessment (agent-memory.md temp.knownAgents)., Track observed agents for threat assessment (agent-memory.md temp.knownAgents)., _track_agents()

### Community 47 - "Community 47"
Cohesion: 0.67
Nodes (3): Resolve a connectedRegions entry to a full region object.     Per v1.5.2 gotcha, Resolve a connectedRegions entry to a full region object.     Per v1.5.2 gotchas, _resolve_region()

### Community 48 - "Community 48"
Cohesion: 0.67
Nodes (3): _get_move_ep_cost(), Calculate move EP cost per game-systems.md.     Base: 2. Storm: +1. Water terra, Calculate move EP cost per game-systems.md.     Base: 2. Storm: +1. Water terrai

### Community 49 - "Community 49"
Cohesion: 0.67
Nodes (3): _find_healing_item(), Find best healing item based on urgency.     critical=True (HP<30): prefer Band, Find best healing item based on urgency.     critical=True (HP<30): prefer Banda

### Community 50 - "Community 50"
Cohesion: 0.67
Nodes (3): get_weapon_range(), Get range from equipped weapon., Get range from equipped weapon.

### Community 51 - "Community 51"
Cohesion: 0.67
Nodes (3): calc_damage(), Damage formula per combat-items.md + game-systems.md weather penalty.     Base:, Damage formula per combat-items.md + game-systems.md weather penalty.     Base:

## Knowledge Gaps
- **277 isolated node(s):** `Molty Royale AI Agent Bot`, `State router — determines agent state from GET /accounts/me response. Routes per`, `Analyze /accounts/me response → return (state, context).     Context contains re`, `Exception`, `Async REST API client for Molty Royale. All endpoints from api-summary.md with r` (+272 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **21 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Logger Utility` connect `Community 14` to `Community 0`, `Community 1`, `Community 2`, `Community 7`, `Community 8`, `Community 10`, `Community 11`, `Community 12`, `Community 13`, `Community 15`, `Community 16`, `Community 18`, `Community 21`, `Community 23`, `Community 25`, `Community 28`, `Community 34`, `Community 35`, `Community 36`, `Community 52`?**
  _High betweenness centrality (0.378) - this node is a cross-community bridge._
- **Why does `Heartbeat` connect `Community 7` to `Community 0`, `Community 11`, `Community 14`, `Community 18`, `Community 19`, `Community 21`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Why does `MoltyAPI` connect `Community 0` to `Community 35`, `Community 11`, `Community 14`, `Community 15`, `Community 17`, `Community 18`, `Community 52`, `Community 21`, `Community 31`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._
- **Are the 28 inferred relationships involving `MoltyAPI` (e.g. with `.run()` and `run_first_run_intake()`) actually correct?**
  _`MoltyAPI` has 28 INFERRED edges - model-reasoned connections that need verification._
- **Are the 12 inferred relationships involving `AgentMemory` (e.g. with `.__init__()` and `Heartbeat`) actually correct?**
  _`AgentMemory` has 12 INFERRED edges - model-reasoned connections that need verification._
- **Are the 26 inferred relationships involving `APIError` (e.g. with `Heartbeat` and `Heartbeat loop — main orchestration per heartbeat.md. State machine: setup → joi`) actually correct?**
  _`APIError` has 26 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `ActionSender` (e.g. with `WebSocketEngine` and `.__init__()`) actually correct?**
  _`ActionSender` has 10 INFERRED edges - model-reasoned connections that need verification._