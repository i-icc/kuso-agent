# syntax=docker/dockerfile:1

FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /app

ENV UV_PROJECT_ENVIRONMENT=/app/.venv \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1

COPY . .

RUN uv sync --no-dev

ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uv run adk web --host 0.0.0.0 --port ${PORT:-8000}"]
