"""
Free game join via matchmaking queue.
POST /join (Long Poll ~15s) → assigned → open WS immediately.
Rate-limited: max 30 attempts, 0.5s delay between retries.
"""

import asyncio
from bot.api_client import MoltyAPI, APIError
from bot.utils.logger import get_logger

log = get_logger(__name__)

MAX_ATTEMPTS = 30  # ~15 seconds at 0.5s delay
RETRY_DELAY = 0.5  # seconds between attempts


async def join_free_game(api: MoltyAPI) -> tuple[str, str]:
    """
    Enter free matchmaking queue and wait for assignment.
    Returns (game_id, agent_id) when assigned.
    """
    # Idempotency guard: check queue status first
    try:
        status_resp = await api.get_join_status()
        if isinstance(status_resp, dict):
            status = status_resp.get("status", "not_queued")
            if status == "assigned":
                gid = status_resp.get("gameId", "")
                aid = status_resp.get("agentId", "")
                if gid and aid:
                    log.info("Already assigned to game: %s", gid)
                    return gid, aid
            elif status == "queued":
                log.info("Already in queue, resuming...")
    except APIError:
        pass

    # Queue loop with rate limiting
    attempt = 0
    last_log_at = 0  # throttle logging
    while attempt < MAX_ATTEMPTS:
        attempt += 1

        try:
            resp = await api.post_join("free")
            if not isinstance(resp, dict):
                log.warning("Unexpected join response type: %s", type(resp).__name__)
                await asyncio.sleep(RETRY_DELAY)
                continue

            status = resp.get("status", "")

            if status == "assigned":
                gid = resp.get("gameId", "")
                aid = resp.get("agentId", "")
                if gid and aid:
                    log.info("✅ Assigned to free game: %s (agent=%s)", gid, aid)
                    return gid, aid
                log.warning("Assigned but missing gameId/agentId: %s", resp)

            # Log every 10th attempt to reduce noise
            if attempt - last_log_at >= 10:
                log.info("Free queue attempt #%d (status=%s)...", attempt, status)
                last_log_at = attempt

            await asyncio.sleep(RETRY_DELAY)

        except APIError as e:
            if e.code == "NO_IDENTITY":
                log.error("❌ ERC-8004 identity not registered. Cannot join free room.")
                raise
            if e.code == "OWNERSHIP_LOST":
                log.error("❌ NFT ownership changed. Re-register identity.")
                raise
            if e.code == "SERVICE_UNAVAILABLE":
                log.warning(
                    "Service unavailable — matchmaking paused (attempt %d). "
                    "Waiting 10s...",
                    attempt,
                )
                await asyncio.sleep(10)
                continue
            if e.code == "TOO_MANY_AGENTS_PER_IP":
                log.error("❌ IP agent limit reached for this game")
                raise
            if e.code in ("FORBIDDEN", "UNAUTHORIZED"):
                log.error("❌ API key rejected (403). Stopping.")
                raise
            if e.code == "ACCOUNT_ALREADY_IN_GAME":
                log.info("Already in a game. Returning to heartbeat.")
                raise
            # Unknown errors: back off
            log.warning(
                "Join error: %s — retrying (attempt %d/%d)",
                e,
                attempt,
                MAX_ATTEMPTS,
            )
            await asyncio.sleep(RETRY_DELAY * 2)

    log.warning(
        "Free queue exhausted after %d attempts — trying again next cycle", MAX_ATTEMPTS
    )
    return "", ""
