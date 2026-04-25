# AGENTS.md

## Run

```bash
python -m bot.main
```

Dashboard + bot run concurrently. Dashboard available at http://localhost:8080 (platforms inject `PORT` env var automatically).

## No tests, lint, or typecheck

There are no test files, no `pyproject.toml`, no `setup.py`, and no configured linters or type checkers. Verify changes by running the bot locally.

## Dependencies

```bash
pip install -r requirements.txt
```

Requirements: `websockets`, `httpx`, `web3`, `eth-account`, `python-dotenv`, `aiofiles`, `aiohttp`.

## Env config

Copy `.env.example` to `.env`. Required variables:
- `AGENT_NAME` — bot name (max 50 chars)
- `ROOM_MODE` — `free` (default) / `auto` / `paid`
- `ADVANCED_MODE` — `true` to auto-generate Owner EOA + Agent wallet
- `RAILWAY_API_TOKEN` — only needed on Railway for auto-persist credentials

Auto-generated (bot fills these after first run): `API_KEY`, `AGENT_WALLET_ADDRESS`, `AGENT_PRIVATE_KEY`, `OWNER_EOA`, `OWNER_PRIVATE_KEY`.

## Architecture

```
bot/
├── main.py           # Entry point (python -m bot.main)
├── heartbeat.py      # Main loop / state machine
├── dashboard/        # Web dashboard (port 8080)
├── setup/            # Account + wallet + whitelist + identity
├── game/             # WebSocket engine + game strategy
├── strategy/         # Combat AI + movement + guardian farming
├── web3/             # EIP-712, contracts, wallet management
├── memory/           # Cross-game learning
└── utils/            # Logger, rate limiter, Railway sync
```

## Docker

```bash
docker build -t molty-bot .
docker run --env-file .env -p 8080:8080 -it molty-bot
```

Docker Compose mounts `molty-memory` volume for persistence at `/root/.molty-royale` and `./dev-agent:/app/dev-agent`.

## Deployment

### Fly.io (Recommended - Free Tier)

1. Install CLI: `brew install flyctl` (macOS) or `iwr https://fly.io/install.ps1 -useb | iex` (Windows)
2. `fly auth login`
3. `fly launch` — choose app name, region, select "Deploy now: No"
4. Create volume: `fly volumes create molty_memory --size 1`
5. Set secrets: `fly secrets set AGENT_NAME=xxx ROOM_MODE=free ADVANCED_MODE=true`
6. `fly deploy`

Credentials persist via VM files (`/app/dev-agent/`), no API token needed.

### Railway

`railway.toml` build from `Dockerfile`, start command `python -m bot.main`. Bot auto-syncs credentials via `RAILWAY_API_TOKEN`.

## Windows

`main.py` sets `asyncio.WindowsSelectorEventLoopPolicy()` on Windows. No other platform quirks.

## Gitignore

Excluded: `.env`, `dev-agent/`, `log/`, `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `*.egg-info/`, `dist/`, `build/`, `*.rar`, `logs.*.json`