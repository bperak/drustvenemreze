# Primjeri za Istraživanje društvenih mreža

Ova mapa sadrži **detaljne, dokumentirane primjere** koji ilustriraju koncepte iz sadržaja kolegija.

## Struktura

- **`data/`** — podaci korišteni u primjerima (preuzeti ili generirani u bilježnicama).
- **`kulturologija_mreza_primjer.ipynb`** — praktični primjer za sekciju [Kulturologija i komunikacijski/društveni problemi](../content/01_uvod_drustvene_mreze_teorija_grafova.md#kulturologija-i-komunikacijskidruštveni-problemi) (pogl. 1).

## Kulturologija: mreža likova (Les Misérables)

Bilježnica `kulturologija_mreza_primjer.ipynb`:

- Učitava mrežu **supojavljivanja likova** iz romana *Les Misérables* (Victor Hugo) iz `data/les_miserables_edges.csv` i `data/les_miserables_nodes.csv`.
- Ako datoteke ne postoje, generira ih iz ugrađene NetworkX mreže i sprema u `data/`.
- Računa mjere centralnosti (stupanj, betweenness) i prikazuje ih u **pandas** tablicama.
- Vizualizira mrežu interaktivno (**plotly**) ili statično (**matplotlib** ako plotly nije instaliran).
- Interpretira rezultate u smislu kulturologije: položaj u mreži, „mostovi” između grupa, identitet i moć.

**Ovisnosti:** `pandas`, `networkx`, `matplotlib`; opcionalno `plotly` za interaktivni graf (`pip install plotly`).

## AI uz ovaj primjer

Kao i u teorijskim poglavljima, generativni AI može pomoći u **nacrtu interpretacije** likova i mostova — uz iste uvjete: ne slati osjetljive podatke bez etike, provjeriti citate i brojke. Vidi odjeljak **„AI u ovom poglavlju”** u [poglavlju 1](../content/01_uvod_drustvene_mreze_teorija_grafova.md) i cjelinu [poglavlja 15](../content/15_ai_gemini_u_sna.md).
