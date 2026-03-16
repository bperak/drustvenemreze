---
name: Nastavni materijal SNA MD i Jupyter
overview: Plan za prebacivanje skripte „Istraživanja društvenih mreža” u 10+ Markdown poglavlja s po jednim Jupyter primjerom po poglavlju, uz osuvremenjavanje sadržaja (platforme Instagram, X, Facebook) i kulturološki relevantne primjere — sve na hrvatskom.
todos: []
isProject: false
---

# Plan: Nastavni materijal Istraživanja društvenih mreža (MD + Jupyter, na hrvatskom)

## Uvod i preduvjeti

- **Predmet:** INP Istraživanja društvenih mreža 2025/26  
- **Izvori:** skripta [Istrazivanja Drustvenih Mreza.md](d:\Kulturalni_studiji\IstrazivanjeDrustvenihMreza\Istrazivanja Drustvenih Mreza.md) (jedan veliki .md u repozitoriju), predmetni dokument `INP Istraživanja društvenih mreža 2025.26.docx`  
- **Cilj:** Nastavni materijal u obliku **14 .md datoteka po poglavljima** (prema strukturi skripte) + **po jedan .ipynb primjer po poglavlju**, sve **na hrvatskom**, s naglaskom na **osuvremenjavanje** i **istraživanje online mreža** (Instagram, X, Facebook) te **kulturološki relevantne primjere**.

---

## 1. Priprema sadržaja i strukture repozitorija

