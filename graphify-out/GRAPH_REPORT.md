# Graph Report - .  (2026-05-04)

## Corpus Check
- Corpus is ~45,811 words - fits in a single context window. You may not need a graph.

## Summary
- 493 nodes · 774 edges · 48 communities detected
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 130 edges (avg confidence: 0.61)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Heartbeat & State Machine|Heartbeat & State Machine]]
- [[_COMMUNITY_API Client & Account Setup|API Client & Account Setup]]
- [[_COMMUNITY_Combat Strategy AI|Combat Strategy AI]]
- [[_COMMUNITY_Game Reference Documentation|Game Reference Documentation]]
- [[_COMMUNITY_WebSocket Game Actions|WebSocket Game Actions]]
- [[_COMMUNITY_Dashboard Server|Dashboard Server]]
- [[_COMMUNITY_Web3 Contracts & Gas|Web3 Contracts & Gas]]
- [[_COMMUNITY_Setup Concepts & Wallet Types|Setup Concepts & Wallet Types]]
- [[_COMMUNITY_Dashboard Frontend (app.js)|Dashboard Frontend (app.js)]]
- [[_COMMUNITY_Project Config & Infrastructure|Project Config & Infrastructure]]
- [[_COMMUNITY_Agent Config & Logging|Agent Config & Logging]]
- [[_COMMUNITY_Dashboard State Management|Dashboard State Management]]
- [[_COMMUNITY_Railway Sync|Railway Sync]]
- [[_COMMUNITY_Module Entry Points (Core)|Module Entry Points (Core)]]
- [[_COMMUNITY_Wallet & Whitelist Setup|Wallet & Whitelist Setup]]
- [[_COMMUNITY_Runtime Modes|Runtime Modes]]
- [[_COMMUNITY_Rate Limiter|Rate Limiter]]
- [[_COMMUNITY_Version Check|Version Check]]
- [[_COMMUNITY_Core Module Files|Core Module Files]]
- [[_COMMUNITY_EIP-712 Signer|EIP-712 Signer]]
- [[_COMMUNITY_Identity Setup|Identity Setup]]
- [[_COMMUNITY_Paid Game Join|Paid Game Join]]
- [[_COMMUNITY_Package bot|Package: bot]]
- [[_COMMUNITY_Package web3.contracts|Package: web3.contracts]]
- [[_COMMUNITY_Package dashboard|Package: dashboard]]
- [[_COMMUNITY_Package game|Package: game]]
- [[_COMMUNITY_Package memory|Package: memory]]
- [[_COMMUNITY_Package setup|Package: setup]]
- [[_COMMUNITY_Package strategy|Package: strategy]]
- [[_COMMUNITY_Package utils|Package: utils]]
- [[_COMMUNITY_Package web3|Package: web3]]
- [[_COMMUNITY_API Client Module|API Client Module]]
- [[_COMMUNITY_State Router Module|State Router Module]]
- [[_COMMUNITY_Dashboard State Module|Dashboard State Module]]
- [[_COMMUNITY_Action Sender Module|Action Sender Module]]
- [[_COMMUNITY_Free Join Module|Free Join Module]]
- [[_COMMUNITY_Paid Join Module|Paid Join Module]]
- [[_COMMUNITY_Room Selector Module|Room Selector Module]]
- [[_COMMUNITY_Settlement Module|Settlement Module]]
- [[_COMMUNITY_WebSocket Engine Module|WebSocket Engine Module]]
- [[_COMMUNITY_Agent Memory Module|Agent Memory Module]]
- [[_COMMUNITY_Account Setup Module|Account Setup Module]]
- [[_COMMUNITY_Identity Module|Identity Module]]
- [[_COMMUNITY_Wallet Setup Module|Wallet Setup Module]]
- [[_COMMUNITY_Dashboard JS Bundle|Dashboard JS Bundle]]
- [[_COMMUNITY_Ethers.js|Ethers.js]]
- [[_COMMUNITY_Eth Account|Eth Account]]
- [[_COMMUNITY_Web3.py|Web3.py]]

## God Nodes (most connected - your core abstractions)
1. `MoltyAPI` - 50 edges
2. `APIError` - 31 edges
3. `ActionSender` - 27 edges
4. `Logger Utility` - 26 edges
5. `Agent Instructions Document` - 26 edges
6. `AgentMemory` - 25 edges
7. `brain.py` - 24 edges
8. `Skill` - 23 edges
9. `app.js` - 21 edges
10. `decide_action()` - 20 edges

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

## Communities (48 total, 26 thin omitted)

### Community 0 - "Heartbeat & State Machine"
Cohesion: 0.06
Nodes (40): APIError, Heartbeat, Heartbeat loop — main orchestration per heartbeat.md. State machine: setup → jo, Single heartbeat cycle: check state → route → act., Setup pipeline: wallet → whitelist → identity. Respects config flags., Join a game based on room selection., Resume or start playing an active game.         Per game-loop.md: always connec, Run the WebSocket gameplay engine. (+32 more)

