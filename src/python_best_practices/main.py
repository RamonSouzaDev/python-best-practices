from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import polars as pl
from datetime import datetime
import os

# Initialize FastAPI
app = FastAPI(
    title="Python 2026 Best Practices",
    description="Demonstrating the State of the Art in Python Development",
    version="1.0.0"
)

# Mount static directory for images
# Ensure the directory exists to avoid startup errors
static_path = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_path, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Modern 2026 Type Alias
type Coordinates = tuple[float, float]

class TechStack(BaseModel):
    component: str
    choice: str
    description: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """
    Returns a premium, high-performance landing page.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python 2026: The Future is Now</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Outfit', sans-serif; background-color: #0f172a; overflow-x: hidden; }
            .glass {
                background: rgba(30, 41, 59, 0.7);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            }
            .glass-card {
                background: linear-gradient(145deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.9));
                border: 1px solid rgba(16, 185, 129, 0.2);
                transition: all 0.3s ease;
            }
            .glass-card:hover {
                transform: translateY(-5px);
                border-color: rgba(16, 185, 129, 0.6);
                box-shadow: 0 20px 25px -5px rgba(16, 185, 129, 0.15);
            }
            .text-glow {
                text-shadow: 0 0 20px rgba(52, 211, 153, 0.5);
            }
            .animate-float {
                animation: float 6s ease-in-out infinite;
            }
            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-20px); }
                100% { transform: translateY(0px); }
            }
            .grid-bg {
                background-image: linear-gradient(rgba(16, 185, 129, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(16, 185, 129, 0.05) 1px, transparent 1px);
                background-size: 30px 30px;
            }
        </style>
    </head>
    <body class="text-white min-h-screen flex flex-col items-center relative grid-bg">
        
        <!-- Decorative Glows -->
        <div class="absolute top-0 left-0 w-full h-96 bg-gradient-to-b from-emerald-500/10 to-transparent pointer-events-none"></div>
        <div class="absolute bottom-0 right-0 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>

        <nav class="w-full max-w-7xl px-6 py-6 flex justify-between items-center z-10 animate-fade-in-down">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-400 to-emerald-400 flex items-center justify-center font-bold text-slate-900">
                    26
                </div>
                <span class="font-bold text-xl tracking-wide">PY<span class="text-emerald-400">PROJECT</span></span>
            </div>
            <a href="https://github.com/RamonSouzaDev/python-best-practices" target="_blank" class="px-5 py-2 glass rounded-full hover:bg-white/10 transition text-sm font-medium">
                View on GitHub
            </a>
        </nav>

        <main class="w-full max-w-7xl px-6 flex flex-col items-center mt-10 z-10">
            <!-- Hero Section -->
            <div class="text-center max-w-4xl relative">
                <img src="/static/python-logo.png" alt="Python Logo" class="w-24 h-24 mx-auto mb-6 drop-shadow-2xl animate-float">
                <h1 class="text-6xl md:text-8xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-300 via-emerald-300 to-green-300 mb-6 leading-tight">
                    The State of the Art
                </h1>
                <p class="text-xl md:text-2xl text-slate-400 max-w-2xl mx-auto leading-relaxed">
                    Experience <span class="text-emerald-400 font-semibold">Python 3.14</span> Free-Threading, 
                    <span class="text-blue-400 font-semibold">uv</span> Speed, and 
                    <span class="text-purple-400 font-semibold">Polars</span> Performance.
                </p>
            </div>

            <!-- Perf Section -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 w-full mt-24">
                
                <!-- Stack Cards -->
                <div class="grid grid-cols-1 gap-4">
                    <div class="glass-card p-6 rounded-2xl flex items-start gap-4">
                        <div class="p-3 bg-blue-500/20 rounded-xl text-blue-400">⚡</div>
                        <div>
                            <h3 class="font-bold text-lg text-white">uv Packages</h3>
                            <p class="text-slate-400 text-sm mt-1">100x faster resolution using Rust.</p>
                        </div>
                    </div>
                    <div class="glass-card p-6 rounded-2xl flex items-start gap-4">
                        <div class="p-3 bg-emerald-500/20 rounded-xl text-emerald-400">🐍</div>
                        <div>
                            <h3 class="font-bold text-lg text-white">Python 3.14 NoGIL</h3>
                            <p class="text-slate-400 text-sm mt-1">True multi-core parallelism is finally here.</p>
                        </div>
                    </div>
                    <div class="glass-card p-6 rounded-2xl flex items-start gap-4">
                        <div class="p-3 bg-purple-500/20 rounded-xl text-purple-400">🛡️</div>
                        <div>
                            <h3 class="font-bold text-lg text-white">Ruff Linter</h3>
                            <p class="text-slate-400 text-sm mt-1">Instant static analysis.</p>
                        </div>
                    </div>
                </div>

                <!-- Live Demo -->
                <div class="glass p-8 rounded-3xl border-t border-emerald-500/30 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <h2 class="text-2xl font-bold text-white flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
                                Live Benchmark
                            </h2>
                            <span class="text-xs font-mono text-emerald-400 bg-emerald-900/30 px-2 py-1 rounded">POWERED BY POLARS</span>
                        </div>
                        <div class="bg-slate-900/80 p-6 rounded-xl font-mono text-sm h-48 overflow-y-auto mb-6 border border-slate-700 shadow-inner" id="console">
                            <p class="text-slate-500">> System Ready.</p>
                            <p class="text-slate-500">> Waiting for user input...</p>
                        </div>
                    </div>
                    
                    <button onclick="runBenchmark()" class="w-full py-4 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 rounded-xl font-bold text-white shadow-lg shadow-emerald-900/20 transition transform active:scale-95">
                        Run Heavy Computation (Rust)
                    </button>
                </div>
            </div>

            <footer class="mt-20 mb-10 text-slate-600 text-sm font-medium">
                © 2026 Ramon Mendes • Architecting the Future
            </footer>
        </main>

        <script>
            async function runBenchmark() {
                const consoleDiv = document.getElementById('console');
                const log = (text, color = 'text-slate-300') => {
                    consoleDiv.innerHTML += `<p class="${color} mt-1">> ${text}</p>`;
                    consoleDiv.scrollTop = consoleDiv.scrollHeight;
                };
                
                log("Initializing Polars Engine...", "text-blue-400");
                log("Processing 10,000 rows across cores...");

                try {
                    const res = await fetch('/api/benchmark');
                    const data = await res.json();
                    
                    setTimeout(() => {
                        log(`Success! Engine: ${data.engine}`, "text-emerald-400");
                        log(`Time: ${data.duration_ms}ms`, "text-yellow-400");
                        log(`Sample Result: ${JSON.stringify(data.sample).substring(0, 50)}...`, "text-slate-500");
                    }, 600);
                } catch (e) {
                    log("Error connecting to backend.", "text-red-500");
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
    df = pl.DataFrame({
        "a": range(10000),
        "b": [x * 2 for x in range(10000)],
        "category": ["A", "B", "C", "D"] * 2500
    })
    
    # Perform aggregation
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