- **Izvorni sadržaj:** Skripta je u repozitoriju kao jedan .md: [Istrazivanja Drustvenih Mreza.md](d:\Kulturalni_studiji\IstrazivanjeDrustvenihMreza\Istrazivanja Drustvenih Mreza.md). Potrebno je **izrezati** po poglavljima (prema naslovima # u skripti) u zasebne .md datoteke.
- **Predmetni dokument:** Pročitati `INP Istraživanja društvenih mreža 2025.26.docx` (ako je dostupan) radi usklađivanja ishoda učenja i terminologije.
- **Struktura repozitorija:**
  - `**content/`** — 14 .md datoteka (jedna po poglavlju, vidi popis u odjeljku 2); teorijski sadržaj i tekst poglavlja.
  - `**code/`** — 14 .ipynb datoteka (po jedan po poglavlju); skripte i primjeri koji se mogu pokrenuti.
  - **Veze između content i code:** U svakom .md u `content/` na kraju (ili u uvodnom bloku) link na odgovarajući .ipynb u `code/`. U svakom .ipynb u `code/` u prvoj markdown ćeliji link na odgovarajući .md u `content/` (npr. „Poglavlje: [Naslov](../content/XX_ime.md)”).
  - Opcionalno: izvorni `Istrazivanja Drustvenih Mreza.md` ostaje u rootu kao arhiva ili se premjesti u `materijali/`.
  - `requirements.txt` u rootu za Python ovisnosti (networkx, pandas, matplotlib, itd.)

---

## 2. Raspored poglavlja (prema skripti Istrazivanja Drustvenih Mreza.md)

Skripta ima **14 poglavlja** (prema sadržaju Istrazivanja Drustvenih Mreza.md):  

1. Uvod u društvene mreže i teoriju grafova · 2. Prikupljanje i obrada podataka · 3. Mjere mrežne strukture i interpretacija rezultata · 4. Socijalni kapital i društvene mreže · 5. Mreže usmjerene i mreže sa težinama · 6. Analiza zajednica · 7. Vizualizacija društvenih mreža · 8. Difuzija inovacija i utjecaj · 9. Dinamika mreža i promjene u vremenu · 10. Online društvene mreže · 11. Primjena SNA u marketinškim istraživanjima · 12. Društvene mreže i političko ponašanje · 13. Kritičko razmišljanje i ograničenja SNA · 14. Analiza Twittera/X programskim alatima.

Svako poglavlje postaje jedan .md u `**content/`** i jedan .ipynb u `**code/`**, s međusobnim linkovima (v. odjeljak 1). Nazivi datoteka bez dijakritika (ASCII) radi kompatibilnosti. **Za svako poglavlje** primjenjuje se ista struktura, uključujući **izdvojene** definicije, istraživače i probleme: teorijski koncept → definicije → istraživači → reference na recentne radove → problemi → primjer u stvarnosti → kulturologija/komunikacija/društvo → podaci → modeliranje mreže → alati → metode → rezultati → implikacija (v. odjeljak 3).


| Br. | Poglavlje (.md)                                    | Sadržaj (kratko)                                                                      | Primjer u .ipynb                                                                                       |
| --- | -------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 1   | Uvod u istraživanje društvenih mreža               | Pojam mreže, čvorovi, bridovi, tipovi mreža                                           | Graf iz liste bridova, osnovna vizualizacija (NetworkX)                                                |
| 2   | Teorijski okvir i povijest SNA                     | Kratka povijest, Granovetter, jak/slabi tie, strukturalne rupe                        | Vizualizacija “malog svijeta” ili jednostavan primjer jakih/slabih veza                                |
| 3   | Prikupljanje podataka: ankete i egocentrične mreže | Ankete, name generator, Google Forms                                                  | Učitavanje odgovora iz CSV/Excel, građenje egocentričnog grafa (nastavak na postojeći Perak_Network_2) |
| 4   | Mrežne metrike: stupanj, središnjost, gustoća      | Degree, betweenness, closeness, gustoća, komponente                                   | Izračun metrika u NetworkX i jednostavna tablica                                                       |
| 5   | Grupe i zajednice u mrežama                        | Klasteri, zajednice, modularnost, algoritmi (npr. Louvain)                            | Detekcija zajednica na malom primjeru                                                                  |
| 6   | Vizualizacija i interpretacija mreža               | Layouti, boje, veličine čvorova, dobre prakse                                         | Jedan layout (npr. force-directed) s objašnjenjima                                                     |
| 7   | Osuvremenjavanje: platforme i API-ji               | Instagram, X (Twitter), Facebook — što se može istraživati, ograničenja API-ja, etika | Primjer s javnim podacom (npr. Twitter/X API v2 ili mock podaci) — bez kršenja ToS                     |
| 8   | Istraživanje X (Twitter) i sličnih platformi       | Hashtagovi, retweet mreže, vremenske serije, kulturološki primjeri                    | Mala mreža “tko koga retweetira” ili analiza hashtagova (mock ili javni dataset)                       |
| 9   | Istraživanje Instagrama i vizualnih platformi      | Slike, hashtagovi, following/followers, kulturološki primjeri                         | Graf sličnosti hashtagova ili egocentrična mreža (mock podaci)                                         |
| 10  | Facebook i druge “prijateljske” mreže              | Struktura, grupe, stranice, etika i GDPR                                              | Primjer s javnim stranicama ili simulirani podaci                                                      |
| 11  | Etika i pravni okvir istraživanja online mreža     | GDPR, suglasnost, anonymizacija, ToS platformi                                        | Checklist i kratki kod za pseudonimizaciju / agregaciju                                                |
| 12  | Kulturološki i domaći primjeri                     | Hrvatska/srednjoeuropski kontekst: kulturne ustanove, mediji, aktivizam               | Jedan konkretan primjer (npr. mreža hashtagova vezanih uz kulturni događaj ili medij)                  |


Skripta je u repozitoriju; 14 poglavlja mapirati na .md/.ipynb kako je navedeno u odjeljku 2. Poglavlja 10 i 14 osuvremeniti (Instagram, X, Facebook, API-ji, kulturološki primjeri). “širenju informacija”, 

## 3. Jedinstvena struktura svakog poglavlja

U **svakom poglavlju** (.md + povezani .ipynb) obavezno **izdvojiti** i uvesti sljedeće elemente (na hrvatskom):

1. **Teorijski koncept** — koji se pojam ili teorija obrađuje (npr. centralnost, zajednice, difuzija, socijalni kapital).
2. **Definicije** — ključni pojmovi jasno definirani u poglavlju (npr. čvor, brid, centralnost, gustoća, zajednica); mogu biti u posebnoj podsekciji ili u tekstu s jasnim oznakama.
3. **Istraživači** — autori i klasične studije vezane uz koncept (npr. Granovetter, Wasserman i Faust, Barabási, Freeman); tko je utemeljio ili razvio pojam, s kratkim navodom rada ili doprinosa.
4. **Reference na recentne radove** — obavezno u svakom poglavlju navesti **recentnu literaturu** (radove od cca. 2015. nadalje): ključne članke, knjige ili preglede koji osuvremenjuju temu; po mogućnosti s DOI-om ili URL-om. Izdvojiti u podsekciju „Recentna literatura” ili „Daljnje čitanje”.
5. **Problemi** — istraživačka pitanja, kontroverze, metodološka ili društvena ograničenja na koje se poglavlje odnosi; koji se problemi rješavaju ili otvaraju.
6. **Primjer u stvarnom svijetu** — kako se taj koncept očituje u praksi (npr. mreža prijateljstva, retweetovi, hashtagovi na događaju).
7. **Kulturologija i komunikacijski/društveni problemi** — na što se odnosi u kulturološkim studijama, medijima, društvenim pitanjima (identitet, moć, širenje informacija, zajednice, aktivizam).
8. **Kako doći do podataka** — izvori (ankete, API-ji, scrape, javni datasetovi), što mjeriti (čvorovi, veze, atributi), etična ograničenja.
9. **Kako modelirati mrežu** — što su čvorovi, što su bridovi, usmjerenost, težine; koji dio stvarnosti preslikati u graf.
10. **Alati** — koji programski alati ili platforme (NetworkX, Gephi, Pandas, API-ji za X/Instagram/Facebook, Google Forms itd.).
11. **Metode** — koje analitičke ili statističke metode primijeniti (metrike centralnosti, detekcija zajednica, vizualizacija, vremenske serije).
12. **Rezultati** — što konkretno dobivamo (tablice, grafovi, indeksi); kako ih čitati.
13. **Implikacija rezultata** — što rezultati znače za istraživača, za kulturologiju/komunikologiju/društvo; koje zaključke ili daljnja istraživanja sugeriraju.

**Poboljšanja (ilustracije, povezivanje, primjeri):** Za dosljednu primjenu kroz sva poglavlja koristi [ENHANCEMENT_PROMPTS.md](ENHANCEMENT_PROMPTS.md) — prompti i checkliste za Mermaid ilustracije u sadržaju, povezivanje sadržaj ↔ kod, više/zabavniji primjeri, te stepwise notebook s crtežima u svakom koraku.

**Markdown datoteka (.md):**  
Sadržaj poglavlja organizirati prema gornjim točkama. Definicije, istraživači, **reference na recentne radove** i problemi moraju biti jasno izdvojeni (podnaslovi npr. "Definicije", "Ključni istraživači", "Recentna literatura", "Problemi"). Tekst preuzeti/prilagoditi iz skripte i dopuniti gdje treba. Na kraju navesti: “Vidi primjer u notebooku: `../code/XX_ime.ipynb`.”

**Jupyter notebook (.ipynb) u `code/`:**  
Jedan notebook po poglavlju. U **prvoj markdown ćeliji** link na teorijski sadržaj: npr. „Poglavlje: [Naslov poglavlja](../content/XX_ime.md)”. Zatim uvod (na hrvatskom), kod koji ilustrira **dohvat podataka → modeliranje mreže → alati → metode → rezultati**, te kratki zaključak o **implikaciji**. Koristiti javne ili mock podatke.

---

## 4. Osuvremenjavanje sadržaja

- **U svim .md i .ipynb:** terminologija i reference ažurirati gdje je skripta zastarjela (npr. stare verzije API-ja, stare platforme).
- **Reference na recentne radove:** U **svakom** poglavlju obavezno uključiti recentnu literaturu (cca. 2015.+): članke, knjige ili preglede s DOI-om/URL-om; izdvojiti u podsekciju „Recentna literatura” ili „Daljnje čitanje”. Posebno u poglavljima o online mrežama (10, 14) navesti recentne radove o Instagramu, X-u, Facebooku i metodama istraživanja.
- **Dodati sekcije ili podpoglavlja:**
  - Istraživanje **online** mreža: što je drugačije u odnosu na klasične ankete (podaci u stvarnom vremenu, veliki volumen, ograničenja API-ja, etika).
  - **Instagram, X, Facebook:** što se tipično istražuje (hashtagovi, following, grupe, stranice), koje metode i koja ograničenja.
- **Kulturološki primjeri:** u tekstu i u notebookima uključiti primjere relevantne za kulturološke studije i, gdje je moguće, za hrvatsko/srednjoeuropsko područje (kulturne ustanove, mediji, aktivizam, lokalne zajednice).
- **Etika i pravo:** posebno poglavlje (npr. 11) + kratke napomene u poglavljima o platformama.

---

## 5. Tehnički i jezični zahtjevi

- **Jezik:** Sav sadržaj (naslovi, paragrafi, komentari u kodu, objašnjenja u notebookima) na **hrvatskom**.
- **Notebooki:** Python 3, ovisnosti u `requirements.txt` (npr. `networkx`, `matplotlib`, `pandas`, eventualno `tweepy` ili drugi API wrapperi ako se koriste samo s mock/javnim podacima).
- **Podaci:** Bez stvarnih osobnih podataka bez suglasnosti. Za Instagram/Facebook/X koristiti javne agregirane datasetove, mock podatke ili službene primjere; u tekstu jasno naglasiti etična i pravna ograničenja.

---

## 6. Povezivanje s predmetom i postojećim materijalom

- U prvom .md (ili u posebnom `README.md` za materijal) navesti:
  - Naziv predmeta i akademsku godinu.
  - Kako su poglavlja povezana s ishodima učenja iz `INP Istraživanja društvenih mreža 2025.26.docx`.
- Postojeći **Perak_Network_2.ipynb** (ankete, Google Forms, učitavanje podataka) logično uklopiti kao primjer za poglavlje o **prikupljanju podataka / egocentričnim mrežama** (npr. poglavlje 3) i u .md tog poglavlja referencirati ga.

---

## 7. Redoslijed izrade (preporuka)

1. Izrezati iz [Istrazivanja Drustvenih Mreza.md](d:\Kulturalni_studiji\IstrazivanjeDrustvenihMreza\Istrazivanja Drustvenih Mreza.md) sadržaj po poglavljima (prema naslovima # 1.–14.) u 14 zasebnih .md datoteka u `**content/`**.
2. Kreirati mape `**content/`** i `**code/`** te `requirements.txt` u rootu.
3. Za svako poglavlje redom: dopuniti .md u `content/`, napisati povezani .ipynb u `code/` i u oba unijeti međusobne linkove.
4. U svakom .md u `content/` dodati link na odgovarajući .ipynb u `code/`; u svakom .ipynb u `code/` u prvoj ćeliji link na .md u `content/`. Za poglavlje 2 referencirati postojeći Perak_Network_2.ipynb (npr. u `code/` ili link iz `content/02_...md`).
5. Dodati uvodni README i povezati Perak_Network_2 s poglavljem 2.
6. Provjera: svi linkovi rade, jezik hrvatski, primjeri etički (javni/mock podaci).

---

## Pregled izlaza

- **14 .md datoteka** u `**content/`**, svaka jedan poglavlje (prema skripti), na hrvatskom, s osuvremenjenim sadržajem, referencama na recentne radove (podsekcija Recentna literatura) i kulturološki relevantnim primjerima.  
- **14 .ipynb datoteka** u `**code/`**, po jedan po poglavlju, s primjerima koji se mogu pokrenuti (javni/mock podaci).  
- **Veze:** Svaki .md u `content/` linka na odgovarajući .ipynb u `code/`; svaki .ipynb u `code/` linka na odgovarajući .md u `content/`.  
- **requirements.txt** za Python ovisnosti.  
- **README** koji povezuje predmet, ishode učenja i strukturu materijala.  
- **Perak_Network_2** referenciran u poglavlju 2 (Prikupljanje i obrada podataka).

