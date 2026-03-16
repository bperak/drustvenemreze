# 5. Mreže usmjerene i mreže s težinama

Do sada smo uglavnom razmatrali **neusmjerene** grafove: veza između A i B bila je jedna, bez smjera. U mnogim stvarnim situacijama to nije dovoljno. Na društvenim mrežama **A prati B** nije isto što **B prati A**; u mreži citiranja članak A citira B, a ne obrnuto. Takve veze zahtijevaju **usmjereni graf**. Drugi korak prema realnosti jest **težine**: ne sve veze su jednake — intenzitet komunikacije, broj poruka, snaga odnosa mogu varirati. **Težinski graf** na svaki brid stavlja broj (ili drugi atribut). Ovo poglavlje uvodi usmjerene i težinske mreže: zašto su važne, kako ih formalno opisati i koje mjere i alate koristiti.

---

## Teorijski koncept

**Usmjerene mreže** odražavaju **asimetriju** odnosa: tko koga prati, tko koga citira, tko šalje poruku kome. Smjer je bitan za pitanja o **protoku** (informacije, utjecaj, resursi) i za **uloge** (tko je „izvor”, tko „primatelj”). **Težinske mreže** dopuštaju da razlikujemo **jačinu** veze: ne samo postoji li veza, nego koliko je intenzivna. Time možemo bolje modelirati stvarnost — npr. mrežu u kojoj neki parovi komuniciraju deset puta više od drugih — i preciznije analizirati (npr. težinski stupanj umjesto običnog broja veza). Oboje proširuje analitički okvir i približava ga primjenama u komunikologiji, ekonomiji i istraživanju online platformi.

---

## Definicije

- **Usmjereni graf (directed graph)**: Graf u kojem svaki brid ima **smjer**: od jednog čvora prema drugome. Označavamo ga parom (izvor, cilj). **In-degree** čvora je broj bridova koji *ulaze* u taj čvor; **out-degree** je broj bridova koji *izlaze*. U kontekstu sljedbenika: in-degree = broj sljedbenika, out-degree = broj praćenja.
- **Težinski graf**: Na svakom bridu (usmjerenom ili ne) definiran je atribut **težina** (najčešće broj). U NetworkX-u obično `weight`. **Težinski stupanj** čvora može biti zbroj težina svih bridova incidentnih s tim čvorom (umjesto broja bridova).
- **Asimetrija**: U usmjerenom grafu matrica susjedstva nije simetrična: postoji veza od A prema B ne znači da postoji od B prema A. Ta asimetrija nosi informaciju o tome tko je „aktivniji” u odnosu, tko je izvor, tko primateľj.

---

## Ključni istraživači

- **David Easley i Jon Kleinberg** u knjizi *Networks, Crowds, and Markets* sustavno obrađuju usmjerene i težinske mreže u kontekstu tržišta, informacijskih mreža i društvenih platformi. Posebno korisno za intuiciju o protoku i ulogama.
- **Robert A. Hanneman i Mark Riddle** u *Introduction to Social Network Analysis* daju operacionalizaciju: kako odlučiti kada koristiti usmjereni graf, kako kodirati težine i koje mjere primijeniti.

---

## Recentna literatura

- **Easley, D., & Kleinberg, J. (2010).** *Networks, Crowds, and Markets: Reasoning About a Highly Connected World*. Cambridge University Press. (I novija izdanja.)
- Za implementaciju: **NetworkX** dokumentacija za `nx.DiGraph()`, `add_edge(u, v, weight=w)`, te za in/out degree i težinske varijante mjera.

---

## Problemi

- **Odabir smjera**: Što točno predstavlja smjer? „A prati B” vs. „A i B se međusobno prate” — odluka utječe na graf i na sve mjere. Treba eksplicitno definirati u metodologiji.
- **Odabir težine**: Što je „jačina” veze? Broj poruka, frekvencija susreta, percipirana bliskost? Različite operacionalizacije daju različite rezultate.
- **Interpretacija asimetrije**: Visok in-degree i nizak out-degree mogu značiti „popularan” čvor koji malo prati druge; obrnuto može značiti aktivnog korisnika koji prati mnoge. Kontekst platforme i istraživačko pitanje vode interpretaciji.

---

## Primjer u stvarnom svijetu

- **Sljedbenici na X/Twitteru**: Čvorovi su korisnici, usmjereni brid od A do B znači „A prati B”. In-degree = broj sljedbenika, out-degree = broj praćenja. Težina na bridu može (ako podatak postoji) označavati broj interakcija.
- **Broj poruka između parova** u organizaciji: čvorovi su zaposlenici, bridovi su usmjereni (tko je kome poslao) ili neusmjereni, s težinom = broj poruka. Težinski stupanj pokazuje „najaktivnije” čvorove.
- **Citiranja**: članak A citira članak B — usmjereni brid od A do B. In-degree članka = broj citata (često korištena mjera „utjecaja”).

Modeliranje zahtijeva odluku: čvorovi = korisnici (ili članci, stranice), bridovi = usmjereni ili ne, s ili bez težine.

---

## Alati i metode

U **NetworkX**-u: `nx.DiGraph()` za usmjereni graf; `G.add_edge(u, v, weight=w)` za težinski brid. Metrike: `in_degree_centrality`, `out_degree_centrality`; za težinski stupanj `nx.degree(G, weight='weight')`. Neke mjere (npr. betweenness, closeness) imaju varijante za usmjerene grafove — v. dokumentaciju. Gephi i drugi alati također podržavaju usmjerene i težinske mreže; pri vizualizaciji smjer se često prikazuje strelicama, težina debljinom brida.

---

Vidi primjer: [05_usmjerene_tezinske_mreze.ipynb](../code/05_usmjerene_tezinske_mreze.ipynb)
