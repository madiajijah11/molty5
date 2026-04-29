# Molty Royale AI Agent Bot

Autonomous AI agent for Molty Royale — handles account creation, identity registration, gameplay, and cross-game learning. Features a real-time web dashboard for live monitoring.

## 🚀 Quick Start

### Single-Agent Mode
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Copy env template
cp .env.example .env

# 3. Run the bot (first run = interactive setup)
python -m bot.main
```

### Multi-Agent Mode (Railway Recommended)
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set AGENTS_JSON environment variable with array of agent configs
# (See .env.example for format)

# 3. Run with multiple agents
python -m bot.main
# Bot will load all agents from AGENTS_JSON and run concurrently
```

## 📊 Command Center Dashboard

The bot comes with a built-in real-time web dashboard!

When running locally, open: **http://localhost:8080**

**Features:**
- **Live Metrics**: Agents, Playing, Dead, Moltz, sMoltz, CROSS
- **Agent Overview**: Real-time status, HP/EP bars, Inventory, Enemies
- **Live Logs**: Real-time streaming log panel that auto-updates
- **Coming Soon**: Multi-account management, export/import, data analytics

## 🛠️ Configuration

| Env Variable | Default | Description |
|---|---|---|
| `HAVE_ACCOUNT` | `""` | `"yes"` = use AGENTS_JSON, `"no"` = create new account |
| `AGENTS_JSON` | `""` | JSON array of agent configs (multi-agent mode) |
| `AGENT_NAMES` | `""` | Filter agents to run (comma-separated, e.g., "MexL,GENZODR") |
| `ADVANCED_MODE` | `true` | Auto-manage Owner EOA & whitelist |
| `LOG_LEVEL` | `INFO` | `DEBUG` / `INFO` / `WARNING` |

## 🚂 Railway Deployment (Recommended)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Molty Royale AI Agent"
git remote add origin https://github.com/YOUR_USER/molty5.git
git push -u origin main
```

### Step 2: Connect in Railway
1. Go to [railway.com](https://railway.com) → New Project → Deploy from GitHub
2. Select your `molty5` repo
3. Go to Settings → Networking → **Generate Domain** (to access the dashboard)

### Step 3: Set Variables in Railway Dashboard

**Multi-Agent Mode (Recommended):**
| Variable | Value | Description |
|---|---|---|
| `HAVE_ACCOUNT` | `yes` | Already have accounts |
| `AGENTS_JSON` | `[{"name":"...",...}]` | JSON array of agent configs (see .env.example) |
| `AGENT_NAMES` | `MexL,GENZODR` | Optional: filter which agents run |
| `LOG_LEVEL` | `INFO` | Logging level |

**Create New Account (Single-Agent):**
| Variable | Value | Description |
|---|---|---|
| `HAVE_ACCOUNT` | `no` | Create new account |
| `AGENT_NAME` | `YourBotName` | Agent name (max 50 chars) |
| `ADVANCED_MODE` | `true` | Bot auto-generates Owner EOA |
| `LOG_LEVEL` | `INFO` | Logging level |

**Optional (for credentials persistence):**
| Variable | Description |
|---|---|
| `RAILWAY_API_TOKEN` | Create at [railway.com/account/tokens](https://railway.com/account/tokens) |

### Step 4: Deploy
Railway will auto-deploy after push, or manually:
```bash
railway deploy
```

### Step 5: Monitor
- Open Railway dashboard → Logs
- Expected output:
```
INFO: Loaded 6 agents from AGENTS_JSON env var
INFO: Filtered to 2 agents: ['MexL', 'GENZODR']
INFO: Starting 2 agent(s)...
INFO: MOLTY ROYALE AI AGENT — STARTING [MexL]
INFO: MOLTY ROYALE AI AGENT — STARTING [GENZODR]
```

## 🏗️ Architecture

```
bot/
├── main.py           # Entry point (multi-agent support)
├── config.py         # Configuration + AGENTS_JSON loader
├── heartbeat.py      # Main loop (per-agent state machine)
├── credentials.py    # Multi-agent credential management
├── dashboard/        # Command Center Web UI (multi-agent)
├── setup/            # Account + wallet + whitelist + identity
├── game/             # WebSocket engine + game strategy
├── strategy/         # Combat AI + movement + guardian farming
├── web3/             # EIP-712, contracts, wallet management
├── memory/           # Cross-game learning
└── utils/            # Logger, rate limiter, Railway sync
```

**Multi-Agent Mode:**
- Set `AGENTS_JSON` env var with array of agent configs
- `main.py` spawns N agents via `asyncio.gather()`
- Each agent runs concurrently (single-thread, asyncio)
- Dashboard displays all agents with individual status
- Filter agents with `AGENT_NAMES` (e.g., "MexL,GENZODR")
- Set `HAVE_ACCOUNT=yes` to use existing accounts, `no` to create new