### Community 1 - "API Client & Account Setup"
Cohesion: 0.05
Nodes (39): MoltyAPI, POST /accounts — create account, returns apiKey (shown once!)., GET /accounts/me — readiness check, state detection, balance., PUT /accounts/wallet — attach wallet to existing account., POST /create/wallet — create MoltyRoyale Wallet., POST /whitelist/request — request whitelist approval., POST /api/identity — register ERC-8004 identity., GET /api/identity — check current identity. (+31 more)

### Community 2 - "Combat Strategy AI"
Cohesion: 0.07
Nodes (42): calc_damage(), _check_equip(), _check_pickup(), _choose_move_target(), decide_action(), _estimate_enemy_weapon_bonus(), _find_energy_drink(), _find_healing_item() (+34 more)

### Community 3 - "Game Reference Documentation"
Cohesion: 0.09
Nodes (42): Action Payload Reference, Agent Memory & Growth, API Summary, MoltyAPI, Combat & Items Spec Sheet, CROSS, Moltz, Agent EOA (+34 more)

### Community 4 - "WebSocket Game Actions"
Cohesion: 0.08
Nodes (18): ActionSender, Tracks cooldown state and builds action envelopes., Update state from action_result payload.         Per actions.md: canAct and coo, Update state from can_act_changed server push., Can we send a Group 1 (cooldown) action?, Build action envelope per actions.md spec.         Truncates thought fields to, Per actions.md: requires megaphone item or broadcast_station facility., Process a single WebSocket message. Returns game result or None. (+10 more)

### Community 5 - "Dashboard Server"
Cohesion: 0.07
Nodes (31): api_accounts(), api_accounts_post(), api_export(), api_import(), api_state(), create_app(), index_handler(), _push_loop() (+23 more)

### Community 6 - "Web3 Contracts & Gas"
Cohesion: 0.1
Nodes (29): Web3 Contracts Module, Gas Checker Module, Web3 Provider Module, ensure_whitelist(), Request whitelist + auto-approve if advanced mode.     Returns True if whitelis, check_cross_balance(), gas_checker.py, Gas fee checker — check CROSS balance before any on-chain transaction. If insuf (+21 more)

### Community 7 - "Setup Concepts & Wallet Types"
Cohesion: 0.14
Nodes (27): Agent EOA, CROSS (native token), EIP-712 Signing, ERC-8004 Identity, Legacy WalletFactory, Legacy Wallet Withdraw, MoltyRoyale Wallet (SC Wallet), MoltyRoyaleWallet Contract (+19 more)

### Community 8 - "Dashboard Frontend (app.js)"
Cohesion: 0.19
Nodes (19): app.js, $(), animateNum(), esc(), fmt(), itemName(), itemTag(), _logLine() (+11 more)

### Community 9 - "Project Config & Infrastructure"
Cohesion: 0.12
Nodes (16): Agent Instructions Document, Project Readme Document, Dashboard Index HTML, Setup Package Init, Strategy Package Init, Utils Package Init, Railway Sync Utility, Version Check Utility (+8 more)

### Community 10 - "Agent Config & Logging"
Cohesion: 0.22
Nodes (12): _filter_agents(), load_agents(), Configuration & constants for Molty Royale AI Agent. All env vars loaded here., Filter agents by AGENT_NAMES env var (comma-separated list of agent names)., Warn if multiple agents share the same SC wallet., Select only 1 agent per SC wallet (molty_royale_wallet).     If multiple agents, Load agent configs from AGENTS_JSON env var, fallback to credentials.json., _select_primary_per_wallet() (+4 more)

### Community 11 - "Dashboard State Management"
Cohesion: 0.15
Nodes (7): DashboardState, state.py, Dashboard shared state — bridge between bot engine and web dashboard. Bot write, Singleton shared state between bot and dashboard., Update agent state from bot engine., Add or update account., Full state snapshot for dashboard API.

### Community 12 - "Railway Sync"
Cohesion: 0.26
Nodes (12): _collection_upsert(), _get_railway_config(), is_railway(), is_setup_complete(), railway_sync.py, Railway Variables auto-sync. After account creation, saves API_KEY + private ke, ONE-TIME sync of ALL variables to Railway after first-run.     Combines config, Check if running on Railway. (+4 more)

### Community 13 - "Module Entry Points (Core)"
Cohesion: 0.22
Nodes (8): State router — determines agent state from GET /accounts/me response. Routes pe, Logger Utility, action_sender.py, Action envelope builder + cooldown state tracker. Builds action messages per ac, room_selector.py, Room selector — choose free or paid room based on readiness and config. room_mo, agent_memory.py, Agent memory — persistent cross-game learning via molty-royale-context.json. Tw

