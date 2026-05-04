"""Logika iz bilježnice 09_dinamika_mreza.ipynb — snimci, Jaccard, Louvain."""
import json
from pathlib import Path

import networkx as nx
from networkx.algorithms import community


def jaccard_bridova(G_prije, G_poslije):
    norm = lambda G: {frozenset((u, v)) for u, v in G.edges()}
    A, B = norm(G_prije), norm(G_poslije)
    if not A and not B:
        return 1.0
    return len(A & B) / len(A | B)


def test_notebook_09_snapshot_metrics():
    G1 = nx.Graph()
    G1.add_edges_from([("Ana", "Bruno"), ("Bruno", "Carla")])
    G2 = nx.Graph()
    G2.add_edges_from(
        [
            ("Ana", "Bruno"),
            ("Bruno", "Carla"),
            ("Carla", "David"),
            ("David", "Ana"),
        ]
    )

    assert G1.number_of_nodes() == 3
    assert G1.number_of_edges() == 2
    assert G2.number_of_nodes() == 4
    assert G2.number_of_edges() == 4
    assert round(nx.density(G1), 4) == round(2 / 3, 4)
    assert round(nx.density(G2), 4) == round(4 / 6, 4)
    assert round(jaccard_bridova(G1, G2), 4) == 0.5

    deg1 = nx.degree_centrality(G1)
    deg2 = nx.degree_centrality(G2)
    assert "David" not in deg1
    assert abs(deg2["David"] - 2 / 3) < 1e-9

    comms1 = community.louvain_communities(G1, seed=42)
    comms2 = community.louvain_communities(G2, seed=42)
    Q1 = community.modularity(G1, comms1)
    Q2 = community.modularity(G2, comms2)
    assert -0.51 <= Q1 <= 1.0
    assert -0.51 <= Q2 <= 1.0
    assert len(comms2) >= 1


def test_notebook_09_json_executable():
    """Izvorna ćelija bilježnice mora biti valjan Python (UTF-8)."""
    nb_path = Path(__file__).resolve().parent.parent / "code" / "09_dinamika_mreza.ipynb"
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    code = "".join(nb["cells"][1]["source"])
    ns = {}
    exec(code, ns, ns)  # noqa: S102 — kontrolirani sadržaj repozitorija
    assert "jaccard_bridova" in ns
