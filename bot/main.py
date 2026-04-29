"""
Molty Royale AI Agent — Entry Point v2.0.
Run: python -m bot.main
Dashboard + Multi-Agent run concurrently.
"""
import asyncio
import os
import sys
from bot.heartbeat import Heartbeat
from bot.dashboard.server import start_dashboard
from bot.config import load_agents
from bot.utils.logger import get_logger

log = get_logger(__name__)

# Railway injects PORT env var; fallback to DASHBOARD_PORT or 8080
DASHBOARD_PORT = int(os.getenv("PORT", os.getenv("DASHBOARD_PORT", "8080")))


def main():
    """Entry point for the bot."""
    log.info("Molty Royale AI Agent v2.0.0 — Multi-Agent Mode")
    log.info("Press Ctrl+C to stop")

    # Load all agents from AGENTS_JSON env var or credentials.json
    agents = load_agents()

    if not agents:
        log.error("No agents found! Set AGENTS_JSON env var or add agents to credentials.json")
        sys.exit(1)

    log.info("Starting %d agent(s)...", len(agents))

    # Create Heartbeat instance for each agent
    heartbeats = [Heartbeat(agent_config=agent) for agent in agents]

    async def run_all():
        # Start dashboard server (non-blocking)
        await start_dashboard(port=DASHBOARD_PORT)

        # Run all agents concurrently
        tasks = [hb.run() for hb in heartbeats]
        await asyncio.gather(*tasks)

    try:
        if sys.platform == "win32":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(run_all())
    except KeyboardInterrupt:
        log.info("Shutdown signal received.")
        # Signal all heartbeats to stop
        for hb in heartbeats:
            hb.running = False
        log.info("Shutdown complete.")


if __name__ == "__main__":
    main()
