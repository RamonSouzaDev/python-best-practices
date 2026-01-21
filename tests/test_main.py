import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Python 2026" in response.text

def test_benchmark_endpoint():
    response = client.get("/api/benchmark")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["engine"] == "Polars (Rust-backed)"
    assert len(data["sample"]) > 0
