# Prompts za poboljšanja: sadržaj (Markdown) i kod (Jupyter)

Ovaj dokument izvlači **prompte i obrasce** korištene za poboljšanje poglavlja 3 (mjere mrežne strukture) kako bi se **ista poboljšanja primijenila na sva poglavlja** — i na `content/*.md` i na `code/*.ipynb`. Koristi ove točke kao checklistu ili kao upute (prompte) pri uređivanju ostalih poglavlja.

**Referentno poglavlje:** [content/03_mjere_mrezne_strukture.md](content/03_mjere_mrezne_strukture.md) + [code/03_mjere_centralnosti_klasteriranje.ipynb](code/03_mjere_centralnosti_klasteriranje.ipynb).

---

## 1. Sadržaj (Markdown datoteke u `content/`)

### 1.1 Ilustracija na početku poglavlja

- **Prompt:** Na vrhu poglavlja, odmah ispod uvodnog odlomka, dodaj **jednu Mermaid ilustraciju** koja prikazuje glavni primjer ili strukturu koju poglavlje obrađuje.
- **Što uključiti:**
  - Kratak uvodni red (**Ilustracija:** ...) koji objašnjava što dijagram prikazuje.
  - Blok ```mermaid``` s grafikom (npr. `graph LR` ili `graph TB` za graf mreže; `flowchart` za odluke/korake).
  - Jedna-dvije rečenice ispod dijagrama (kurziv) koje povezuju dijagram s teorijom.
  - Ako postoji povezani notebook, dodaj link: *Isti primjer u [bilježnici](../code/XX_ime.ipynb)...*

**Primjer (pogl. 3):** Graf s čvorovima Ana, Bruno, Carla, David, Eva — trokut + most; caption objašnjava betweenness i klasteriranje.

---

### 1.2 Ilustracije kroz cijelo poglavlje

- **Prompt:** Nakon svake ključne sekcije (npr. Definicije, Problemi, Temeljne mjere, Primjeri) dodaj **kratku Mermaid ilustraciju** koja vizualizira pojam iz te sekcije.
- **Gdje dodati:**
  - Nakon **Definicije** — dijagram koji ilustrira 1–2 ključna pojma (npr. degree vs betweenness).
  - Nakon **Problemi** — flowchart: Pitanje? → odabir mjere (ako je primjenjivo).
  - Nakon **Temeljne metode / mjere** — isti primjer grafa kao u kodu ili shema „ista mreža, različite mjere”.
  - Nakon **Temeljne mjere klasteriranja** (ili analognog) — dijagram visoko vs nisko klasteriranje (trokut vs lanac).
  - Nakon **Primjeri (apstraktna uporaba)** — apstraktna mreža s dvije grupe i mostom.
  - Nakon **Primjeri iz filmova/serija** — shema „most” (npr. Nick Fury između SHIELD i Avengers).
  - Nakon **Primjeri iz umjetnosti/književnosti** — shema (npr. Gertrude Stein između pisaca i umjetnika).
  - Nakon **Nedavni primjeri** — shema (npr. bridge igrač između Discord grupa).
- **Format:** Za svaku ilustraciju: *Ilustracija — [kratki opis].* → blok ```mermaid``` → *[Caption u kurzivu].*

---

### 1.3 Povezivanje sadržaj → kod

- **Prompt:** U svakom poglavlju eksplicitno poveži tekst s odgovarajućim notebookom.
- **Gdje:**
  - U odlomku **Definicije:** na kraju dodaj rečenicu tipa: **Korak-po-korak izračun** nalazi se u [XX_ime.ipynb](../code/XX_ime.ipynb).
  - U odlomku **Temeljne mjere / metode:** dodaj **U kodu:** u [bilježnica](link), Korak X — ...
  - U **Primjerima i interpretaciji:** dodaj rečenicu da se u bilježnici radi tablica i crtež (Korak 8, 9 ili analogno).
  - Na **kraju dokumenta** dodaj tablicu **Povezivanje sadržaj ↔ kod** s 4–5 redaka: Što tražite | Gdje (ovaj dokument / bilježnica, koraci).

