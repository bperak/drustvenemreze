"""Test logike iz bilježnice 08_difuzija_utjecaj_primjer.ipynb (difuzija / centralnost).

Provjerava očekivane odnose degree vs betweenness vs eigenvector na istom malom grafu
te Plotly simulacije širenja informacije (valovi + SI).
"""
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import pytest


def _patch_plotly_show_noop():
    """Sprječava blokiranje `fig.show()` u okruženjima bez interaktivnog renderera."""
    import plotly.graph_objects as go

    def _noop(self, *args, **kwargs):
        return None

    return go.Figure, go.Figure.show, _noop


def _chapter08_toy_graph():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])
    return G


def test_betweenness_bridge_node_dominates():
    G = _chapter08_toy_graph()
    bet = nx.betweenness_centrality(G)
    bridge = max(bet, key=bet.get)
    assert bridge == 4, "Čvor 4 je jedini most prema periferijskom čvoru 5"
    assert bet[4] > bet[1] and bet[4] > bet[5]


def test_eigenvector_and_degree_table_roundtrip():
    G = _chapter08_toy_graph()
    deg = dict(G.degree())
    eig = nx.eigenvector_centrality(G, max_iter=500)
    df = pd.DataFrame({"degree": deg, "eigenvector": eig}).round(3)
    assert df.loc[5, "degree"] == 1
    assert df.loc[4, "degree"] == 3
    assert df.loc[4, "eigenvector"] > df.loc[5, "eigenvector"]


def test_ego_radius_two_reach_counts():
    G = _chapter08_toy_graph()
    reach = {n: nx.ego_graph(G, n, radius=2).number_of_nodes() for n in G.nodes()}
    assert reach[5] == 4
    assert reach[1] == 4
    assert all(reach[n] == 5 for n in (2, 3, 4))


def test_draw_betweenness_colormap_no_display():
    G = _chapter08_toy_graph()
    bet = nx.betweenness_centrality(G)
    pos = nx.spring_layout(G, seed=42)
    plt.figure()
    nx.draw_networkx(
        G,
        pos,
        with_labels=True,
        node_color=[bet[n] for n in G.nodes()],
        cmap=plt.cm.Blues,
        edgecolors="black",
    )
    plt.close()


def test_notebook_08_plotly_diffusion_cells():
    pytest.importorskip("plotly")
    nb_path = Path(__file__).resolve().parent.parent / "code" / "08_difuzija_utjecaj_primjer.ipynb"
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    globs = {}
    cls, orig_show, noop = _patch_plotly_show_noop()
    cls.show = noop
    try:
        for idx in (1, 7, 8, 9, 10, 11):
            exec("".join(nb["cells"][idx]["source"]), globs, globs)  # noqa: S102
    finally:
        cls.show = orig_show

    assert globs["snimke"][-1] == {1, 2, 3, 4, 5}
    assert len(globs["snimke"]) == 4
    fig_val = globs["fig_valovi"]
    assert len(fig_val.frames) == 4
    assert len(globs["mu"]) >= 2
    assert globs["mu"][-1] >= 4.5
    assert np.isfinite(globs["koraci_hist"]).sum() >= 50


def test_notebook_08_bonus_karate_and_export():
    pytest.importorskip("plotly")
    nb_path = Path(__file__).resolve().parent.parent / "code" / "08_difuzija_utjecaj_primjer.ipynb"
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    globs = {}
    # Ćelija 19 (write_html) ostaje u bilježnici za ručni rad; ovdje testiramo isti API bez oslanjanja na mrežu.
    cls, orig_show, noop = _patch_plotly_show_noop()
    cls.show = noop
    try:
        for idx in (1, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18):
            exec("".join(nb["cells"][idx]["source"]), globs, globs)  # noqa: S102
    finally:
        cls.show = orig_show

    assert globs["K"].number_of_nodes() == 34
    assert len(globs["snaps_k"][-1]) == 34
    assert len(globs["fig_karate_valovi"].data[1].marker.color) == 34
    assert globs["mu_k0"][-1] >= 28

    export_dir = nb_path.parent / "exports"
    export_dir.mkdir(parents=True, exist_ok=True)
    html_path = export_dir / "08_plotly_bonus_karate_cmp_test.html"
    globs["fig_k_cmp"].write_html(html_path, include_plotlyjs="cdn", full_html=True)
    assert html_path.is_file()
    assert html_path.stat().st_size > 800
    html_path.unlink()


if __name__ == "__main__":
    test_betweenness_bridge_node_dominates()
    test_eigenvector_and_degree_table_roundtrip()
    test_ego_radius_two_reach_counts()
    test_draw_betweenness_colormap_no_display()
    print("OK: testovi poglavlja 08")
