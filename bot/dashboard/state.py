"""
Dashboard shared state — bridge between bot engine and web dashboard.
Bot writes → Dashboard reads. Thread-safe via asyncio lock.
"""

import time
from collections import deque
from bot.utils.logger import get_logger

log = get_logger(__name__)

# Maximum log entries kept in memory
MAX_LOGS = 500


class DashboardState:
    """Singleton shared state between bot and dashboard."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True

        # ── Agent state ────────────────────────────────────────
        self.agents: dict[str, dict] = {}  # {agent_id: {name, status, hp, ep, ...}}

        # ── Global stats ───────────────────────────────────────
        self.total_wins = 0
        self.total_moltz = 0
        self.total_smoltz = 0
        self.total_cross = 0.0
        self.bots_running = 0

        # ── Logs ───────────────────────────────────────────────
        self.global_logs: deque = deque(maxlen=MAX_LOGS)
        self.agent_logs: dict[str, deque] = {}  # {agent_id: deque}

        # ── Accounts ───────────────────────────────────────────
        self.accounts: list[dict] = []

        # ── Learning / Memory ──────────────────────────────────
        self.learning_data: dict = {
            "total_games": 0,
            "wins": 0,
            "win_rate": 0.0,
            "avg_kills": 0.0,
            "lessons": [],
            "strategy_rules": [],
            "opponents": [],
        }

        # ── Timestamps ─────────────────────────────────────────
        self.started_at = time.time()
        self.last_update = time.time()

    # ── Bot writes ─────────────────────────────────────────────

    def update_agent(self, agent_id: str, data: dict):
        """Update agent state from bot engine."""
        if agent_id not in self.agents:
            self.agents[agent_id] = {}
            self.agent_logs[agent_id] = deque(maxlen=MAX_LOGS)
        self.agents[agent_id].update(data)
        self.agents[agent_id]["last_update"] = time.time()
        self.last_update = time.time()

    def add_log(self, message: str, level: str = "info", agent_id: str = None):
        """Add log entry."""
        entry = {
            "ts": time.time(),
            "msg": message,
            "level": level,
            "agent": agent_id,
        }
        self.global_logs.append(entry)
        if agent_id and agent_id in self.agent_logs:
            self.agent_logs[agent_id].append(entry)

    def set_account(self, account_data: dict):
        """Add or update account."""
        api_key = account_data.get("api_key", "")
        for i, acc in enumerate(self.accounts):
            if acc.get("api_key") == api_key:
                self.accounts[i] = account_data
                return
        self.accounts.append(account_data)

    def update_learning(self, memory_stats: dict):
        """Update learning data from AgentMemory.get_stats()."""
        if not memory_stats:
            return
        self.learning_data["total_games"] = memory_stats.get("total_games", 0)
        self.learning_data["wins"] = memory_stats.get("wins", 0)
        self.learning_data["win_rate"] = memory_stats.get("win_rate", 0.0)
        self.learning_data["avg_kills"] = memory_stats.get("avg_kills", 0.0)
        self.learning_data["lessons_count"] = memory_stats.get("lessons_count", 0)
        self.learning_data["rules_count"] = memory_stats.get("rules_count", 0)
        self.learning_data["opponents_count"] = memory_stats.get("opponents_count", 0)
        # Full lists for tab display
        self.learning_data["lessons"] = memory_stats.get("lessons", [])
        self.learning_data["strategy_rules"] = memory_stats.get("strategy_rules", [])
        self.learning_data["opponents"] = memory_stats.get("opponents", [])
        self.learning_data["dangerous_opponents"] = memory_stats.get(
            "dangerous_opponents", []
        )
        self.last_update = time.time()

    # ── Dashboard reads ────────────────────────────────────────

    def get_snapshot(self) -> dict:
        """Full state snapshot for dashboard API."""
        return {
            "agents": dict(self.agents),
            "stats": {
                "total_wins": self.total_wins,
                "total_moltz": self.total_moltz,
                "total_smoltz": self.total_smoltz,
                "total_cross": self.total_cross,
                "bots_running": self.bots_running,
                "agents_active": sum(
                    1 for a in self.agents.values() if a.get("status") == "playing"
                ),
                "agents_idle": sum(
                    1
                    for a in self.agents.values()
                    if a.get("status") in ("idle", "queuing")
                ),
                "agents_dead": sum(
                    1 for a in self.agents.values() if a.get("status") == "dead"
                ),
                "agents_error": sum(
                    1 for a in self.agents.values() if a.get("status") == "error"
                ),
                "uptime": time.time() - self.started_at,
            },
            "accounts": self.accounts,
            "learning": dict(self.learning_data),
            "logs": list(self.global_logs)[-200:],
            "agent_logs": {k: list(v)[-100:] for k, v in self.agent_logs.items()},
        }


# Global singleton
dashboard_state = DashboardState()
