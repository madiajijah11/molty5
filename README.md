# Molty Royale AI Agent Bot

Autonomous AI agent for Molty Royale — handles account creation, identity registration, gameplay, and cross-game learning. Features a real-time web dashboard for live monitoring.

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Copy env template
cp .env.example .env

# 3. Run the bot (first run = interactive setup)
python -m bot.main
```

## 📊 Command Center Dashboard

The bot comes with a built-in real-time web dashboard!

When running locally, open: **http://localhost:8080**
When running on Fly.io or Railway, open the provided domain link.

**Features:**
- **Live Metrics**: Agents, Playing, Dead, Moltz, sMoltz, CROSS
- **Agent Overview**: Real-time status, HP/EP bars, Inventory, Enemies
- **Live Logs**: Real-time streaming log panel that auto-updates
- **Coming Soon**: Multi-account management, export/import, data analytics

## 🛠️ Configuration

| Env Variable | Default | Description |
|---|---|---|
| `ROOM_MODE` | `free` | `free` (default) / `auto` / `paid` |
| `ADVANCED_MODE` | `true` | Auto-manage Owner EOA & whitelist |
| `LOG_LEVEL` | `INFO` | `DEBUG` / `INFO` / `WARNING` |
| `WEB_PORT` | `8080` | Port for the web dashboard |

## 🐳 Docker

```bash
docker build -t molty-bot .
docker run --env-file .env -p 8080:8080 -it molty-bot
```

## ✈️ Fly.io Deployment (Recommended - Free Tier)

> **Fly.io handles persistence differently than Railway.** The VM persists across restarts, so credentials are saved automatically in `/app/dev-agent/`. No need for manual token sync.

### Step 1: Install Fly CLI
```bash
# macOS
brew install flyctl

# Windows (PowerShell)
iwr https://fly.io/install.ps1 -useb | iex

# Linux
curl -L https://fly.io/install.sh | sh
```

### Step 2: Login
```bash
fly auth login
```

### Step 3: Launch App (creates fly.toml + volume)
```bash
fly launch
# When asked:
# - App name: molty-bot
# - Region: choose closest to you
# - Deploy now: No (we'll configure first)
```

The `fly.toml` in this repo already configures a persistent volume at `/root/.molty-royale` for cross-game memory.

### Step 4: Set Secrets
```bash
fly secrets set AGENT_NAME=YourBotName
fly secrets set ROOM_MODE=free
fly secrets set ADVANCED_MODE=true
fly secrets set LOG_LEVEL=INFO
```

### Step 5: Deploy
```bash
fly deploy
```

### Step 6: Access Dashboard
```bash
fly open
```

### Common Commands
```bash
fly logs              # View logs
fly status           # Check VM status
fly restart          # Restart the app
fly scale count 1    # Ensure 1 VM running
```

### Managing Secrets

**View all secrets:**
```bash
fly secrets list
```

**View specific secret:**
```bash
fly secret show AGENT_NAME
```

**Update secret:**
```bash
fly secrets set AGENT_NAME=NewBotName
```

**Access credentials from VM:**
```bash
fly ssh cat /app/dev-agent/credentials.json
fly ssh cat /app/dev-agent/agent-wallet.json
```

**Dashboard:** https://fly.io/dashboard → Select app → Secrets tab

### First-Run Behavior
On first deploy, the bot will:
1. Generate wallets & API key
2. Save credentials to `/app/dev-agent/`
3. Since Fly.io VMs persist, credentials survive restarts!

> **No RAILWAY_API_TOKEN needed** — Fly.io doesn't support Railway's GraphQL API. Credentials persist via the VM itself.

## 🎨 Render Deployment

### Step 1: Daftar
Buka https://render.com → Sign Up dengan GitHub

### Step 2: Connect Repo
1. Dashboard → New → Web Service
2. Pilih repo `molty5`
3. Branch: `main`

### Step 3: Configure
| Field | Value |
|-------|-------|
| Name | `molty5` |
| Environment | `Python 3` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python -m bot.main` |

### Step 4: Environment Variables
Tambah di dashboard:

| Key | Value |
|-----|-------|
| `AGENT_NAME` | `MexL` |
| `ROOM_MODE` | `free` |
| `ADVANCED_MODE` | `true` |
| `LOG_LEVEL` | `INFO` |

### Step 5: Deploy
Klik **Create Web Service**

> **Note**: Render free tier tidur setelah 15 menit tidak aktif. Upgrade ke $5/bln Biar jalan terus 24/7.

## 🚂 Railway Deployment

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

Go to your service → **Variables** tab → add these:

**Required (You fill these):**
| Variable | Value | Description |
|---|---|---|
| `AGENT_NAME` | `YourBotName` | Agent name (max 50 chars) |
| `ADVANCED_MODE` | `true` | Bot auto-generates Owner EOA |
| `ROOM_MODE` | `free` | `free` / `auto` / `paid` |
| `LOG_LEVEL` | `INFO` | Logging level |
| `RAILWAY_API_TOKEN` | *(see below)* | Required to auto-save credentials |

**Auto-generated (DO NOT FILL):**
| Variable | Description |
|---|---|
| `API_KEY` | Auto-filled after POST /accounts |
| `AGENT_WALLET_ADDRESS` | Auto-generated Agent EOA |
| `AGENT_PRIVATE_KEY` | Auto-generated Agent private key |
| `OWNER_EOA` | Auto-generated Owner EOA |
| `OWNER_PRIVATE_KEY` | Auto-generated Owner private key |

### Step 4: Create RAILWAY_API_TOKEN
1. Go to [railway.com/account/tokens](https://railway.com/account/tokens)
2. Create new token → copy
3. Add as `RAILWAY_API_TOKEN` in Variables

> *Why?* The bot uses this token to automatically save its generated API Keys and wallets directly into your Railway environment variables. This ensures persistence across redeploys without needing external databases.

## 🏗️ Architecture

```
bot/
├── main.py           # Entry point
├── heartbeat.py      # Main loop (state machine)
├── dashboard/        # Command Center Web UI
├── setup/            # Account + wallet + whitelist + identity
├── game/             # WebSocket engine + game strategy
├── strategy/         # Combat AI + movement + guardian farming
├── web3/             # EIP-712, contracts, wallet management
├── memory/           # Cross-game learning
└── utils/            # Logger, rate limiter, Railway sync
```
