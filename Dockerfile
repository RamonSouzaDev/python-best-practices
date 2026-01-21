# Syntax: Dockerfile for Python 2026 Best Practices
# Using python:3.13-slim as a reliable base (since 3.14 is alpha/preview for many images)
FROM python:3.13-slim-bookworm AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies into a virtual environment
RUN uv venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv
# Force rebuild 2026-01-21-1
RUN uv pip install --python /opt/venv/bin/python -r pyproject.toml

# proper stage
FROM python:3.13-slim-bookworm

COPY --from=builder /opt/venv /opt/venv

# Add venv to path
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH="/app/src"

WORKDIR /app

COPY . .

# Install the project itself (if needed as a package)
# builder stage only installed dependencies. We can install project here or just run code.
# Since we copied /app/src, we can just point PYTHONPATH.

# Expose port
EXPOSE 8000

# Run with Uvicorn
# Update import path to match new structure
CMD ["uvicorn", "python_best_practices.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