**Primjer tablice:**
| Što tražite | Gdje |
|-------------|------|
| Definicije mjera | Ovaj dokument, odlomak **Definicije** |
| Korak-po-korak izračun u Pythonu | [XX_ime.ipynb](../code/XX_ime.ipynb) |
| Konceptualni primjeri | Ovaj dokument, **Primjeri i interpretacija** |
| Tablica mjera + vizualizacija | Bilježnica, Korak 8 i 9 |

---

### 1.4 Primjeri: više, recentniji, zabavniji

- **Prompt:** Proširi sekciju primjera tako da uključuje:
  - **Više primjera** za svaki koncept (degree, betweenness, closeness, eigenvector, klasteriranje, gustoća — ili analogne koncepte poglavlja).
  - **Recentnije primjere** (filmovi, serije, glazba, gaming, streaming od ~2015. nadalje).
  - **Zabavne / relatable primjere** s kojima se studenti mogu poistovjetiti: filmovi (MCU, Harry Potter, Game of Thrones, The Wire), umjetnici i pisci (Gertrude Stein, Bloomsbury, impresionisti, galeristi), glazba (hip-hop crewovi, producenti), gaming (Among Us, Discord, Twitch/YouTube collabi).
- **Struktura:** Za svaku mjeru ili koncept navedi 1–3 konkretna primjera (ime lika/serije/umjetnika + kratko zašto je to dobar primjer).

---

## 2. Kod (Jupyter bilježnice u `code/`)

### 2.1 Struktura: korak po korak, temeljito, ilustrativno

- **Prompt:** Organiziraj notebook tako da svaki glavni koncept ima **svoj korak** (Korak 1, 2, 3, …). Za svaki korak:
  - **Markdown ćelija** na početku: naslov `## Korak N: [Naziv]`, zatim **Što mjerimo / Što radimo** (1–2 rečenice), **Pitanje na koje odgovara** (ako je primjenjivo), te *(Link na sadržaj: Definicija / Primjeri u [pogl. X](link)).*
  - **Code ćelija:** samo ono što pripada tom koraku (izgradnja grafa, jedna mjera, jedna tablica, jedan crtež).
  - **Ispis / vizualizacija:** rezultat koji student vidi (print, tablica, graf).
- **Korak 1:** Uvoz biblioteka + izgradnja primjer grafa. Definirati **čitljiva imena** za čvorove (npr. Ana, Bruno, Carla, David, Eva) i **zajednički layout** (`pos = nx.spring_layout(G, seed=42)`) za sve kasnije crteže.

---

### 2.2 Uvijek crtaj graf koji ilustrira teoriju

- **Prompt:** U svakom koraku gdje je to smisleno **nacrtaj graf** (matplotlib + NetworkX) tako da vizualizacija **ilustrira teoriju** tog koraka.
- **Gdje crtati:**
  - **Korak 1 (izgradnja grafa):** crtež osnovne strukture (npr. trokut + most) s jednakim veličinama čvorova; naslov objašnjava strukturu.
  - **Korak za svaku mjeru (degree, betweenness, closeness, eigenvector, clustering):** crtež s **veličinom čvora proporcionalnom toj mjeri** i naslovom koji objašnjava mjeru (npr. „Degree centralnost: veličina ∝ broj direktnih veza”).
  - **Korak za gustoću (ili globalnu mjeru):** crtež s fiksnom veličinom čvorova, naslov uključuje vrijednost gustoće.
  - **Završni korak (pregled):** jedan **multi-panel** crtež (npr. 2×3) gdje svaki panel prikazuje isti graf s veličinom čvora = druga mjera (degree, betweenness, closeness, eigenvector, clustering, gustoća).
- **Konzistentno:** Koristiti isti `pos` u svim crtežima; razlikovati panele bojom ili naslovom.

---

### 2.3 Povezivanje kod → sadržaj

