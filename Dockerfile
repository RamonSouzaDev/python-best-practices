# Syntax: Dockerfile for Python 2026 Best Practices
FROM python:3.13-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Copy dependency files
# Copy all project files at once since we are doing single stage
COPY . .

# Install dependencies
# We use --system or create a venv. Since we want uv managed 3.14, we let uv create the venv.
# We also need to ensure the system dependencies for 3.14 might be okay or use the managed one.
# Simplest for now: Use uv sync to install environment into .venv (default)
RUN uv sync --frozen

# Expose port
EXPOSE 8000

# Run with Uvicorn using `uv run` which handles the venv activation and python version automatically
CMD ["uv", "run", "uvicorn", "python_best_practices.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
