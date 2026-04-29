"""
Configuration & constants for Molty Royale AI Agent.
All env vars loaded here. Never hardcode secrets.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ── Skill / API version ──────────────────────────────────────────────
SKILL_VERSION = "1.5.2"

# ── URLs ──────────────────────────────────────────────────────────────
API_BASE = "https://cdn.moltyroyale.com/api"
WS_URL = "wss://cdn.moltyroyale.com/ws/agent"

# ── Chain config (CROSS Mainnet) ──────────────────────────────────────
CROSS_CHAIN_ID = 612055
CROSS_RPC = "https://mainnet.crosstoken.io:22001"

# ── Contract addresses ────────────────────────────────────────────────
IDENTITY_REGISTRY = "0x8004A169FB4a3325136EB29fA0ceB6D2e539a432"
WALLET_FACTORY = "0x378De49F47817D3dF10393851A587e5C2C58EF7C"
WALLET_FACTORY_LEGACY = "0x0713665E4D19fD16e1F09AD77526CC343c6F0223"
MOLTZ_TOKEN = "0xdb99a97d607c5c5831263707E7b746312406ba7E"
ARENA_PAID = "0x8f705417C2a11446e93f94cbe84F476572EE90Ed"
ARENA_FREE = "0xAbC98bBe54e5bc495D97E6A9c51eEf14fd34e77D"
REWARD_VAULT = "0x046a1C632f7e21C215CaF11e1176861567FcB8EE"
FORGE_ROUTER = "0x7aF414e4d373bb332f47769c8d28A446A0C1a1E8"
WCROSS = "0xDdF8AaA3927b8Fd5684dc2edcc7287EcB0A2122d"
REPUTATION_REGISTRY = "0x8004BAa17C55a88189AE136b182e5fdA19dE9b63"

# ── Economy constants (from economy.md) ───────────────────────────────
PAID_ENTRY_FEE_MOLTZ = 500
PAID_ENTRY_FEE_SMOLTZ = 500
FREE_ROOM_POOL = 1000
GUARDIAN_KILL_POOL_SHARE = 0.60  # 60%

# ── Rate limits ───────────────────────────────────────────────────────
REST_RATE_LIMIT = 300   # calls/min per IP
WS_RATE_LIMIT = 120     # messages/min per connection
COOLDOWN_DURATION = 60  # seconds

# ── Credential paths ─────────────────────────────────────────────────
DEV_AGENT_DIR = Path("dev-agent")
CREDENTIALS_FILE = DEV_AGENT_DIR / "credentials.json"
OWNER_INTAKE_FILE = DEV_AGENT_DIR / "owner-intake.json"
AGENT_WALLET_FILE = DEV_AGENT_DIR / "agent-wallet.json"
OWNER_WALLET_FILE = DEV_AGENT_DIR / "owner-wallet.json"
MEMORY_DIR = Path.home() / ".molty-royale"
MEMORY_FILE = MEMORY_DIR / "molty-royale-context.json"

# ── Environment variables ─────────────────────────────────────────────
AGENT_NAME = os.getenv("AGENT_NAME", "")
ADVANCED_MODE = os.getenv("ADVANCED_MODE", "true").lower() == "true"
ROOM_MODE = os.getenv("ROOM_MODE", "free")  # free | auto | paid
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
API_KEY = os.getenv("API_KEY", "")
AGENT_PRIVATE_KEY = os.getenv("AGENT_PRIVATE_KEY", "")
AGENT_WALLET_ADDRESS = os.getenv("AGENT_WALLET_ADDRESS", "")
OWNER_EOA = os.getenv("OWNER_EOA", "")
OWNER_PRIVATE_KEY = os.getenv("OWNER_PRIVATE_KEY", "")

# ── First-Run Intake answers (setup.md lines 29-39) ──────────────────
# These replace the interactive yes/no prompts for Railway/Docker.
# All default to "yes/auto" so zero-config deployment works.
AUTO_WHITELIST = os.getenv("AUTO_WHITELIST", "true").lower() == "true"        # Q4: auto-check + approve
AUTO_SC_WALLET = os.getenv("AUTO_SC_WALLET", "true").lower() == "true"       # Q6: auto-create SC wallet
ENABLE_MEMORY = os.getenv("ENABLE_MEMORY", "true").lower() == "true"         # Q7: cross-game learning
ENABLE_AGENT_TOKEN = os.getenv("ENABLE_AGENT_TOKEN", "false").lower() == "true"  # Q8: agent token
AUTO_IDENTITY = os.getenv("AUTO_IDENTITY", "true").lower() == "true"         # Q9: ERC-8004 auto-register

# ── Account Status Confirmation ─────────────────────────────────
# Set to "yes" if agent already has account (use AGENTS_JSON)
# Set to "no" if agent needs new account (run FIRST-RUN INTAKE)
# If not set, auto-detect based on AGENTS_JSON api_key
HAVE_ACCOUNT = os.getenv("HAVE_ACCOUNT", "").lower()


# ── Multi-Agent Support ──────────────────────────────────────────
def load_agents() -> list:
    """
    Load agent configs from AGENTS_JSON env var, fallback to credentials.json.
    Filters by AGENT_NAMES env var if set (comma-separated list of agent names).
    Returns list of dicts, each with: name, owner_eoa, molty_royale_wallet,
    account_id, api_key, agent_wallet_address, agent_wallet_private_key
    """
    import json
    from bot.utils.logger import get_logger
    log = get_logger(__name__)

    # Try AGENTS_JSON env var first (Railway deployment)
    agents_json = os.getenv("AGENTS_JSON", "")
    if agents_json:
        try:
            agents = json.loads(agents_json)
            if isinstance(agents, list) and len(agents) > 0:
                log.info("Loaded %d agents from AGENTS_JSON env var", len(agents))
                # If only 1 agent in AGENTS_JSON, use it directly (Railway single-agent deploy)
                if len(agents) == 1:
                    log.info("Single agent in AGENTS_JSON, using directly: %s", agents[0].get("name"))
                    return _select_primary_per_wallet(agents, log)
                return _filter_agents(agents)
        except json.JSONDecodeError as e:
            log.error("Failed to parse AGENTS_JSON: %s", e)

    # Fallback to credentials.json (local development)
    if CREDENTIALS_FILE.exists():
        try:
            data = json.loads(CREDENTIALS_FILE.read_text(encoding="utf-8"))
            agents = data.get("agents", [])
            if isinstance(agents, list) and len(agents) > 0:
                log.info("Loaded %d agents from credentials.json", len(agents))
                return _filter_agents(agents)
        except (json.JSONDecodeError, OSError) as e:
            log.error("Failed to read credentials.json: %s", e)

    log.warning("No agents found in AGENTS_JSON or credentials.json")
    return []


def _filter_agents(agents: list) -> list:
    """
    Filter agents by AGENT_NAMES env var (comma-separated list of agent names).
    If AGENT_NAMES is not set or empty, return all agents.
    Handles case-insensitive matching and selects only primary agent per SC wallet
    to avoid NOT_PRIMARY_AGENT errors.
    """
    from bot.utils.logger import get_logger
    log = get_logger(__name__)

    agent_names_filter = os.getenv("AGENT_NAMES", "").strip()
    if not agent_names_filter:
        # No filter - return all agents, but warn about shared SC wallets
        _warn_shared_wallets(agents, log)
        return agents

    # Parse comma-separated list (e.g., "MexL,GENZODR")
    allowed_names = [name.strip() for name in agent_names_filter.split(",") if name.strip()]
    if not allowed_names:
        return agents

    # Case-insensitive matching
    allowed_lower = {name.lower(): name for name in allowed_names}
    filtered = [a for a in agents if a.get("name", "").lower() in allowed_lower]

    if not filtered:
        available = [a.get("name") for a in agents]
        log.warning("No agents matched filter %s. Available agents: %s", allowed_names, available)

    # Select only primary agent per SC wallet to avoid NOT_PRIMARY_AGENT
    filtered = _select_primary_per_wallet(filtered, log)

    log.info("Filtered to %d agents: %s", len(filtered), [a.get("name") for a in filtered])
    return filtered


def _warn_shared_wallets(agents: list, log):
    """Warn if multiple agents share the same SC wallet."""
    from collections import Counter
    wallets = [a.get("molty_royale_wallet") for a in agents if a.get("molty_royale_wallet")]
    dupes = {w: c for w, c in Counter(wallets).items() if c > 1}
    if dupes:
        log.warning(
            "Multiple agents share SC wallets: %s. Only 1 agent per wallet can play. "
            "Set AGENT_NAMES to select which agent runs.",
            dupes
        )


def _select_primary_per_wallet(agents: list, log) -> list:
    """
    Select only 1 agent per SC wallet (molty_royale_wallet).
    If multiple agents share a wallet, pick the first one (assumed primary).
    This prevents NOT_PRIMARY_AGENT errors from the game server.
    """
    seen_wallets = {}
    selected = []

    for agent in agents:
        wallet = agent.get("molty_royale_wallet")
        if not wallet:
            selected.append(agent)
            continue

        if wallet in seen_wallets:
            log.warning(
                "Agent '%s' shares SC wallet %s with '%s' - skipping to avoid NOT_PRIMARY_AGENT",
                agent.get("name"), wallet, seen_wallets[wallet]
            )
            continue

        seen_wallets[wallet] = agent.get("name")
        selected.append(agent)

    return selected