- **Prompt:** U bilježnici na više mjesta dodaj linkove natrag na markdown poglavlje.
- **Gdje:**
  - **Prva markdown ćelija:** osim linka „Poglavlje: [Naslov](link)” dodaj 2 bullet točke: **Definicije** u [sadržaj — Definicije](link#definicije), **Konceptualni primjeri** u [sadržaj — Primjeri](link#primjeri-i-interpretacija).
  - **Svaki Korak (markdown):** na kraju odlomka u zagradi *(Definicija: [pogl. X — Naziv mjere](link). Primjeri u sadržaju: ...).*
  - **Zaključak:** rečenica **Sadržaj ↔ kod** s linkom na poglavlje i na tablicu „Povezivanje sadržaj ↔ kod”.

---

### 2.4 Jedan konkretan, čitljiv primjer

- **Prompt:** Koristi **jedan mali, konkretan primjer** (npr. 5–7 čvorova s imenima) koji je isti u cijelom notebooku i koji odgovara primjeru u sadržaju (filmovi, umjetnici, „trokut + most”). Izbjegavaj anonimne brojeve (1, 2, 3) u ispisu — koristi `names` ili labele na grafu.

---

## 3. Kratki checklist po poglavlju

Pri primjeni na novo poglavlje (npr. 01, 02, 04, … 14):

**Content (XX_ime.md):**
- [ ] Ilustracija na početku (Mermaid + caption + link na notebook).
- [ ] Ilustracije nakon: Definicije, Problemi, Temeljne metode, Klasteriranje (ako postoji), Primjeri (apstraktna, filmovi/serije, umjetnost, nedavni).
- [ ] U tekstu: „U kodu” / „Korak-po-korak u bilježnici” s linkom na odgovarajući .ipynb i korake.
- [ ] Tablica „Povezivanje sadržaj ↔ kod” na kraju.
- [ ] Primjeri: više, recentniji, zabavniji (filmovi, serije, umjetnici, glazba, gaming) gdje je primjenjivo.

**Code (XX_ime.ipynb):**
- [ ] Naslovna ćelija: link na poglavlje + linkovi na Definicije i Primjere u sadržaju.
- [ ] Koraci: svaki koncept = jedan Korak (markdown „Što mjerimo” + code + ispis/crtež).
- [ ] U svakom relevantnom koraku: crtež grafa (veličina čvora = mjera ili struktura).
- [ ] Završni korak: tablica svih mjera + multi-panel vizualizacija (ako ima više mjera).
- [ ] U svakom koraku: kratki link natrag na sadržaj (definicija / primjeri).
- [ ] Zaključak: „Sadržaj ↔ kod” + link na tablicu u sadržaju.
- [ ] Čitljiva imena čvorova i zajednički `pos` za sve crteže.

---

## 4. Mapiranje poglavlja (content ↔ code)

| Pogl. | Content (.md) | Code (.ipynb) |
|-------|----------------|---------------|
| 1 | 01_uvod_drustvene_mreze_teorija_grafova.md | 01_uvod_grafovi_networkx.ipynb |
| 2 | 02_prikupljanje_obrada_podataka.md | 02_prikupljanje_podataka_ankete.ipynb |
| 3 | 03_mjere_mrezne_strukture.md | 03_mjere_centralnosti_klasteriranje.ipynb |
| 4 | 04_socijalni_kapital.md | 04_socijalni_kapital_primjer.ipynb |
| 5 | 05_mreze_usmjerene_tezine.md | 05_usmjerene_tezinske_mreze.ipynb |
| 6 | 06_analiza_zajednica.md | 06_detekcija_zajednica.ipynb |
| 7 | 07_vizualizacija_mreza.md | 07_vizualizacija_layouti.ipynb |
| 8 | 08_difuzija_inovacija_utjecaj.md | 08_difuzija_utjecaj_primjer.ipynb |
| 9 | 09_dinamika_mreza_vrijeme.md | 09_dinamika_mreza.ipynb |
| 10 | 10_online_drustvene_mreze.md | 10_online_mreze_primjer.ipynb |
| 11 | 11_sna_marketing.md | 11_marketing_primjer.ipynb |
| 12 | 12_drustvene_mreze_politika.md | 12_politika_primjer.ipynb |
| 13 | 13_kriticko_razmisljanje_ogranicenja.md | 13_etika_anonimizacija.ipynb |
| 14 | 14_analiza_twittera_alati.md | 14_twitter_x_primjer.ipynb |

Primjeni gornje prompte na svaki par (content, code) prema strukturi tog poglavlja; neka sekcija (npr. „Temeljne mjere klasteriranja”) postoji samo u poglavljima gdje je tema relevantna.
