# Graph Report - F:\Website\molty5  (2026-05-01)

## Corpus Check
- Corpus is ~42,413 words - fits in a single context window. You may not need a graph.

## Summary
- 493 nodes · 774 edges · 34 communities detected
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 130 edges (avg confidence: 0.61)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Core Game Loop|Core Game Loop]]
- [[_COMMUNITY_API & Wallet Management|API & Wallet Management]]
- [[_COMMUNITY_Config & Documentation|Config & Documentation]]
- [[_COMMUNITY_Combat Strategy AI|Combat Strategy AI]]
- [[_COMMUNITY_Game Concepts & Systems|Game Concepts & Systems]]
- [[_COMMUNITY_Action & WebSocket Engine|Action & WebSocket Engine]]
- [[_COMMUNITY_Web3 & Smart Contracts|Web3 & Smart Contracts]]
- [[_COMMUNITY_Setup & Configuration|Setup & Configuration]]
- [[_COMMUNITY_Dashboard Frontend|Dashboard Frontend]]
- [[_COMMUNITY_Config & Logging|Config & Logging]]
- [[_COMMUNITY_Dashboard State|Dashboard State]]
- [[_COMMUNITY_Railway Deployment|Railway Deployment]]
- [[_COMMUNITY_Runtime Modes|Runtime Modes]]
- [[_COMMUNITY_Rate Limiting|Rate Limiting]]
- [[_COMMUNITY_Bot Initialization|Bot Initialization]]
- [[_COMMUNITY_Web3 Contracts Init|Web3 Contracts Init]]
- [[_COMMUNITY_Dashboard Init|Dashboard Init]]
- [[_COMMUNITY_Dashboard State Module|Dashboard State Module]]
- [[_COMMUNITY_Action Sender Module|Action Sender Module]]
- [[_COMMUNITY_Free Join Module|Free Join Module]]
- [[_COMMUNITY_Paid Join Module|Paid Join Module]]
- [[_COMMUNITY_Room Selector|Room Selector]]
- [[_COMMUNITY_Settlement Module|Settlement Module]]
- [[_COMMUNITY_WebSocket Engine|WebSocket Engine]]
- [[_COMMUNITY_Agent Memory|Agent Memory]]
- [[_COMMUNITY_Account Setup|Account Setup]]
- [[_COMMUNITY_Identity Setup|Identity Setup]]
- [[_COMMUNITY_Wallet Setup|Wallet Setup]]
- [[_COMMUNITY_Dashboard App JS|Dashboard App JS]]
- [[_COMMUNITY_Ethers JS|Ethers JS]]
- [[_COMMUNITY_Eth Account Setup|Eth Account Setup]]
- [[_COMMUNITY_Web3 Python|Web3 Python]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]

## God Nodes (most connected - your core abstractions)
1. `MoltyAPI` - 50 edges
2. `APIError` - 31 edges
3. `ActionSender` - 27 edges
4. `Logger Utility` - 26 edges
5. `Agent Instructions Document` - 26 edges
6. `AgentMemory` - 25 edges
7. `Skill` - 23 edges
8. `decide_action()` - 20 edges
9. `WebSocketEngine` - 19 edges
10. `Setup Guide Document` - 19 edges

## Surprising Connections (you probably didn't know these)
- `Agent Instructions Document` --references--> `Whitelist Setup Module`  [EXTRACTED]
  AGENTS.md → bot/setup/whitelist.py
- `Agent Instructions Document` --references--> `Gas Checker Module`  [EXTRACTED]
  AGENTS.md → bot/web3/gas_checker.py
- `Agent Instructions Document` --references--> `Wallet Manager Module`  [EXTRACTED]
  AGENTS.md → bot/web3/wallet_manager.py
- `WebSocket gameplay engine — wss://cdn.moltyroyale.com/ws/agent. Core loop: conn` --uses--> `ActionSender`  [INFERRED]
  game\websocket_engine.py → game\action_sender.py
- `Manages the gameplay WebSocket session.` --uses--> `ActionSender`  [INFERRED]
  game\websocket_engine.py → game\action_sender.py

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

## Communities

### Community 0 - "Core Game Loop"
Cohesion: 0.06
Nodes (38): APIError, Heartbeat, Heartbeat loop — main orchestration per heartbeat.md. State machine: setup → jo, Single heartbeat cycle: check state → route → act., Setup pipeline: wallet → whitelist → identity. Respects config flags., Join a game based on room selection., Resume or start playing an active game.         Per game-loop.md: always connec, Run the WebSocket gameplay engine. (+30 more)

### Community 1 - "API & Wallet Management"
Cohesion: 0.05
Nodes (37): MoltyAPI, POST /accounts — create account, returns apiKey (shown once!)., GET /accounts/me — readiness check, state detection, balance., PUT /accounts/wallet — attach wallet to existing account., POST /create/wallet — create MoltyRoyale Wallet., POST /whitelist/request — request whitelist approval., POST /api/identity — register ERC-8004 identity., GET /api/identity — check current identity. (+29 more)

