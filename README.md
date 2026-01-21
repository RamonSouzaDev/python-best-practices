
<h1 align="center">Python 2026: The State of the Art 🐍</h1>
<h3 align="center">High-Performance • True Parallelism • Modern Toolchain</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Package_Manager-uv-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Linter-Ruff-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Data-Polars-orange?style=for-the-badge" />
</p>

---

## 👋 Hello, I'm Ramon Mendes - Software Developer
### Mastering the Next Generation of Python Engineering

This project serves as a definitive **2026 Reference Implementation** for modern Python development. It moves beyond the legacy stack (pip, pandas, GIL-limited execution) to embrace the performance revolution defined by Rust-based tooling and Python 3.14's free-threading capabilities.

- 🔭 **Project Goal**: Demonstrate a production-ready, high-speed Python environment.
- 🌱 **Tech Stack**:
    - **Runtime**: Python 3.14 (Free-threaded / NoGIL supported)
    - **Dependency Management**: `uv` (100x faster than pip)
    - **Linting & Formatting**: `Ruff` (Instantaneous analysis)
    - **API Framework**: `FastAPI` + `Pydantic v2`
    - **Data Processing**: `Polars` (Rust-backed, multi-core dataframes)

- 📫 **Contact**: dwmom@hotmail.com

---

## 🚀 Key Features & Releases Implemented

### 1. The New Toolchain (`uv` & `ruff`)
Gone are the days of sluggish `pip` installs and slow linting using `flake8`.
- **`uv`**: We use Astral's `uv` for package management. It resolves dependencies in milliseconds.
- **`ruff`**: A single tool replacing Black, Isort, and Flake8. Pre-configured in `pyproject.toml`.

### 2. High-Performance Base
- **FastAPI**: Asynchronous by default.
- **Polars**: Used instead of Pandas for data processing. It utilizes all CPU cores effectively, matching the 2026 parallel computing paradigm.

### 3. Dockerized & Ready
A multi-stage `Dockerfile` ensures the application is lightweight and secure, with a production-ready `gunicorn` + `uvicorn` setup hidden behind a clean interface.

---

## 🛠️ Installation & Running

### Using Docker (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RamonSouzaDev/python-best-practices.git
   cd python-best-practices
   ```

2. **Build and Run**:
   ```bash
   docker compose up --build
   ```

3. **Access the Application**:
   Open [http://localhost:8000](http://localhost:8000) to see the **Live Documentation & Demo**.

### Local Development (The 2026 Way)

1. **Install uv** (if not installed):
   ```bash
   pip install uv
   ```

2. **Sync Dependencies**:
   ```bash
   uv sync
   ```

3. **Run the App**:
   ```bash
   uv run uvicorn src.main:app --reload
   ```

4. **Run Tests**:
   ```bash
   uv run pytest
   ```

---

## 🧪 Testing & Code Quality

<p align="left">
  <img src="https://img.shields.io/badge/Tests-Pytest-green" />
  <img src="https://img.shields.io/badge/Coverage-100%25-brightgreen" />
</p>

To run the full test suite and linting checks:

```bash
# Run Linter
uv run ruff check .

# Run Unit Tests
uv run pytest
```

---

<p align="center">
  Built with ❤️ by Ramon Mendes for the IBM Interview Studies
</p>
