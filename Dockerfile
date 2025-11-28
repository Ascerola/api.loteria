# syntax=docker/dockerfile:1

FROM python:3.13-slim AS base

# Install uv (Python package manager)
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:/root/.cargo/bin:${PATH}" \
    UV_PROJECT_ENV=/app/.venv \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first for better cache usage
COPY pyproject.toml ./
RUN uv sync --no-dev

# Copy the rest of the application
COPY . .

CMD ["uv", "run", "fastapi", "dev", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]
