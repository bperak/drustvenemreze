# 6. Analiza zajednica u društvenim mrežama

Jedno od najintuitivnijih pitanja kada pogledamo mrežu jest: **ima li u njoj grupe**? Ljudi se prirodno grupiraju — po interesima, prijateljstvima, institucijama; na platformama se pojavljuju klasteri korisnika koji međusobno više komuniciraju. **Detekcija zajednica** (community detection) jest skup algoritama i mjera kojima nastojimo **automatski** pronaći takve grupe u grafu: podskupove čvorova koji su gusto povezani unutar skupa, a rjeđe prema van. Rezultat može biti particija mreže u zajednice ili hijerarhija grupa. Ovo poglavlje uvodi koncept zajednice, glavne metode (uključujući Louvain i modularnost) i način na koji ih tumačimo u društvenom i kulturnom kontekstu.

---

## Teorijski koncept

**Zajednica** (u mrežnom smislu) nije nužno ono što sudionici nazivaju „zajednica”; to je **strukturalna** grupa: skup čvorova s **više veza unutar skupa** nego prema ostalim čvorovima. Takve grupe često odgovaraju društvenim ili kulturnim segmentima — npr. grupe interesa na društvenim mrežama, odjeli u organizaciji, klike prijatelja. **Detekcija zajednica** omogućuje da ih identificiramo bez unaprijed zadanih kategorija: algoritam „traži” particiju koja maksimizira neku mjeru kohezije (npr. modularnost). Time možemo otkriti latentnu strukturu mreže, usporediti je s poznatim grupama ili pratiti kako se zajednice mijenjaju u vremenu.

---

## Definicije

- **Zajednica (community)**: Skup čvorova takav da je **gustoća veza unutar skupa** veća (ili značajno veća) od gustoće veza prema ostalim čvorovima. Formalno se često definira putem **modularnosti** ili sličnih mjera.
- **Modularnost (modularity)**: Mjera kvalitete particije: uspoređuje broj veza unutar grupa s očekivanim brojem u **nasumičnoj** mreži istih stupnjeva čvorova. Viša modularnost znači da su grupe „izraženije”. Koristi se i kao ciljna funkcija koju algoritmi maksimiziraju.
- **Algoritam Louvain**: Heuristički algoritam za **maksimizaciju modularnosti**. Brz je i često korišten; radi u dva koraka (lokalno premještanje čvorova, zatim agregacija grupa). Daje jednu particiju; moguće je izgraditi hijerarhiju ponavljanjem.
- **Label propagation, spectral clustering**: Alternative ili nadopune; svaka ima prednosti i mane ovisno o veličini i tipu mreže.

---

## Ključni istraživači

- **Lei Tang i Huan Liu** (ur.) u knjizi *Community Detection and Mining in Social Media* daju pregled metoda detekcije zajednica u kontekstu društvenih medija i velikih grafova.
- **Borgatti, Everett i Johnson** u *Analyzing Social Networks* raspravljaju o interpretaciji grupa u SNA-u i o povezivanju strukturalnih klastera s društvenim kategorijama.
- **Blondel et al. (2008)** u članku „Fast unfolding of communities in large networks” (*Journal of Statistical Mechanics*) opisuju Louvain algoritam koji je postao jedan od standardnih alata.

---

## Recentna literatura

- **Fortunato, S. (2010).** Community detection in graphs. *Physics Reports*. Opsežan pregled metoda i mjera.
- **Blondel et al. (2008).** Fast unfolding of communities (Louvain). *Journal of Statistical Mechanics*.
- Korisno je tražiti radove od cca. 2015. nadalje o detekciji zajednica u **online mrežama** (skalabilnost, dinamičke mreže, usporedba algoritama).

---

## Problemi

- **Odabir broja ili razine zajednica**: Neki algoritmi zahtijevaju unaprijed broj grupa (npr. k-means na embeddingu); drugi (Louvain) ga ne. Hijerarhijski pristupi daju više razina; treba odlučiti koju razinu tumačiti.
- **Stabilnost**: Različiti algoritmi ili različite randomizacije mogu dati različite particije. Korisno je provjeriti koliko su rezultati stabilni (npr. ponovljenim pokretanjem) i usporediti s kontekstom.
- **Interpretacija**: Pronađene grupe treba **interpretirati** — što ih čini kohezivnima? Odgovaraju li poznatim kategorijama (npr. institucije, interesi)? Bez interpretacije ostaje samo tehnički output.

---

## Primjer u stvarnom svijetu

- **Grupe interesa na društvenim mrežama**: korisnici koji se međusobno više prate ili komentiraju često padaju u iste zajednice; mogu odgovarati tematskim ili identitetskim skupinama.
- **Klike u organizacijama**: detekcija neformalnih grupa prema tome tko s kime surađuje ili komunicira; usporedba s formalnom strukturom (odjeli, timovi).
- **Koautorstvo ili citiranje**: zajednice autora ili članaka po poljima ili školama mišljenja.

Metode uključuju Louvain, label propagation, spectral clustering; izbor ovisi o veličini grafa i o tome želimo li hijerarhiju ili jednu particiju.

---

## Alati

- **NetworkX**: U novijim verzijama `nx.community.louvain_communities` (ako je dostupno); inače se koristi **python-louvain** paket (`community_louvain.best_partition(G)`).
- **Gephi**: Modul za Modularity; pokreće se algoritam i dobiva se particija te vizualizacija po boji zajednica.

U bilježnici uz ovo poglavlje dan je minimalan primjer; za velike mreže preporučuje se provjera dokumentacije i eventualno korištenje igraph ili drugih biblioteka za brže izvršavanje.

---

Vidi primjer: [06_detekcija_zajednica.ipynb](../code/06_detekcija_zajednica.ipynb)
