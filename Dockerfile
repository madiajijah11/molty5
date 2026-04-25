FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (cache layer for fast rebuilds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot source
COPY bot/ ./bot/

# Create dirs for credentials and memory persistence
RUN mkdir -p /app/dev-agent /root/.molty-royale

# Platform-agnostic: Railway and Fly.io both inject PORT env var; default 8080
EXPOSE 8080

# Platform-specific notes:
# - Railway: env vars injected at runtime, volumes configured via dashboard
# - Fly.io: uses fly.toml [mounts] for persistent volume at /root/.molty-royale
# - Local Docker: use docker run --env-file .env -v molty-data:/root/.molty-royale

CMD ["python", "-m", "bot.main"]
