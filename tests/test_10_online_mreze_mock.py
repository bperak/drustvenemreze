"""Logika iz bilježnice 10_online_mreze_primjer.ipynb — mock pratnja i kulturni scenarij."""
import json
from pathlib import Path

import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities


def digraph_follow_mock():
    D = nx.DiGraph()
    D.add_edges_from(
        [
            ("u1", "u2"),
            ("u1", "u3"),
            ("u2", "u1"),
            ("u3", "u1"),
            ("u4", "u1"),
            ("u4", "u2"),
        ]
    )
    return D


def graph_kulturni_dogadaj_mock():
    G = nx.Graph()
    G.add_edges_from(
        [
            ("festival", "lokalni_portal"),
            ("festival", "volonter_A"),
            ("festival", "volonter_B"),
            ("lokalni_portal", "volonter_A"),
            ("lokalni_portal", "volonter_B"),
            ("volonter_A", "volonter_B"),
        ]
    )
    G.add_edges_from(
        [
            ("nacionalni_medij", "kriticar"),
            ("nacionalni_medij", "muzej_partner"),
            ("kriticar", "muzej_partner"),
        ]
    )
    G.add_edge("festival", "nacionalni_medij")
    return G


def test_mock_follow_indegree_max_u1():
    D = digraph_follow_mock()
    in_deg = dict(D.in_degree())
    assert in_deg["u1"] == max(in_deg.values())
    assert D.number_of_edges() == 6


def test_mock_follow_pagerank_positive():
    D = digraph_follow_mock()
    pr = nx.pagerank(D, alpha=0.85)
    assert all(v > 0 for v in pr.values())
    assert max(pr, key=pr.get) == "u1"


def test_mock_kulturni_dvije_zajednice():
    G = graph_kulturni_dogadaj_mock()
    parts = list(greedy_modularity_communities(G))
    assert len(parts) == 2
    flat = {n for p in parts for n in p}
    assert flat == set(G.nodes())


def test_notebook_10_code_cells_executable():
    """Sve kod-ćelije bilježnice moraju se izvršiti uz zajednički namespace."""
    nb_path = Path(__file__).resolve().parent.parent / "code" / "10_online_mreze_primjer.ipynb"
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    ns: dict = {}
    for cell in nb["cells"]:
        if cell.get("cell_type") != "code":
            continue
        code = "".join(cell["source"])
        exec(code, ns, ns)  # noqa: S102 — kontrolirani sadržaj repozitorija
    assert "G" in ns and isinstance(ns["G"], nx.Graph)
    assert "D" in ns and isinstance(ns["D"], nx.DiGraph)
