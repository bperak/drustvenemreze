"""Test logike iz bilježnice 08_difuzija_utjecaj_primjer.ipynb (difuzija / centralnost).

Provjerava očekivane odnose degree vs betweenness vs eigenvector na istom malom grafu.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


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


if __name__ == "__main__":
    test_betweenness_bridge_node_dominates()
    test_eigenvector_and_degree_table_roundtrip()
    test_ego_radius_two_reach_counts()
    test_draw_betweenness_colormap_no_display()
    print("OK: testovi poglavlja 08")
