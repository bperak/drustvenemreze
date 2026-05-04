"""Test logike iz bilježnice 11_marketing_primjer.ipynb (marketing / WOM centralnost).

Graf: gusti klaster A–D i periferija E preko D — D dominira betweennessom i degreeom.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


def _chapter11_toy_graph():
    G = nx.Graph()
    G.add_edges_from(
        [("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    )
    return G


def test_degree_and_betweenness_identify_broker_d():
    G = _chapter11_toy_graph()
    deg = nx.degree_centrality(G)
    bet = nx.betweenness_centrality(G)
    assert max(deg, key=deg.get) == "D"
    assert max(bet, key=bet.get) == "D"
    assert bet["D"] == 0.5
    assert bet["E"] == 0.0


def test_eigenvector_dominates_over_leaf_e():
    G = _chapter11_toy_graph()
    eig = nx.eigenvector_centrality(G, max_iter=500)
    assert eig["D"] > eig["E"]
    assert eig["A"] == eig["B"] == eig["C"]


def test_dataframe_ranking_roundtrip():
    G = _chapter11_toy_graph()
    deg = nx.degree_centrality(G)
    bet = nx.betweenness_centrality(G)
    eig = nx.eigenvector_centrality(G, max_iter=500)
    df = pd.DataFrame({"degree": deg, "betweenness": bet, "eigenvector": eig}).round(3)
    assert df.loc["E", "degree"] < df.loc["D", "degree"]


def test_draw_betweenness_colormap_no_display():
    G = _chapter11_toy_graph()
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


if __name__ == "__main__":
    test_degree_and_betweenness_identify_broker_d()
    test_eigenvector_dominates_over_leaf_e()
    test_dataframe_ranking_roundtrip()
    test_draw_betweenness_colormap_no_display()
    print("OK: testovi poglavlja 11")