### Community 14 - "Wallet & Whitelist Setup"
Cohesion: 0.25
Nodes (9): Whitelist Contract Module, ensure_molty_wallet(), wallet_setup.py, MoltyRoyale Wallet (SC Wallet) setup — POST /create/wallet. Handles CONFLICT, W, Create or recover MoltyRoyale Wallet. Returns wallet address or "".     Per set, Try to recover wallet address on-chain via WalletFactory.getWallets()., _recover_wallet_address(), whitelist.py (+1 more)

### Community 15 - "Runtime Modes"
Cohesion: 0.25
Nodes (9): Autonomous WebSocket Runner Mode, Cost Guidance, Heartbeat Mode, Runtime Modes Document, action messages, agent_view, heartbeat.md, ws/agent (+1 more)

### Community 16 - "Rate Limiter"
Cohesion: 0.29
Nodes (5): rate_limiter.py, RateLimiter, Token-bucket rate limiter for REST (300/min) and WebSocket (120/min). Non-block, Async token-bucket rate limiter., Wait until tokens are available. Non-blocking via asyncio.sleep.

### Community 17 - "Version Check"
Cohesion: 0.33
Nodes (6): check_version(), get_version_header(), version_check.py, Version check — GET /api/version and X-Version header management. Returns 426 V, Fetch current server version. Returns version string., Return X-Version header dict.

### Community 18 - "Core Module Files"
Cohesion: 0.33
Nodes (5): Async REST API client for Molty Royale. All endpoints from api-summary.md with, Strategy Brain Module, Rate Limiter Utility, websocket_engine.py, WebSocket gameplay engine — wss://cdn.moltyroyale.com/ws/agent. Core loop: conn

### Community 19 - "EIP-712 Signer"
Cohesion: 0.5
Nodes (4): eip712_signer.py, EIP-712 typed data signing for paid room join. Signs JoinTournament typed data, Sign EIP-712 typed data for paid room join.     eip712_data comes from GET /gam, sign_join_paid()

### Community 20 - "Identity Setup"
Cohesion: 0.67
Nodes (3): Identity Contract Module, identity.py, ERC-8004 Identity registration — on-chain register() + POST /api/identity. Neve

### Community 21 - "Paid Game Join"
Cohesion: 0.67
Nodes (3): EIP-712 Signer Module, paid_join.py, Paid game join — EIP-712 sign → POST /games/{id}/join-paid. Per paid-games.md:

## Knowledge Gaps
- **168 isolated node(s):** `Async REST API client for Molty Royale. All endpoints from api-summary.md with`, `Async HTTP client for all Molty Royale REST endpoints.`, `Parse JSON safely, handling malformed/concatenated responses.`, `Rate-limited request with error handling.`, `POST /accounts — create account, returns apiKey (shown once!).` (+163 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Logger Utility` connect `Module Entry Points (Core)` to `Heartbeat & State Machine`, `API Client & Account Setup`, `Combat Strategy AI`, `Dashboard Server`, `Web3 Contracts & Gas`, `Project Config & Infrastructure`, `Dashboard State Management`, `Railway Sync`, `Wallet & Whitelist Setup`, `Version Check`, `Core Module Files`, `EIP-712 Signer`, `Identity Setup`, `Paid Game Join`?**
  _High betweenness centrality (0.342) - this node is a cross-community bridge._
- **Why does `Heartbeat` connect `Heartbeat & State Machine` to `API Client & Account Setup`, `Game Reference Documentation`, `Dashboard Server`, `Wallet & Whitelist Setup`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Why does `MoltyAPI` connect `API Client & Account Setup` to `Heartbeat & State Machine`, `Web3 Contracts & Gas`, `Wallet & Whitelist Setup`, `Core Module Files`, `Identity Setup`, `Paid Game Join`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Are the 28 inferred relationships involving `MoltyAPI` (e.g. with `Heartbeat` and `Heartbeat loop — main orchestration per heartbeat.md. State machine: setup → jo`) actually correct?**
  _`MoltyAPI` has 28 INFERRED edges - model-reasoned connections that need verification._
- **Are the 26 inferred relationships involving `APIError` (e.g. with `Heartbeat` and `Heartbeat loop — main orchestration per heartbeat.md. State machine: setup → jo`) actually correct?**
  _`APIError` has 26 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `ActionSender` (e.g. with `WebSocketEngine` and `WebSocket gameplay engine — wss://cdn.moltyroyale.com/ws/agent. Core loop: conn`) actually correct?**
  _`ActionSender` has 10 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Async REST API client for Molty Royale. All endpoints from api-summary.md with`, `Async HTTP client for all Molty Royale REST endpoints.`, `Parse JSON safely, handling malformed/concatenated responses.` to the rest of the system?**
  _168 weakly-connected nodes found - possible documentation gaps or missing edges._