### Community 2 - "Config & Documentation"
Cohesion: 0.04
Nodes (44): Agent Instructions Document, Project Readme Document, Async REST API client for Molty Royale. All endpoints from api-summary.md with, Dashboard Index HTML, Setup Package Init, State router — determines agent state from GET /accounts/me response. Routes pe, Strategy Brain Module, Strategy Package Init (+36 more)

### Community 3 - "Combat Strategy AI"
Cohesion: 0.07
Nodes (41): calc_damage(), _check_equip(), _check_pickup(), _choose_move_target(), decide_action(), _estimate_enemy_weapon_bonus(), _find_energy_drink(), _find_healing_item() (+33 more)

### Community 4 - "Game Concepts & Systems"
Cohesion: 0.09
Nodes (42): Action Payload Reference, Agent Memory & Growth, API Summary, MoltyAPI, Combat & Items Spec Sheet, CROSS, Moltz, Agent EOA (+34 more)

### Community 5 - "Action & WebSocket Engine"
Cohesion: 0.08
Nodes (18): ActionSender, Tracks cooldown state and builds action envelopes., Update state from action_result payload.         Per actions.md: canAct and coo, Update state from can_act_changed server push., Can we send a Group 1 (cooldown) action?, Build action envelope per actions.md spec.         Truncates thought fields to, Per actions.md: requires megaphone item or broadcast_station facility., Process a single WebSocket message. Returns game result or None. (+10 more)

### Community 6 - "Web3 & Smart Contracts"
Cohesion: 0.07
Nodes (30): api_accounts(), api_accounts_post(), api_export(), api_import(), api_state(), create_app(), index_handler(), _push_loop() (+22 more)

