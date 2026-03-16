# Istraživanja društvenih mreža (Social Network Analysis)

**Teaching materials for the course *Istraživanja društvenih mreža* (INP)** — theory, code, and examples for Social Network Analysis (SNA) in Croatian. Content covers graph theory, centrality, community detection, visualization, diffusion, ethics, and applications (marketing, policy, Twitter/X).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Contents

- [Overview](#overview)
- [Repository structure](#repository-structure)
- [Content (theory)](#content-theory)
- [Code (notebooks)](#code-notebooks)
- [Examples and data](#examples-and-data)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Learning outcomes mapping](#learning-outcomes-mapping)
- [License and citation](#license-and-citation)

---

## Overview

This repository contains:

- **14 theory chapters** (Markdown) in `content/` — definitions, key researchers, literature, methods, and interpretation.
- **14 Jupyter notebooks** in `code/` — executable examples using **NetworkX**, **pandas**, **matplotlib**, and **plotly**.
- **Examples** in `examples/` — extended use cases (e.g. *Les Misérables* character co-occurrence for cultural studies) and sample data.

Each chapter links to its notebook and vice versa, so you can read theory and run code side by side.

---

## Repository structure

```
.
├── content/                    # Theory (14 .md files)
│   ├── 01_uvod_drustvene_mreze_teorija_grafova.md
│   ├── 02_prikupljanje_obrada_podataka.md
│   ├── 03_mjere_mrezne_strukture.md
│   ├── 04_socijalni_kapital.md
│   ├── 05_mreze_usmjerene_tezine.md
│   ├── 06_analiza_zajednica.md
│   ├── 07_vizualizacija_mreza.md
│   ├── 08_difuzija_inovacija_utjecaj.md
│   ├── 09_dinamika_mreza_vrijeme.md
│   ├── 10_online_drustvene_mreze.md
│   ├── 11_sna_marketing.md
│   ├── 12_drustvene_mreze_politika.md
│   ├── 13_kriticko_razmisljanje_ogranicenja.md
│   └── 14_analiza_twittera_alati.md
├── code/                       # Jupyter notebooks (14 .ipynb)
│   ├── 01_uvod_grafovi_networkx.ipynb
│   ├── 02_prikupljanje_podataka_ankete.ipynb
│   ├── 03_mjere_centralnosti_klasteriranje.ipynb
│   ├── 04_socijalni_kapital_primjer.ipynb
│   ├── 05_usmjerene_tezinske_mreze.ipynb
│   ├── 06_detekcija_zajednica.ipynb
│   ├── 07_vizualizacija_layouti.ipynb
│   ├── 08_difuzija_utjecaj_primjer.ipynb
│   ├── 09_dinamika_mreza.ipynb
│   ├── 10_online_mreze_primjer.ipynb
│   ├── 11_marketing_primjer.ipynb
│   ├── 12_politika_primjer.ipynb
│   ├── 13_etika_anonimizacija.ipynb
│   └── 14_twitter_x_primjer.ipynb
├── examples/                   # Extended examples and data
│   ├── data/                   # CSV data (e.g. Les Misérables)
│   │   ├── les_miserables_edges.csv
│   │   └── les_miserables_nodes.csv
│   ├── kulturologija_mreza_primjer.ipynb
│   └── README.md
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Content (theory)

| # | Chapter | File |
|---|--------|------|
| 1 | Uvod u društvene mreže i teoriju grafova | [01_uvod_drustvene_mreze_teorija_grafova.md](content/01_uvod_drustvene_mreze_teorija_grafova.md) |
| 2 | Prikupljanje i obrada podataka | [02_prikupljanje_obrada_podataka.md](content/02_prikupljanje_obrada_podataka.md) |
| 3 | Mjere mrežne strukture | [03_mjere_mrezne_strukture.md](content/03_mjere_mrezne_strukture.md) |
| 4 | Socijalni kapital | [04_socijalni_kapital.md](content/04_socijalni_kapital.md) |
| 5 | Mreže usmjerene i s težinama | [05_mreze_usmjerene_tezine.md](content/05_mreze_usmjerene_tezine.md) |
| 6 | Analiza zajednica | [06_analiza_zajednica.md](content/06_analiza_zajednica.md) |
| 7 | Vizualizacija mreža | [07_vizualizacija_mreza.md](content/07_vizualizacija_mreza.md) |
| 8 | Difuzija inovacija i utjecaj | [08_difuzija_inovacija_utjecaj.md](content/08_difuzija_inovacija_utjecaj.md) |
| 9 | Dinamika mreža | [09_dinamika_mreza_vrijeme.md](content/09_dinamika_mreza_vrijeme.md) |
| 10 | Online društvene mreže | [10_online_drustvene_mreze.md](content/10_online_drustvene_mreze.md) |
| 11 | SNA u marketingu | [11_sna_marketing.md](content/11_sna_marketing.md) |
| 12 | Društvene mreže i politika | [12_drustvene_mreze_politika.md](content/12_drustvene_mreze_politika.md) |
| 13 | Kritičko razmišljanje i ograničenja | [13_kriticko_razmisljanje_ogranicenja.md](content/13_kriticko_razmisljanje_ogranicenja.md) |
| 14 | Analiza Twittera/X | [14_analiza_twittera_alati.md](content/14_analiza_twittera_alati.md) |

---

## Code (notebooks)

Each chapter has a matching notebook in `code/`:

| # | Topic | Notebook |
|---|--------|----------|
| 1 | Grafovi i NetworkX | [01_uvod_grafovi_networkx.ipynb](code/01_uvod_grafovi_networkx.ipynb) |
| 2 | Prikupljanje podataka, ankete | [02_prikupljanje_podataka_ankete.ipynb](code/02_prikupljanje_podataka_ankete.ipynb) |
| 3 | Mjere centralnosti i klasteriranje | [03_mjere_centralnosti_klasteriranje.ipynb](code/03_mjere_centralnosti_klasteriranje.ipynb) |
| 4 | Socijalni kapital | [04_socijalni_kapital_primjer.ipynb](code/04_socijalni_kapital_primjer.ipynb) |
| 5 | Usmjerene i težinske mreže | [05_usmjerene_tezinske_mreze.ipynb](code/05_usmjerene_tezinske_mreze.ipynb) |
| 6 | Detekcija zajednica | [06_detekcija_zajednica.ipynb](code/06_detekcija_zajednica.ipynb) |
| 7 | Vizualizacija i layouti | [07_vizualizacija_layouti.ipynb](code/07_vizualizacija_layouti.ipynb) |
| 8 | Difuzija i utjecaj | [08_difuzija_utjecaj_primjer.ipynb](code/08_difuzija_utjecaj_primjer.ipynb) |
| 9 | Dinamika mreža | [09_dinamika_mreza.ipynb](code/09_dinamika_mreza.ipynb) |
| 10 | Online mreže | [10_online_mreze_primjer.ipynb](code/10_online_mreze_primjer.ipynb) |
| 11 | Marketing | [11_marketing_primjer.ipynb](code/11_marketing_primjer.ipynb) |
| 12 | Politika | [12_politika_primjer.ipynb](code/12_politika_primjer.ipynb) |
| 13 | Etika i anonimizacija | [13_etika_anonimizacija.ipynb](code/13_etika_anonimizacija.ipynb) |
| 14 | Twitter/X | [14_twitter_x_primjer.ipynb](code/14_twitter_x_primjer.ipynb) |

---

## Examples and data

- **`examples/kulturologija_mreza_primjer.ipynb`** — Cultural studies example: character co-occurrence network from *Les Misérables* (Victor Hugo). Uses degree and betweenness centrality, interprets “bridges” and narrative power. Data in `examples/data/`.
- **`examples/data/`** — `les_miserables_edges.csv` and `les_miserables_nodes.csv`. If missing, the notebook can generate them from NetworkX’s built-in dataset.

See [examples/README.md](examples/README.md) for details.

---

## Installation

### Requirements

- **Python 3.9+** (3.10 or 3.11 recommended)
- pip

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/bperak/drustvenemreze.git
   cd drustvenemreze
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) For **community detection** (Chapter 6):

   ```bash
   pip install python-louvain
   ```

5. (Optional) For **Twitter/X API** examples (Chapter 14) — use your own keys and comply with ToS:

   ```bash
   pip install tweepy
   ```
   Set credentials via environment variables or `.env` (e.g. `TWITTER_BEARER_TOKEN`); never commit secrets.

### Run Jupyter

```bash
jupyter notebook
# or
jupyter lab
```

Open notebooks from `code/` or `examples/`. Run cells in order; paths assume you start from the project root.

---

## Quick start

1. Install as above.
2. Open [code/01_uvod_grafovi_networkx.ipynb](code/01_uvod_grafovi_networkx.ipynb) and run all cells to build and draw a small graph (triangle + bridge).
3. Open [examples/kulturologija_mreza_primjer.ipynb](examples/kulturologija_mreza_primjer.ipynb) to analyse the *Les Misérables* network with pandas, NetworkX, and plotly/matplotlib.

---

## Learning outcomes mapping

- **Network theory (outcomes 1–3):** Chapters 1, 3, 5, 6, 8.
- **Data collection and processing (outcomes 2–4):** Chapters 2, 10, 14.
- **Programming and tools (outcome 5):** All notebooks in `code/` (Python, NetworkX, pandas, matplotlib, plotly).

---

## License and citation

- **License:** [MIT](LICENSE).  
- **Author:** Benedikt Perak.  
- **Course:** INP Istraživanja društvenih mreža (2025/26).

If you use this material in teaching or research, please cite the repository:

```text
Perak, B. (2026). Istraživanja društvenih mreža — nastavni materijal. GitHub. https://github.com/bperak/drustvenemreze
```
