# 7. Vizualizacija društvenih mreža i njihovih svojstava

Brojke i tablice opisuju mrežu, ali **vizualizacija** često omogućuje da **vidimo** strukturu: tko je u sredini, gdje su grupe, koji čvorovi povezuju različite dijelove. Dobra vizualizacija služi istraživaču za pregled i provjeru, a publici za **komunikaciju** rezultata. No vizualizacija nije neutralna: odabir **layouta** (kako pozicionirati čvorove), **boja**, **veličine** i **debljine bridova** utječe na to što naglašavamo i kako se graf čita. Ovo poglavlje uvodi osnove vizualizacije mreža: što je layout, kako prenijeti atribute (centralnost, zajednica) u vizualne varijable i koje alate koristiti, uz napomenu o ograničenjima i etici prikaza.

---

## Teorijski koncept

Vizualizacija mreža služi nekoliko ciljeva: **(1) pregled** — brzo uočiti opću strukturu, outlier čvorove, očite klastere; **(2) provjera** — je li particija u zajednice smislena, ima li artefakata u podacima; **(3) komunikacija** — predstaviti rezultate drugima (čitateljima, sudionicima). Da bi vizualizacija bila informativna, **layout** (pozicija čvorova) i **atributi** (veličina, boja, debljina bridova) moraju prenositi informaciju. Force-directed layouti („spring”) grupirat će gusto povezane čvorove; veličina čvora može odgovarati centralnosti; boja — pripadnosti zajednici. Loše odabrane opcije mogu dovesti do zbrke ili pristrane slike. Stoga je važno znati osnove: što koji layout radi i kako čitati (i kritizirati) vizualni prikaz.

---

## Definicije

- **Layout**: Algoritam koji **pozicionira čvorove** u 2D (ili 3D) prostoru tako da graf postane čitljiv. **Force-directed** (spring) layouti privlače povezane čvorove i odbijaju nepovezane; rezultat često „grupa” gusto povezane čvorove. **Circular** layout raspoređuje čvorove u krug — jednostavan, ali rijetko otkriva strukturu. **Hierarchical** layout raspoređuje čvorove u slojeve prema razini (npr. stabla). Izbor layouta ovisi o tipu mreže i o tome što želimo naglasiti.
- **Atributi vizualizacije**: Način na koji **prenosimo podatke u vizualne varijable**. **Veličina čvora** često odgovara stupnju ili drugoj mjeri centralnosti; **boja** — pripadnosti zajednici ili kategoriji; **debljina brida** — težini. Konzistentna legenda i naslov omogućuju čitatelju da interpretira prikaz.

---

## Ključni istraživači i resursi

- **Tamara Munzner** u knjizi *Visualization Analysis and Design* daje sustavan pregled načela vizualizacije: kada koji prikaz, kako izbjeći zloupotrebu i kako evaluirati vizualizacije.
- **Peter Eades** i **Kozo Sugiyama** ključni su za razvoj **force-directed** i **hijerarhijskih** layout algoritama koji se i danas koriste u alatima.
- **Mike Bostock** (D3.js) i **Jeffrey Heer** (Vega, Prefuse) utjecajni su u području **interaktivne** vizualizacije na webu; D3.js često korišten za mrežne i graf prikaze.
- **Edward Tufte** u knjigama o vizualnom prikazu podataka postavlja načela jasnoće, poštenja prema podacima i izbjegavanja „chartjunk” — korisno i za mrežne vizualizacije.

---

## Recentna literatura

- **Majeed, S., Uzair, M., Qamar, U. & Farooq, A. (2020).** Social Network Analysis Visualization Tools: A Comparative Review. IEEE. Usporedba alata i preporuke.
- **Lima, M.** *Visual Complexity: Mapping Patterns of Information* — pregled složenih mrežnih i informacijskih vizualizacija.
- Dokumentacija i tutoriali za **Gephi**, **Cytoscape**, **Graphviz** i **NetworkX** (nx.draw, layouti) ažuriraju se; korisno koristiti najnovije verzije za primjere i mogućnosti.

---

## Problemi

- **Vizualna zbrka**: Na **velikim mrežama** (tisuće čvorova) čak i dobri layouti postaju nečitljivi — preklapanje čvorova i bridova. Rješenja uključuju filtriranje (prikazati samo dio), povećanje, interaktivnost (zum, pomicanje) ili agregaciju (prikazati zajednice kao super-čvorove).
- **Pristranost**: Odabir layouta i atributa može **naglasiti** neke aspekte a druge sakriti. Npr. force-directed može pretjerano naglasiti klastere ako ih interpretator već očekuje. Treba biti transparentan u izboru i u ograničenjima prikaza.
- **Erika i anonimizacija**: Pri prikazu stvarnih mreža (npr. korisnici platformi) treba paziti na to ne otkrivamo li identitete na način koji krši etiku ili GDPR; pseudonimizacija ili prikaz samo agregiranih struktura ponekad su nužni.

---

## Alati

- **Gephi**: Besplatan, moćan za interaktivnu vizualizaciju; mnogi layouti, filtriranje, boje po atributima. [gephi.org](https://gephi.org/)
- **Cytoscape**: Popularan u biologiji i za složene mreže; podrška za stilove i aplikacije. [cytoscape.org](http://www.cytoscape.org/)
- **Graphviz**: Alat za crtanje grafova iz opisa; koristan za manje grafove i automatizaciju. [graphviz.org](https://www.graphviz.org/)
- **Python**: **NetworkX** s `nx.draw`, `nx.draw_networkx` i layoutima (`spring_layout`, `circular_layout`, itd.) te **matplotlib** za izlaz; za interaktivne web prikaze često se koristi **D3.js** ili Python wrapperi (npr. pyvis).

U bilježnici uz ovo poglavlje dan je primjer force-directed layouta u NetworkX-u; za naprednije vizualizacije preporučuje se Gephi ili interaktivne biblioteke.

---

Vidi primjer: [07_vizualizacija_layouti.ipynb](../code/07_vizualizacija_layouti.ipynb)
