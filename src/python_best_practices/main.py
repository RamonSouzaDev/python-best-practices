from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import polars as pl
import asyncio
from datetime import datetime

# Initialize FastAPI
app = FastAPI(
    title="Python 2026 Best Practices",
    description="Demonstrating the State of the Art in Python Development",
    version="1.0.0"
)

# Modern 2026 Type Alias (PEP 695 style if supported, otherwise standard)
type Coordinates = tuple[float, float]

class TechStack(BaseModel):
    component: str
    choice: str
    description: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """
    Returns a beautifully styled landing page explaining the implementation.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python 2026: State of the Art</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body { font-family: 'Inter', sans-serif; }
            .glass { background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2); }
        </style>
    </head>
    <body class="bg-slate-900 text-white min-h-screen flex flex-col items-center p-10">
        <header class="mb-10 text-center">
            <h1 class="text-6xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400 mb-4">
                Python 2026
            </h1>
            <p class="text-xl text-slate-400">High-Performance • Async • Typed • Parallel</p>
        </header>

        <main class="max-w-4xl w-full grid gap-8">
            <section class="glass p-8 rounded-2xl shadow-2xl">
                <h2 class="text-3xl font-bold mb-6 text-emerald-400">🚀 The Stack Implemented</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="p-4 bg-slate-800 rounded-lg border border-slate-700">
                        <h3 class="font-bold text-lg text-blue-300">🐍 Python 3.14 (Free-Threaded)</h3>
                        <p class="text-slate-400 text-sm mt-2">Running without the GIL for true parallelism on multi-core CPUs.</p>
                    </div>
                    <div class="p-4 bg-slate-800 rounded-lg border border-slate-700">
                        <h3 class="font-bold text-lg text-blue-300">⚡ uv Package Manager</h3>
                        <p class="text-slate-400 text-sm mt-2">Replaces pip/poetry. 10-100x faster dependency resolution using Rust.</p>
                    </div>
                    <div class="p-4 bg-slate-800 rounded-lg border border-slate-700">
                        <h3 class="font-bold text-lg text-blue-300">🛡️ Ruff Linter</h3>
                        <p class="text-slate-400 text-sm mt-2">Instant static analysis and formatting. Replaces Flake8/Black.</p>
                    </div>
                    <div class="p-4 bg-slate-800 rounded-lg border border-slate-700">
                        <h3 class="font-bold text-lg text-blue-300">🐼 Polars</h3>
                        <p class="text-slate-400 text-sm mt-2">The new standard for dataframes. Multi-threaded and Rust-backed.</p>
                    </div>
                </div>
            </section>

            <section class="glass p-8 rounded-2xl shadow-2xl">
                <h2 class="text-3xl font-bold mb-6 text-purple-400">📊 Live Performance Demo</h2>
                <div class="bg-slate-800 p-6 rounded-lg font-mono text-sm overflow-x-auto">
                    <p class="text-green-400">$ Processing large dataset with Polars...</p>
                    <p class="text-slate-300 mt-2" id="perf-output">Loading...</p>
                </div>
                <button onclick="fetchPerf()" class="mt-4 px-6 py-2 bg-blue-600 hover:bg-blue-500 rounded-full font-bold transition">
                    Run Benchmark
                </button>
            </section>
        </main>

        <footer class="mt-20 text-slate-500 text-sm">
            Developed by Ramon Mendes • 2026 Best Practices Demo
        </footer>

        <script>
            async function fetchPerf() {
                const out = document.getElementById('perf-output');
                out.innerText = "Running async calculation...";
                try {
                    const res = await fetch('/api/benchmark');
                    const data = await res.json();
                    out.innerHTML = `Processed ${data.rows} rows in ${data.duration_ms}ms.<br>Result: ${JSON.stringify(data.sample)}`;
                } catch (e) {
                    out.innerText = "Error fetching data.";
                }
            }
        </script>
    </body>
    </html>
    """
    return html_content

@app.get("/api/benchmark")
async def benchmark_endpoint():
    """
    Simulates a heavy data processing task using Polars to demonstrate performance.
    """
    start = datetime.now()
    
    # 2026 Best Practice: Use Polars for data manipulation
    # Creating a dummy DataFrame efficiently
    df = pl.DataFrame({
        "a": range(10000),
        "b": [x * 2 for x in range(10000)],
        "category": ["A", "B", "C", "D"] * 2500
    })
    
    # Perform aggregation (uses multiple cores in Polars)
    result = df.group_by("category").agg(
        pl.col("b").sum().alias("total_b"),
        pl.col("a").mean().alias("avg_a")
    )
    
    duration = (datetime.now() - start).total_seconds() * 1000
    
    return {
        "status": "success",
        "engine": "Polars (Rust-backed)",
        "rows": 10000,
        "duration_ms": round(duration, 2),
        "sample": result.to_dicts()
    }
