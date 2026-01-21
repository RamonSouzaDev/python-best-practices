# Syntax: Dockerfile for Python 2026 Best Practices
# Using an imaginary Python 3.14 base image for the prompt's context (in reality, likely 3.13/3.14-rc)
# We will use python:3.13-slim as a proxy for "3.14" stability if 3.14 isn't available, but I'll label it for the user's request.
FROM python:3.13-slim-bookworm AS builder

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Copy dependency files
COPY pyproject.toml .
# COPY uv.lock . # (If we had one)

# Install dependencies into a virtual environment
RUN uv venv /opt/venv && \
    uv pip install -r pyproject.toml

# proper stage
FROM python:3.13-slim-bookworm

COPY --from=builder /opt/venv /opt/venv

# Add venv to path
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH="/app/src"

WORKDIR /app

COPY . .

# Expose port
EXPOSE 8000

# Run with Gunicorn/Uvicorn for production-grade performance
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
