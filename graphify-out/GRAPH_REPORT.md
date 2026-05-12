# Graph Report - molty5  (2026-05-12)

## Corpus Check
- 39 files · ~52,017 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 684 nodes · 1012 edges · 68 communities detected
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 139 edges (avg confidence: 0.62)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4a3edb97`
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
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
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

## God Nodes (most connected - your core abstractions)
1. `MoltyAPI` - 50 edges
2. `AgentMemory` - 36 edges
3. `APIError` - 31 edges
4. `ActionSender` - 27 edges
5. `Logger Utility` - 26 edges
6. `Agent Instructions Document` - 26 edges
7. `Skill` - 23 edges
8. `WebSocketEngine` - 22 edges
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

## Communities (75 total, 25 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (51): APIError, Heartbeat, Heartbeat loop — main orchestration per heartbeat.md. State machine: setup → joi, Single heartbeat cycle: check state → route → act., Single heartbeat cycle: check state → route → act., Single heartbeat cycle: check state → route → act., Setup pipeline: wallet → whitelist → identity. Respects config flags., Setup pipeline: wallet → whitelist → identity. Respects config flags. (+43 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (37): MoltyAPI, POST /accounts — create account, returns apiKey (shown once!)., GET /accounts/me — readiness check, state detection, balance., PUT /accounts/wallet — attach wallet to existing account., POST /create/wallet — create MoltyRoyale Wallet., POST /whitelist/request — request whitelist approval., POST /api/identity — register ERC-8004 identity., GET /api/identity — check current identity. (+29 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (36): ActionSender, Action envelope builder + cooldown state tracker. Builds action messages per act, Tracks cooldown state and builds action envelopes., Update state from action_result payload.         Per actions.md: canAct and cool, Update state from can_act_changed server push., Can we send a Group 1 (cooldown) action?, Build action envelope per actions.md spec.         Truncates thought fields to s, Per actions.md: requires megaphone item or broadcast_station facility.         S (+28 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (37): api_accounts(), api_accounts_post(), api_export(), api_import(), api_learning(), api_lessons(), api_opponents(), api_state() (+29 more)

### Community 4 - "Community 4"
Cohesion: 0.07
Nodes (36): _analyze_action_log(), _analyze_combat_performance(), _analyze_death(), _analyze_resource_efficiency(), _build_combat_metrics(), _extract_death_cause(), _extract_death_details(), _generate_strategy_rules() (+28 more)

### Community 5 - "Community 5"
Cohesion: 0.11
Nodes (38): Action Payload Reference, Agent Memory & Growth, API Summary, Combat & Items Spec Sheet, CROSS, Moltz, Agent EOA, molty-royale-context.json (+30 more)

### Community 6 - "Community 6"
Cohesion: 0.15
Nodes (26): $(), animateNum(), esc(), fetchAllLearning(), fmt(), itemName(), itemTag(), _logLine() (+18 more)

### Community 7 - "Community 7"
Cohesion: 0.14
Nodes (27): Agent EOA, CROSS (native token), EIP-712 Signing, ERC-8004 Identity, Legacy WalletFactory, Legacy Wallet Withdraw, MoltyRoyale Wallet (SC Wallet), MoltyRoyaleWallet Contract (+19 more)

### Community 8 - "Community 8"
Cohesion: 0.09
Nodes (20): MoltyAPI, bot/config.py, bot/dashboard/server.py, create_app(), Create the aiohttp web application., Start the dashboard server (non-blocking)., Create the aiohttp web application., Start the dashboard server (non-blocking). (+12 more)

### Community 9 - "Community 9"
Cohesion: 0.14
Nodes (20): _collection_upsert(), _get_railway_config(), is_railway(), is_setup_complete(), Railway Variables auto-sync. After account creation, saves API_KEY + private key, ONE-TIME sync of ALL variables to Railway after first-run.     Combines config +, ONE-TIME sync of ALL variables to Railway after first-run.     Combines config +, Sync memory learning data to Railway variable.      Saves only essential fields (+12 more)

### Community 10 - "Community 10"
Cohesion: 0.13
Nodes (17): _filter_agents(), load_agents(), Configuration & constants for Molty Royale AI Agent. All env vars loaded here. N, Filter agents by AGENT_NAMES env var (comma-separated list of agent names)., Filter agents by AGENT_NAMES env var (comma-separated list of agent names)., Warn if multiple agents share the same SC wallet., Select only 1 agent per SC wallet (molty_royale_wallet).     If multiple agents, Warn if multiple agents share the same SC wallet. (+9 more)

### Community 11 - "Community 11"
Cohesion: 0.11
Nodes (12): DashboardState, Update learning data from AgentMemory., Full state snapshot for dashboard API., Full state snapshot for dashboard API., Singleton shared state between bot and dashboard., Singleton shared state between bot and dashboard., Update agent state from bot engine., Update agent state from bot engine. (+4 more)

### Community 12 - "Community 12"
Cohesion: 0.12
Nodes (16): Agent Instructions Document, Project Readme Document, Dashboard Index HTML, Setup Package Init, Strategy Package Init, Utils Package Init, Railway Sync Utility, Version Check Utility (+8 more)

### Community 13 - "Community 13"
Cohesion: 0.14
Nodes (4): AgentMemory, Read/write molty-royale-context.json with overall + temp sections.      New stru, Read/write molty-royale-context.json with overall + temp sections., Add a structured combat lesson, capping at 50.

### Community 14 - "Community 14"
Cohesion: 0.15
Nodes (9): determine_state(), State router — determines agent state from GET /accounts/me response. Routes per, Analyze /accounts/me response → return (state, context).     Context contains re, Logger Utility, EIP-712 Signer Module, Identity Contract Module, Dashboard shared state — bridge between bot engine and web dashboard. Bot writes, Paid game join — EIP-712 sign → POST /games/{id}/join-paid. Per paid-games.md: c (+1 more)

### Community 15 - "Community 15"
Cohesion: 0.22
Nodes (11): Gas Checker Module, get_w3(), Shared Web3 provider for Cross Network (PoA chain). All on-chain calls should us, Get Web3 instance with PoA middleware for Cross Network., approve_whitelist_onchain(), get_molty_wallet_address(), WalletFactory + MoltyRoyaleWallet on-chain calls for whitelist approval. Checks, Resolve MoltyRoyaleWallet address from WalletFactory.getWallets(). Returns None (+3 more)

### Community 16 - "Community 16"
Cohesion: 0.22
Nodes (9): decide_action(), get_weapon_range(), Resolve a connectedRegions entry to a full region object.     Per v1.5.2 gotcha, Get range from equipped weapon., Resolve a connectedRegions entry to a full region object.     Per v1.5.2 gotchas, Main decision engine. Returns action dict or None (wait).      Priority chain, Main decision engine. Returns action dict or None (wait).      Priority chain pe, Get range from equipped weapon. (+1 more)

### Community 17 - "Community 17"
Cohesion: 0.28
Nodes (8): Web3 Provider Module, check_cross_balance(), Gas fee checker — check CROSS balance before any on-chain transaction. If insuff, Check if address has enough CROSS for gas.     Returns (has_enough, balance_wei), Check gas balance synchronously. If insufficient, log instructions and return Fa, Check gas balance. If insufficient, wait and retry every 2 minutes     until gas, require_gas_or_wait(), require_gas_or_wait_async()

### Community 18 - "Community 18"
Cohesion: 0.25
Nodes (9): Autonomous WebSocket Runner Mode, Cost Guidance, Heartbeat Mode, Runtime Modes Document, action messages, agent_view, heartbeat.md, ws/agent (+1 more)

### Community 19 - "Community 19"
Cohesion: 0.25
Nodes (8): _check_pickup(), _pickup_score(), Smart pickup: weapons > healing stockpile > utility > Moltz (always).     Max i, Calculate dynamic pickup score based on current inventory state., Smart pickup: weapons > healing stockpile > utility > Moltz (always).     Max in, Smart pickup: weapons > healing stockpile > utility > Moltz (always).     Max in, Calculate dynamic pickup score based on current inventory state., Calculate dynamic pickup score based on current inventory state.

### Community 20 - "Community 20"
Cohesion: 0.25
Nodes (7): calc_damage(), _get_region_id(), Strategy brain — main decision engine with priority-based action selection. Impl, Damage formula per combat-items.md + game-systems.md weather penalty.     Base:, Extract region ID from either a string or dict entry., Extract region ID from either a string or dict entry., Damage formula per combat-items.md + game-systems.md weather penalty.     Base:

### Community 21 - "Community 21"
Cohesion: 0.29
Nodes (4): RateLimiter, Token-bucket rate limiter for REST (300/min) and WebSocket (120/min). Non-blocki, Async token-bucket rate limiter., Wait until tokens are available. Non-blocking via asyncio.sleep.

### Community 22 - "Community 22"
Cohesion: 0.29
Nodes (7): _check_equip(), get_weapon_bonus(), Get ATK bonus from equipped weapon., Auto-equip best weapon from inventory., Auto-equip best weapon from inventory., Auto-equip best weapon from inventory., Get ATK bonus from equipped weapon.

### Community 23 - "Community 23"
Cohesion: 0.29
Nodes (7): learn_from_map(), Use utility items immediately after pickup.     Map: reveals entire map → trigge, Use utility items immediately after pickup.     Map: reveals entire map → trigge, Called after Map is used — learn entire map layout.     Track all death zones, p, Use utility items immediately after pickup.     Map: reveals entire map → trigg, Called after Map is used — learn entire map layout.     Track all death zones,, _use_utility_item()

### Community 24 - "Community 24"
Cohesion: 0.33
Nodes (4): from_dict(), Load memory from disk. Create default if missing., Read structured fields from self.data after JSON load., Load memory from disk. Create default if missing.

### Community 25 - "Community 25"
Cohesion: 0.33
Nodes (5): check_version(), get_version_header(), Version check — GET /api/version and X-Version header management. Returns 426 VE, Fetch current server version. Returns version string., Return X-Version header dict.

### Community 26 - "Community 26"
Cohesion: 0.33
Nodes (5): Whitelist Contract Module, ensure_whitelist(), Whitelist request + auto-approval (advanced mode). POST /whitelist/request → on-, Request whitelist + auto-approve if advanced mode.     Returns True if whitelist, Request whitelist + auto-approve if advanced mode.     Returns True if whitelist

### Community 27 - "Community 27"
Cohesion: 0.33
Nodes (4): Async REST API client for Molty Royale. All endpoints from api-summary.md with r, Strategy Brain Module, Rate Limiter Utility, WebSocket gameplay engine — wss://cdn.moltyroyale.com/ws/agent. Core loop: conne

### Community 28 - "Community 28"
Cohesion: 0.4
Nodes (3): Persist memory to disk, including structured learning data., Write structured fields into self.data for JSON persistence., Persist memory to disk.

### Community 29 - "Community 29"
Cohesion: 0.4
Nodes (3): OpponentProfile, Update or create an opponent profile with new data., Cross-game tracking of a specific opponent agent.

### Community 30 - "Community 30"
Cohesion: 0.4
Nodes (3): Agent memory — persistent cross-game learning via molty-royale-context.json. Two, Adaptive rule that modifies decision thresholds based on learned experience., StrategyRule

### Community 31 - "Community 31"
Cohesion: 0.4
Nodes (4): Web3 Contracts Module, ERC-8004 Identity Registry on-chain calls. register() from Owner EOA → returns t, Call register() on ERC-8004 Identity Registry from Owner EOA.     Returns tokenI, register_identity_onchain()

### Community 33 - "Community 33"
Cohesion: 0.5
Nodes (4): Select target with lowest HP., Select target with lowest HP., Select target with lowest HP., _select_weakest()

### Community 34 - "Community 34"
Cohesion: 0.5
Nodes (4): _choose_move_target(), Choose best region to move to.     CRITICAL: NEVER move into a death zone or pen, Choose best region to move to.     CRITICAL: NEVER move into a death zone or pen, Choose best region to move to.     CRITICAL: NEVER move into a death zone or pe

### Community 35 - "Community 35"
Cohesion: 0.5
Nodes (4): _is_in_range(), Check if target is in weapon range.     Per combat-items.md: melee = same regio, Check if target is in weapon range.     Per combat-items.md: melee = same region, Check if target is in weapon range.     Per combat-items.md: melee = same region

### Community 36 - "Community 36"
Cohesion: 0.5
Nodes (4): _find_safe_region(), Find nearest connected region that's NOT a death zone AND NOT pending DZ.     P, Find nearest connected region that's NOT a death zone AND NOT pending DZ.     Pe, Find nearest connected region that's NOT a death zone AND NOT pending DZ.     Pe

### Community 37 - "Community 37"
Cohesion: 0.5
Nodes (4): _find_energy_drink(), Find energy drink for EP recovery (+5 EP per combat-items.md)., Find energy drink for EP recovery (+5 EP per combat-items.md)., Find energy drink for EP recovery (+5 EP per combat-items.md).

### Community 38 - "Community 38"
Cohesion: 0.5
Nodes (4): _estimate_enemy_weapon_bonus(), Estimate enemy's weapon bonus from their equipped weapon., Estimate enemy's weapon bonus from their equipped weapon., Estimate enemy's weapon bonus from their equipped weapon.

### Community 39 - "Community 39"
Cohesion: 0.5
Nodes (4): _get_move_ep_cost(), Calculate move EP cost per game-systems.md.     Base: 2. Storm: +1. Water terra, Calculate move EP cost per game-systems.md.     Base: 2. Storm: +1. Water terrai, Calculate move EP cost per game-systems.md.     Base: 2. Storm: +1. Water terrai

### Community 40 - "Community 40"
Cohesion: 0.5
Nodes (4): Track observed agents for threat assessment (agent-memory.md temp.knownAgents)., Track observed agents for threat assessment (agent-memory.md temp.knownAgents)., Track observed agents for threat assessment (agent-memory.md temp.knownAgents)., _track_agents()

### Community 41 - "Community 41"
Cohesion: 0.5
Nodes (4): _find_healing_item(), Find best healing item based on urgency.     critical=True (HP<30): prefer Band, Find best healing item based on urgency.     critical=True (HP<30): prefer Banda, Find best healing item based on urgency.     critical=True (HP<30): prefer Banda

### Community 42 - "Community 42"
Cohesion: 0.5
Nodes (4): Select best facility to interact with per game-systems.md.     Facilities: supp, Select best facility to interact with per game-systems.md.     Facilities: suppl, Select best facility to interact with per game-systems.md.     Facilities: suppl, _select_facility()

### Community 43 - "Community 43"
Cohesion: 0.5
Nodes (3): EIP-712 typed data signing for paid room join. Signs JoinTournament typed data w, Sign EIP-712 typed data for paid room join.     eip712_data comes from GET /game, sign_join_paid()

## Knowledge Gaps
- **308 isolated node(s):** `Molty Royale AI Agent Bot`, `State router — determines agent state from GET /accounts/me response. Routes per`, `Analyze /accounts/me response → return (state, context).     Context contains re`, `Exception`, `Async REST API client for Molty Royale. All endpoints from api-summary.md with r` (+303 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Logger Utility` connect `Community 14` to `Community 0`, `Community 1`, `Community 2`, `Community 3`, `Community 4`, `Community 8`, `Community 9`, `Community 43`, `Community 12`, `Community 15`, `Community 17`, `Community 20`, `Community 25`, `Community 26`, `Community 27`, `Community 30`, `Community 31`?**
  _High betweenness centrality (0.380) - this node is a cross-community bridge._
- **Why does `Heartbeat` connect `Community 8` to `Community 0`, `Community 1`, `Community 4`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **Why does `MoltyAPI` connect `Community 1` to `Community 0`, `Community 26`, `Community 27`, `Community 14`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **Are the 28 inferred relationships involving `MoltyAPI` (e.g. with `.run()` and `run_first_run_intake()`) actually correct?**
  _`MoltyAPI` has 28 INFERRED edges - model-reasoned connections that need verification._
- **Are the 12 inferred relationships involving `AgentMemory` (e.g. with `.__init__()` and `Heartbeat`) actually correct?**
  _`AgentMemory` has 12 INFERRED edges - model-reasoned connections that need verification._
- **Are the 26 inferred relationships involving `APIError` (e.g. with `Heartbeat` and `Heartbeat loop — main orchestration per heartbeat.md. State machine: setup → joi`) actually correct?**
  _`APIError` has 26 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `ActionSender` (e.g. with `.__init__()` and `WebSocketEngine`) actually correct?**
  _`ActionSender` has 10 INFERRED edges - model-reasoned connections that need verification._