"""Test da se kod iz bilježnice 07_vizualizacija_layouti.ipynb izvršava bez grešaka.

Replicira sve ćelije i provjerava da se slike i exporti mogu generirati.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import networkx as nx
import numpy as np
from networkx.algorithms import community


def scale_sizes(values, lo=80, hi=1200):
    arr = np.array(list(values), dtype=float)
    if arr.max() == arr.min():
        return [(lo + hi) / 2] * len(arr)
    return list(lo + (hi - lo) * (arr - arr.min()) / (arr.max() - arr.min()))


def test_notebook_07_full_flow():
    plt.rcParams['figure.dpi'] = 110
    plt.rcParams['savefig.dpi'] = 300

    G = nx.karate_club_graph()
    assert G.number_of_nodes() == 34
    assert G.number_of_edges() == 78

    plt.figure(figsize=(6, 5))
    nx.draw(G, with_labels=True, node_color='lightgray', node_size=300)
    plt.close()

    layouts = {
        'spring': nx.spring_layout(G, seed=42),
        'kamada-kawai': nx.kamada_kawai_layout(G),
        'circular': nx.circular_layout(G),
        'shell': nx.shell_layout(G),
        'spectral': nx.spectral_layout(G),
    }
    for name, pos in layouts.items():
        assert len(pos) == G.number_of_nodes(), f'{name} failed'

    fig, axes = plt.subplots(1, 5, figsize=(22, 5))
    for ax, (name, pos) in zip(axes, layouts.items()):
        nx.draw(G, pos, ax=ax, node_color='steelblue', node_size=120,
                edge_color='lightgray', with_labels=False)
    plt.close(fig)

    pos = nx.spring_layout(G, seed=42)
    deg = dict(G.degree())
    sizes = [deg[n] * 60 + 80 for n in G.nodes()]
    top5 = sorted(deg, key=deg.get, reverse=True)[:5]
    labels = {n: f'{n}\n(deg={deg[n]})' for n in top5}

    plt.figure(figsize=(9, 7))
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_nodes(G, pos, node_size=sizes,
                           node_color='steelblue', alpha=0.85)
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=9)
    plt.close()

    centralities = {
        'Degree': nx.degree_centrality(G),
        'Betweenness': nx.betweenness_centrality(G),
        'Closeness': nx.closeness_centrality(G),
        'Eigenvector': nx.eigenvector_centrality(G, max_iter=1000),
    }
    assert all(len(c) == G.number_of_nodes() for c in centralities.values())

    fig, axes = plt.subplots(1, 4, figsize=(22, 6))
    for ax, (name, cent) in zip(axes, centralities.items()):
        sizes_c = scale_sizes([cent[n] for n in G.nodes()], lo=50, hi=1400)
        nx.draw_networkx_edges(G, pos, alpha=0.25, ax=ax)
        nx.draw_networkx_nodes(G, pos, node_size=sizes_c,
                               node_color=[cent[n] for n in G.nodes()],
                               cmap='plasma', alpha=0.9,
                               edgecolors='white', linewidths=1.2, ax=ax)
    plt.close(fig)

    comms = community.louvain_communities(G, seed=42)
    assert len(comms) >= 2
    node2comm = {n: i for i, c in enumerate(comms) for n in c}
    colors = [node2comm[n] for n in G.nodes()]
    Q = community.modularity(G, comms)
    assert Q > 0.3, f'Q too low: {Q}'

    plt.figure(figsize=(10, 7))
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color=colors,
                           cmap='Set2', alpha=0.9,
                           edgecolors='white', linewidths=1.5)
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=9)
    plt.close()

    ego_center = 0
    ego = nx.ego_graph(G, ego_center, radius=1)
    assert ego.number_of_nodes() >= 2
    assert ego_center in ego.nodes()
    pos_e = nx.spring_layout(ego, seed=7)
    ego_density = nx.density(ego)
    assert 0 <= ego_density <= 1

    plt.figure(figsize=(9, 7))
    nx.draw_networkx_edges(ego, pos_e)
    nx.draw_networkx_nodes(ego, pos_e, node_size=500, node_color='lightsteelblue')
    nx.draw_networkx_labels(ego, pos_e, font_size=9)
    plt.close()

    H = nx.Graph()
    razgovori = [
        ('Ana', 'Bruno', 8), ('Ana', 'Carla', 10), ('Bruno', 'Carla', 9),
        ('Carla', 'David', 3), ('David', 'Eva', 7), ('David', 'Filip', 6),
        ('Eva', 'Filip', 8), ('Filip', 'Goran', 2),
        ('Goran', 'Hana', 9), ('Goran', 'Ivan', 8), ('Hana', 'Ivan', 7),
    ]
    H.add_weighted_edges_from(razgovori)
    pos_h = nx.spring_layout(H, seed=7, k=0.8)
    weights = [H[u][v]['weight'] for u, v in H.edges()]
    widths = [w * 0.5 for w in weights]
    comms_h = community.louvain_communities(H, seed=42)
    n2c_h = {n: i for i, c in enumerate(comms_h) for n in c}
    colors_h = [n2c_h[n] for n in H.nodes()]

    plt.figure(figsize=(10, 7))
    nx.draw_networkx_edges(H, pos_h, width=widths, alpha=0.5, edge_color='gray')
    nx.draw_networkx_nodes(H, pos_h, node_size=900, node_color=colors_h,
                           cmap='Pastel1', edgecolors='black', linewidths=1.5)
    nx.draw_networkx_labels(H, pos_h, font_size=10)
    edge_labels = {(u, v): H[u][v]['weight'] for u, v in H.edges()}
    nx.draw_networkx_edge_labels(H, pos_h, edge_labels=edge_labels, font_size=8)
    plt.close()

    Big = nx.barabasi_albert_graph(500, 3, seed=42)
    assert Big.number_of_nodes() == 500
    deg_b = dict(Big.degree())
    top_nodes = sorted(deg_b, key=deg_b.get, reverse=True)[:50]
    Sub = Big.subgraph(top_nodes)
    comms_sub = community.louvain_communities(Sub, seed=42)
    assert len(comms_sub) >= 1

    F = nx.florentine_families_graph()
    assert F.number_of_nodes() == 15
    deg_f = dict(F.degree())
    bet_f = nx.betweenness_centrality(F)

    top_deg = max(deg_f, key=deg_f.get)
    top_bet = max(bet_f, key=bet_f.get)
    assert top_bet == 'Medici', f'Medici should dominate betweenness, got {top_bet}'

    pos_f = nx.kamada_kawai_layout(F)
    sizes_deg = scale_sizes([deg_f[n] for n in F.nodes()], lo=200, hi=1800)
    sizes_bet = scale_sizes([bet_f[n] for n in F.nodes()], lo=200, hi=1800)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(17, 7))
    nx.draw_networkx_edges(F, pos_f, alpha=0.4, ax=ax1)
    nx.draw_networkx_nodes(F, pos_f, node_size=sizes_deg,
                           node_color=[deg_f[n] for n in F.nodes()],
                           cmap='Blues', edgecolors='black', linewidths=1.2, ax=ax1)
    nx.draw_networkx_labels(F, pos_f, font_size=9, ax=ax1)

    nx.draw_networkx_edges(F, pos_f, alpha=0.4, ax=ax2)
    nx.draw_networkx_nodes(F, pos_f, node_size=sizes_bet,
                           node_color=[bet_f[n] for n in F.nodes()],
                           cmap='Reds', edgecolors='black', linewidths=1.2, ax=ax2)
    nx.draw_networkx_labels(F, pos_f, font_size=9, ax=ax2)
    plt.close(fig)

    bet_g = nx.betweenness_centrality(G)
    top_brokers = sorted(bet_g, key=bet_g.get, reverse=True)[:3]
    edgecolors = ['crimson' if n in top_brokers else 'white' for n in G.nodes()]
    linewidths_n = [3.5 if n in top_brokers else 1.5 for n in G.nodes()]

    fig, ax = plt.subplots(figsize=(11, 8))
    nx.draw_networkx_edges(G, pos, alpha=0.25, edge_color='#888', ax=ax)
    nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color=colors,
                           cmap='Set2', alpha=0.92,
                           edgecolors=edgecolors, linewidths=linewidths_n, ax=ax)
    label_nodes = set(top5) | set(top_brokers)
    nx.draw_networkx_labels(G, pos, labels={n: n for n in label_nodes},
                            font_size=10, font_weight='bold', ax=ax)

    out_dir = os.path.dirname(__file__)
    out_png = os.path.join(out_dir, 'karate_publikacija_test.png')
    out_svg = os.path.join(out_dir, 'karate_publikacija_test.svg')
    plt.tight_layout()
    plt.savefig(out_png, dpi=300, bbox_inches='tight')
    plt.savefig(out_svg, bbox_inches='tight')
    plt.close(fig)
    assert os.path.exists(out_png) and os.path.getsize(out_png) > 1000
    assert os.path.exists(out_svg) and os.path.getsize(out_svg) > 1000
    os.remove(out_png)
    os.remove(out_svg)

    for pal in ['jet', 'viridis', 'cividis', 'Set2']:
        plt.figure(figsize=(4, 3))
        nx.draw_networkx_edges(G, pos, alpha=0.25)
        nx.draw_networkx_nodes(G, pos, node_size=sizes,
                               node_color=colors, cmap=pal, alpha=0.9,
                               edgecolors='white', linewidths=1.2)
        plt.close()

    G_export = G.copy()
    for n in G_export.nodes():
        G_export.nodes[n]['degree'] = deg[n]
        G_export.nodes[n]['betweenness'] = round(bet_g[n], 4)
        G_export.nodes[n]['community'] = node2comm[n]
        G_export.nodes[n]['label'] = f'Node_{n}'
    gexf = os.path.join(out_dir, 'karate_test.gexf')
    graphml = os.path.join(out_dir, 'karate_test.graphml')
    nx.write_gexf(G_export, gexf)
    nx.write_graphml(G_export, graphml)
    assert os.path.exists(gexf) and os.path.getsize(gexf) > 500
    assert os.path.exists(graphml) and os.path.getsize(graphml) > 500

    G_re = nx.read_gexf(gexf)
    assert G_re.number_of_nodes() == G.number_of_nodes()
    assert 'degree' in next(iter(G_re.nodes(data=True)))[1]

    os.remove(gexf)
    os.remove(graphml)

    print('OK: svih 15 sekcija bilježnice 07 prolazi test')


if __name__ == '__main__':
    test_notebook_07_full_flow()
