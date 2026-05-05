"""Izvršavanje kod-ćelija iz 15_ai_gemini_primjer.ipynb bez API ključa (preskočen poziv)."""
import json
import os
from pathlib import Path

def test_notebook_15_runs_without_api_key():
    os.environ.pop("GEMINI_API_KEY", None)
    os.environ.pop("GOOGLE_API_KEY", None)
    nb_path = Path(__file__).resolve().parent.parent / "code" / "15_ai_gemini_primjer.ipynb"
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    ns: dict = {}
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        code = "".join(cell["source"])
        exec(code, ns, ns)  # noqa: S102 — kontrolirani sadržaj repozitorija
    assert "summary" in ns
    assert isinstance(ns["summary"], dict)
    assert "degree_centrality" in ns["summary"]


def test_notebook_15_json_valid():
    nb_path = Path(__file__).resolve().parent.parent / "code" / "15_ai_gemini_primjer.ipynb"
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    assert nb["nbformat"] == 4
    assert any(c.get("cell_type") == "code" for c in nb["cells"])
