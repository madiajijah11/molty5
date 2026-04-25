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

> **PENTING: Urutan yang benar adalah SEBELUM deploy, baru set secrets!** Jika deploy dulu baru set secrets, bot akan generate ulang credentials.

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

### Step 3: Launch App (TAPI JANGAN deploy dulu!)
```bash
fly launch --name molty5 --region iad --no-deploy --yes
# Atau interactive:
fly launch
# - App name: molty5
# - Region: closest to you
# - Deploy now: No  <-- PENTING!
```

### Step 4: Set Secrets DULU (sebelum deploy!)
```bash
fly secrets set AGENT_NAME=YourBotName ROOM_MODE=free ADVANCED_MODE=true LOG_LEVEL=INFO
```

### Step 5: Baru Deploy
```bash
fly deploy
```

### Step 6: Akses Credentials (setelah Bot Jalan)

SETELAH bot running, cek logs untuk lihat credentials yang di-generate:
```bash
fly logs
```

Atau akses langsung dari VM:
```bash
# List semua file
fly machine exec <machine-id> "ls -la /app/dev-agent/"

# Get credentials.json (bisa lihat API_KEY, agent_wallet_address, dll)
fly machine exec <machine-id> "cat /app/dev-agent/credentials.json"

# Get wallet (bisa lihat PRIVATE KEY!)
fly machine exec <machine-id> "cat /app/dev-agent/agent-wallet.json"
fly machine exec <machine-id> "cat /app/dev-agent/owner-wallet.json"
```

Contoh output credentials.json:
```json
{
  "api_key": "mr_live_xxxx",
  "agent_name": "MexL",
  "agent_wallet_address": "0x...",
  "owner_eoa": "0x...",
  "erc8004_token_id": 12345
}
```

Contoh output agent-wallet.json:
```json
{
  "address": "0x...",
  "privateKey": "0x..."  // <-- Ini yang dibutuhkan untuk import ke MetaMask!
}
```

### Step 7: akses Dashboard
```bash
fly open
```

Atau langsung ke: https://molty5.fly.dev/

### Common Commands
```bash
fly logs              # View logs
fly status           # Check VM status
fly machine list     # List semua machine
fly restart         # Restart semua machine
fly scale count 1   # Pastikan 1 VM berjalan
```

### ⚠️ Bedanya Railway vs Fly.io

| Aspek | Railway | Fly.io |
|-------|--------|-------|
| Auto-sync credentials | ✅ Ya (GraphQL API) | ❌ Tidak |
| Credentials tersimpan | Railway Variables | VM filesystem (`/app/dev-agent/`) |
| Lihat credentials | Dashboard → Variables | `fly machine exec` + `cat` |
| Persistence | Lewat cloud | Lewat VM volume |

> **Karena Fly.io tidak auto-sync seperti Railway**, credentials tersimpan di dalam VM (`/app/dev-agent/`). Setiap kali deploy ulang, credentials akan di-generate ulang!

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