### Community 7 - "Setup & Configuration"
Cohesion: 0.1
Nodes (25): Web3 Contracts Module, Gas Checker Module, Web3 Provider Module, ensure_whitelist(), Request whitelist + auto-approve if advanced mode.     Returns True if whitelis, check_cross_balance(), Gas fee checker — check CROSS balance before any on-chain transaction. If insuf, Check if address has enough CROSS for gas.     Returns (has_enough, balance_wei (+17 more)

### Community 8 - "Dashboard Frontend"
Cohesion: 0.14
Nodes (27): Agent EOA, CROSS (native token), EIP-712 Signing, ERC-8004 Identity, Legacy WalletFactory, Legacy Wallet Withdraw, MoltyRoyale Wallet (SC Wallet), MoltyRoyaleWallet Contract (+19 more)

### Community 9 - "Config & Logging"
Cohesion: 0.19
Nodes (18): $(), animateNum(), esc(), fmt(), itemName(), itemTag(), _logLine(), patchAgentCard() (+10 more)

### Community 10 - "Dashboard State"
Cohesion: 0.22
Nodes (11): _filter_agents(), load_agents(), Configuration & constants for Molty Royale AI Agent. All env vars loaded here., Filter agents by AGENT_NAMES env var (comma-separated list of agent names)., Warn if multiple agents share the same SC wallet., Select only 1 agent per SC wallet (molty_royale_wallet).     If multiple agents, Load agent configs from AGENTS_JSON env var, fallback to credentials.json., _select_primary_per_wallet() (+3 more)

### Community 11 - "Railway Deployment"
Cohesion: 0.15
Nodes (6): DashboardState, Dashboard shared state — bridge between bot engine and web dashboard. Bot write, Singleton shared state between bot and dashboard., Update agent state from bot engine., Add or update account., Full state snapshot for dashboard API.

### Community 12 - "Runtime Modes"
Cohesion: 0.26
Nodes (11): _collection_upsert(), _get_railway_config(), is_railway(), is_setup_complete(), Railway Variables auto-sync. After account creation, saves API_KEY + private ke, ONE-TIME sync of ALL variables to Railway after first-run.     Combines config, Check if running on Railway., Check if first-run sync was already done (prevents redeploy loop). (+3 more)

### Community 13 - "Rate Limiting"
Cohesion: 0.25
Nodes (9): Autonomous WebSocket Runner Mode, Cost Guidance, Heartbeat Mode, Runtime Modes Document, action messages, agent_view, heartbeat.md, ws/agent (+1 more)

### Community 14 - "Bot Initialization"
Cohesion: 0.29
Nodes (4): RateLimiter, Token-bucket rate limiter for REST (300/min) and WebSocket (120/min). Non-block, Async token-bucket rate limiter., Wait until tokens are available. Non-blocking via asyncio.sleep.

### Community 15 - "Web3 Contracts Init"
Cohesion: 1.0
Nodes (1): Molty Royale AI Agent Bot

### Community 16 - "Dashboard Init"
Cohesion: 1.0
Nodes (1): Contract ABIs and helpers for on-chain interactions. All addresses from contrac

### Community 24 - "Dashboard State Module"
Cohesion: 1.0
Nodes (1): bot/api_client.py

### Community 25 - "Action Sender Module"
Cohesion: 1.0
Nodes (1): bot/state_router.py

### Community 26 - "Free Join Module"
Cohesion: 1.0
Nodes (1): bot/dashboard/state.py

### Community 27 - "Paid Join Module"
Cohesion: 1.0
Nodes (1): bot/game/action_sender.py

### Community 28 - "Room Selector"
Cohesion: 1.0
Nodes (1): bot/game/free_join.py

### Community 29 - "Settlement Module"
Cohesion: 1.0
Nodes (1): bot/game/paid_join.py

### Community 30 - "WebSocket Engine"
Cohesion: 1.0
Nodes (1): bot/game/room_selector.py

### Community 31 - "Agent Memory"
Cohesion: 1.0
Nodes (1): bot/game/settlement.py

### Community 32 - "Account Setup"
Cohesion: 1.0
Nodes (1): bot/game/websocket_engine.py

### Community 33 - "Identity Setup"
Cohesion: 1.0
Nodes (1): bot/memory/agent_memory.py

### Community 34 - "Wallet Setup"
Cohesion: 1.0
Nodes (1): bot/setup/account_setup.py

### Community 35 - "Dashboard App JS"
Cohesion: 1.0
Nodes (1): bot/setup/identity.py

### Community 36 - "Ethers JS"
Cohesion: 1.0
Nodes (1): bot/setup/wallet_setup.py

### Community 37 - "Eth Account Setup"
Cohesion: 1.0
Nodes (1): bot/dashboard/static/app.js

### Community 38 - "Web3 Python"
Cohesion: 1.0
Nodes (1): ethers.js

### Community 39 - "Community 39"
Cohesion: 1.0
Nodes (1): eth_account (Python)

### Community 40 - "Community 40"
Cohesion: 1.0
Nodes (1): web3.py

## Knowledge Gaps
- **160 isolated node(s):** `Async REST API client for Molty Royale. All endpoints from api-summary.md with`, `Async HTTP client for all Molty Royale REST endpoints.`, `Parse JSON safely, handling malformed/concatenated responses.`, `Rate-limited request with error handling.`, `POST /accounts — create account, returns apiKey (shown once!).` (+155 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Web3 Contracts Init`** (2 nodes): `Molty Royale AI Agent Bot`, `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Dashboard Init`** (2 nodes): `contracts.py`, `Contract ABIs and helpers for on-chain interactions. All addresses from contrac`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Dashboard State Module`** (1 nodes): `bot/api_client.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Action Sender Module`** (1 nodes): `bot/state_router.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Free Join Module`** (1 nodes): `bot/dashboard/state.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Paid Join Module`** (1 nodes): `bot/game/action_sender.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Room Selector`** (1 nodes): `bot/game/free_join.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Settlement Module`** (1 nodes): `bot/game/paid_join.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `WebSocket Engine`** (1 nodes): `bot/game/room_selector.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Agent Memory`** (1 nodes): `bot/game/settlement.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Account Setup`** (1 nodes): `bot/game/websocket_engine.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Identity Setup`** (1 nodes): `bot/memory/agent_memory.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Wallet Setup`** (1 nodes): `bot/setup/account_setup.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Dashboard App JS`** (1 nodes): `bot/setup/identity.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Ethers JS`** (1 nodes): `bot/setup/wallet_setup.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Eth Account Setup`** (1 nodes): `bot/dashboard/static/app.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Web3 Python`** (1 nodes): `ethers.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `eth_account (Python)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `web3.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Logger Utility` connect `Config & Documentation` to `Core Game Loop`, `API & Wallet Management`, `Combat Strategy AI`, `Web3 & Smart Contracts`, `Setup & Configuration`, `Railway Deployment`, `Runtime Modes`?**
  _High betweenness centrality (0.342) - this node is a cross-community bridge._
- **Why does `Heartbeat` connect `Core Game Loop` to `API & Wallet Management`, `Config & Documentation`, `Game Concepts & Systems`, `Web3 & Smart Contracts`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Why does `MoltyAPI` connect `API & Wallet Management` to `Core Game Loop`, `Config & Documentation`, `Setup & Configuration`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Are the 28 inferred relationships involving `MoltyAPI` (e.g. with `Heartbeat` and `Heartbeat loop — main orchestration per heartbeat.md. State machine: setup → jo`) actually correct?**
  _`MoltyAPI` has 28 INFERRED edges - model-reasoned connections that need verification._
- **Are the 26 inferred relationships involving `APIError` (e.g. with `Heartbeat` and `Heartbeat loop — main orchestration per heartbeat.md. State machine: setup → jo`) actually correct?**
  _`APIError` has 26 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `ActionSender` (e.g. with `WebSocketEngine` and `WebSocket gameplay engine — wss://cdn.moltyroyale.com/ws/agent. Core loop: conn`) actually correct?**
  _`ActionSender` has 10 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Async REST API client for Molty Royale. All endpoints from api-summary.md with`, `Async HTTP client for all Molty Royale REST endpoints.`, `Parse JSON safely, handling malformed/concatenated responses.` to the rest of the system?**
  _160 weakly-connected nodes found - possible documentation gaps or missing edges._