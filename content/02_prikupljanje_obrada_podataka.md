# 2. Prikupljanje i obrada podataka o društvenim mrežama

Bez podataka o tome tko je s kime povezan — ili kako se ti odnosi mijenjaju — analiza društvenih mreža ostaje samo teorija. Stvarna mreža uvijek se mora *izmjeriti*: putem anketa u kojima ljudi navode svoje kontakte, putem digitalnih tragova na platformama, putem analize tekstova ili promatranja u terenu. **Suvremeni istraživači sve češće koriste umjetnu inteligenciju (AI)** za ekstrakciju entiteta i veza iz teksta, za čišćenje i strukturiranje podataka te za pomoć pri tumačenju. Način na koji prikupljamo podatke određuje što uopće možemo pitati: egocentrična mreža jedne osobe, cijela zajednica, ili mreža korisnika nekog hashtaga na društvenim mrežama. Ovo poglavlje vodi vas kroz glavne metode prikupljanja, **AI-alate i klasične alate** za obradu i odluke koje trebate donijeti prije nego što možete graditi graf i tumačiti rezultate.

---

## Teorijski koncept

Prikupljanje podataka o društvenim mrežama obuhvaća cijeli lanac: **identificiranje** što želimo mjeriti (koji entiteti, koje veze), **prikupljanje** — ankete, API-ji, scrape, promatranje — **čišćenje** i **organiziranje** podataka u oblik pogodan za analizu (npr. liste čvorova i bridova). Obrada podataka odnosi se na sljedeći korak: korištenje tih podataka za izračun mjera, vizualizaciju i identificiranje uzoraka, trendova i značajki. Dva su procesa usko povezana: loše prikupljeni ili neprecizno definirani podaci ne mogu se „spasiti” sofisticiranom obradom; dobro dizajnirana metoda prikupljanja olakšava i tumačenje. Stoga je važno razumjeti prednosti i mane svake metode te odabrati onu koja najbolje odgovara istraživačkom pitanju i etičkim ograničenjima.

---

## Definicije

- **Prikupljanje podataka o društvenim mrežama**: Sustavan postupak dobivanja informacija o **čvorovima** (pojedinci, organizacije, stranice, hashtagovi) i **vezama** između njih unutar mreže koju želimo proučavati. Uključuje odluku tko ili što ulazi u uzorak i kako se veze operacionaliziraju (npr. „navedi do pet ljudi s kojima najčešće surađuješ”).
- **Obrada podataka**: Faza u kojoj se sirovi podaci čiste (duplikati, nedostajuće vrijednosti, pogreške), strukturiraju u oblik grafa (matrica susjedstva, lista bridova) i analiziraju — izračun mjera, detekcija zajednica, vizualizacija. **AI može pomoći** pri automatskom čišćenju, prepoznavanju entiteta i mapiranju relacija u listu bridova. Rezultat obrade su brojke, grafovi i tablice koje možemo interpretirati.
- **SNA (Social Network Analysis)**: Širi pojam koji označava metodologiju proučavanja odnosa i interakcija između aktera u mreži: mapiranje veza, opis strukture i povezivanje te strukture s društvenim ishodima (utjecaj, širenje informacija, kohezija grupe). Prikupljanje i obrada podataka dio su te metodologije.

---

## Ključni istraživači

Metodologija prikupljanja i obrade mrežnih podataka temelji se na desetljećima razvoja u sociologiji, antropologiji i srodnim disciplinama:

- **Stanley Wasserman i Katherine Faust** u klasičnoj knjizi *Social Network Analysis: Methods and Applications* (1994.) sustavno opisuju kako se podaci o mrežama prikupljaju (ankete, name generators, name interpreters), kako se grade matrice i grafovi i kako se interpretiraju mjere. Njihov pristup i danas služi kao referenta točka za „klasične” mrežne studije.
- **Stephen P. Borgatti, Martin G. Everett i Jeffrey C. Johnson** u knjizi *Analyzing Social Networks* (SAGE) nude praktičan vodič: kako odabrati metodu, kako koristiti softver (uključujući UCINet) i kako izbjeći česte pogreške. Posebno je korisno za one koji tek ulaze u područje.
- **Robert A. Hanneman i Mark Riddle** autori su *Introduction to Social Network Analysis* (dostupno online), s naglaskom na konceptualne korake od istraživačkog pitanja do operacionalizacije i analize.

Poznavanje tih izvora pomaže pri dizajniranju vlastitog istraživanja i pri čitanju literature u kojoj se koriste različiti termini za iste ili slične postupke.

---

## Recentna literatura

Područje se brzo mijenja, posebno s razvojem online platformi, API-ja i **umjetne inteligencije**. Korisno je obratiti se novijim izvorima:

- **Borgatti, S. P., Everett, M. G., & Johnson, J. C. (2018).** *Analyzing Social Networks* (2. izd.). SAGE. Ažurirana verzija s primjerima i preporukama za suvremene alate.
- **Russell, M. A. (2018).** *Mining the Social Web* (3. izd.). O'Reilly. Praktičan vodič za prikupljanje i analizu podataka s Facebooka, Twittera, LinkedIna i drugih platformi — uključujući API-je i osnove obrade u Pythonu. Važno je imati na umu da se API-ji i uvjeti korištenja mijenjaju, pa je dobro provjeriti najnoviju dokumentaciju.
- Za **AI u mrežnoj analizi**: tražiti radove o ekstrakciji relacija pomoću LLM-ova (Large Language Models), NER (Named Entity Recognition), ili automatskom kodiranju teksta u mrežne podatke (otprilike 2020. nadalje).
- Preporučuje se tražiti radove od otprilike 2015. nadalje kada je riječ o prikupljanju s online platformi, etici, GDPR-u i reproducibilnosti (npr. korištenje javnih datasetova, dokumentiranje koraka).

---

## Problemi

Prikupljanje i obrada podataka nose s sobom nekoliko izazova koje treba držati na umu:

- **Odabir granica mreže i uzorka**: Tko ulazi u mrežu? Ako koristimo anketu, tko je pozvan i tko odgovori? Ako skupljamo podatke s platforme, tko je uopće na toj platformi? Granice određuju što „vidimo” — i što ne vidimo. Rubni čvorovi ili grupe koje nisu uključene mogu biti upravo oni koji su ključni za neko pitanje.
- **Etička i pravna ograničenja**: Pri skupljanju s društvenih platformi moramo poštivati uvjete korištenja (ToS) i zakone o zaštiti podataka (npr. GDPR). Anonimizacija, suglasnost ispitanika i transparentnost metode dio su odgovorne prakse. Istraživanje bez etičke provjere može nanijeti štetu i diskreditirati rezultate.
- **Kvaliteta i pristranost**: Ankete ovise o tome što ljudi žele ili mogu reći; pamćenje i socijalna poželjnost utječu na odgovore. Digitalni tragovi (likeovi, sljedbenici) ne odražavaju nužno „stvarne” odnose. Treba biti jasan u tome što zapravo mjerimo i koje su ograničenja tog mjerenja.
- **AI i pristranost**: Alati temeljeni na AI (LLM-ovi, NER) mogu uvesti vlastitu pristranost: model može prepoznavati samo određene tipove entiteta ili relacija, ovisno o načinu treniranja. Rezultate ekstrakcije treba provjeravati (uzorak ručne provjere, interkoder pouzdanost) i transparentno dokumentirati korišteni model i prompt.

O tim problemima detaljnije u poglavljima o online mrežama i o kritičkom razmišljanju (pogl. 10, 13).

---

## Primjer u stvarnom svijetu

Različite situacije zahtijevaju različite izvore podataka:

- **Ankete** (npr. Google Forms) pogodne su kada želimo dobiti mrežu iz perspektive ispitanika: „Navedi do pet ljudi s kojima najčešće surađuješ” ili „Tko su ti najbliži prijatelji?”. Iz takvih odgovora gradimo egocentrične mreže ili, ako imamo više ispitanika iz iste zajednice, mrežu cijele grupe. Prednost je kontrola nad definicijom veze; mana je opterećenje ispitanika i moguća pristranost odgovora.
- **Etnografsko promatranje** uključuje dugotrajno sudjelovanje u zajednici i dokumentiranje tko s kime komunicira, surađuje ili se druži. Bogat je izvor konteksta, ali zahtijeva puno vremena i teško se skalira na velike mreže.
- **Analiza sadržaja** — tekstovi, knjige, mediji — omogućuje izvlačenje veza iz samog sadržaja: tko se u romanu pojavljuje zajedno, koji se hashtagovi pojavljuju u istom tweetu. **Suvremeni pristup**: korištenje **LLM-ova (npr. ChatGPT, Claude, lokalni modeli)** ili NER-alata za automatsku ekstrakciju entiteta i relacija iz teksta — npr. „Iz ovog odlomka izluči sve osobe i njihove međusobne odnose”. Ručno tagiranje ostaje opcija za manje korpus ili za validaciju. Primjeri u nastavi uključuju mreže iz literarnih djela i projekata poput [Fiume in Flux](https://rijekafiumeinflux.com/en/home/) te [Network Extraction Chat GPT](https://colab.research.google.com/drive/1Ek-mLoBF11wzKfoL4UYDntvovlwCu-jB?usp=sharing).
- **Web scraping** i korištenje **API-ja** omogućuju automatsko prikupljanje velikih količina podataka s web stranica ili platformi (npr. GitHub, u određenim granicama Twitter/X). Prednost je obujam i brzina; mana su pravna i etička ograničenja te nestabilnost sučelja (API-ji se mijenjaju, kvote se ograničavaju).

U praksi često se kombinira više metoda; važno je da odluka bude svjesna i da se zabilježi u metodologiji.

---

## Metode prikupljanja (pregled)

- **Ankete i upitnici**: Strukturirani ili polustrukturirani upitnici s pitanjima o socijalnim vezama (name generator: „Tko su ljudi koje redovito kontaktiraš?”), zajednicama i komunikaciji. Za primjer modeliranja profesionalne mreže putem Google Formsa i Google Sheetova v. [Network 2 (Colab)](https://colab.research.google.com/drive/19HkPLNPOtGiP4o6v5pUKP2psVKGl8xM0?usp=sharing).
- **Etnografsko istraživanje**: Promatranje i dokumentiranje odnosa u terenu; posebno vrijedno za razumijevanje značenja veza u lokalnom kontekstu.
- **Analiza sadržaja**: Sustavno ispitivanje tekstova, slika ili videa radi identificiranja veza (npr. likovi u književnom djelu, entiteti u vijestima). **AI/LLM ekstrakcija**: uporaba ChatGPT, Claude, lokalnih LLM-ova ili NER (spaCy, Hugging Face) za automatsko izvlačenje entiteta i relacija; rezultat se pretvara u listu bridova. Ručno tagiranje za validaciju ili male korpuse. Primjeri: [Network 3](https://colab.research.google.com/drive/1gol_nC3R68Yp4rGWC66h2JtulTmKzvbH?usp=sharing), [Fiume in Flux](https://rijekafiumeinflux.com/en/home/), [Network Extraction Chat GPT](https://colab.research.google.com/drive/1Ek-mLoBF11wzKfoL4UYDntvovlwCu-jB?usp=sharing).
- **Web scraping**: Automatsko prikupljanje podataka s weba; primjer u nastavi: [FIFA dataset (Colab)](https://colab.research.google.com/drive/1kTo6Y8mVI3SEoojPJ6fMc-pFayjj3lr5?usp=sharing). Uvijek u skladu s ToS i etikom.

---

## AI u prikupljanju i obradi podataka

Umjetna inteligencija danas može podržati cijeli lanac od sirovih podataka do grafa:

| Faza | Kako AI pomaže |
|------|-----------------|
| **Ekstrakcija iz teksta** | LLM-ovi (ChatGPT, Claude, API-ji OpenAI/Anthropic ili lokalni modeli) mogu iz odlomaka izvući *tko* se spominje i *kakav je odnos* (npr. „A je prijatelj B”, „X surađuje s Y”). Rezultat: lista parova (čvor, čvor, tip_veze) koju zatim učitavamo u NetworkX ili Gephi. |
| **Čišćenje i normalizacija** | Automatsko uklanjanje duplikata, usklađivanje imena („Ivan Horvat” = „I. Horvat”), popunjavanje nedostajućih vrijednosti ili kategorizacija tipova veza. Može se kombinirati s Pandasom i jednostavnim promptovima ili skriptama. |
| **Ankete i kodiranje** | AI može pomoći u dizajnu pitanja (name generatora) ili u prekodiranju otvorenih odgovora u strukturirane veze — uz nužnu ljudsku provjeru i etičku pažnju. |
| **Interpretacija** | Nakon izračuna mjera (npr. centralnost), LLM može pomoći u formuliranju interpretacija ili u sumiranju uzoraka u velikim mrežama — ne zamjenjuje kritičko razmišljanje istraživača. |

**Praktični savjet**: Ekstrakciju relacija iz teksta najbolje raditi s **strukturiranim outputom** (npr. tražiti od LLM-a JSON s listom `{ "source": "A", "target": "B", "relation": "surađuje" }`) kako bismo lako uvezli podatke u Python. U bilježnicama kolegija koristi se primjer [Network Extraction Chat GPT](https://colab.research.google.com/drive/1Ek-mLoBF11wzKfoL4UYDntvovlwCu-jB?usp=sharing). Za reprodukciju uvijek zabilježite verziju modela i prompt.

---

## Alati za obradu podataka

Kad imamo sirove podatke, trebamo ih pretvoriti u graf i analizirati. Neki od najčešće korištenih alata:

- **UCINet**: Klasičan softver za analizu društvenih mreža; podrška za matrice, mjere i vizualizaciju. [Upute i preuzimanje](https://sites.google.com/site/ucinetsoftware/home).
- **Gephi**: Besplatan, vizualno moćan alat za vizualizaciju i osnovnu analizu mreža; podržava razne formate i layout algoritme. [gephi.org](https://gephi.org/); korisni primjeri datasetova: [Gephi wiki](https://github.com/gephi/gephi/wiki/Datasets), [Sample social network datasets](https://github.com/melaniewalsh/sample-social-network-datasets).
- **Python**: Programski jezik s bibliotekama kao što su **NetworkX** (grafovi i mjere), **igraph** (velike mreže), **Pandas** (tablični podaci i čišćenje). Pogodan za reproducibilnu analizu i automatizaciju; lako se **spaja s AI**: npr. OpenAI/Anthropic API za ekstrakciju, spaCy za NER, zatim Pandas + NetworkX za graf.
- **AI/LLM alati**: **ChatGPT, Claude, Gemini** (kroz sučelje ili API) za ekstrakciju entiteta i relacija iz teksta; **spaCy** ili **Hugging Face** za NER i relation extraction u Pythonu. Za rad s API-jem koristite varijable iz `.env` (ključevi) kako podaci ostanu sigurni i reprodukcija bude moguća.
- **Online alati**: Npr. [Spotify playlist playground](https://labs.polsys.net/playground/spotify/) za igru s mrežama sličnosti; **Neo4j** za rad s graf bazama podataka. [neo4j.com](https://neo4j.com/)

Izbor alata ovisi o veličini podataka, potrebi za vizualizacijom ili skriptiranjem i prethodnom iskustvu; u ovom kolegiju posebno ćemo koristiti Python i NetworkX u Jupyter bilježnicama, s opcionalnom AI ekstrakcijom za analizu sadržaja.

---

## Kako modelirati mrežu

Prije nego što učitamo podatke u softver, moramo odlučiti **što je čvor** i **što je brid**. Čvorovi su obično entiteti koje proučavamo: ljudi, organizacije, stranice, hashtagovi, knjige. Bridovi su veze ili interakcije: prijateljstvo, suradnja, retweet, zajednička pojavnost. Treba odlučiti jesu li veze **usmjerene** (A prati B ≠ B prati A) ili **neusmjerene**, i imaju li **težinu** (npr. broj poruka). Te odluke direktno ovise o istraživačkom pitanju: za pitanje „Tko širi informacije?” možda nam treba usmjerena mreža retweetova; za „Koliko je grupa kohezivna?” možda neusmjerena mreža prijateljstva s težinama. Dobro je tu logiku zabilježiti u metodologiji kako bi čitatelj i vi sami kasnije znali što brojke zapravo predstavljaju.

---

## Resursi (tutoriali)

Za daljnje samostalno učenje, posebno Python i NetworkX:

1. [Introduction to Network Science with NetworkX (Part 1)](https://python.plainenglish.io/introduction-to-network-science-with-networkx-part-1-c306fc3860e0)
2. [Part 2](https://python.plainenglish.io/introduction-to-network-science-with-networkx-part-2-67e0f4a60fba)
3. [Part 3](https://medium.com/python-in-plain-english/introduction-to-network-science-with-networkx-part-3-18fd6eeaa72d)
4. [Plotting network graphs using Python](https://towardsdatascience.com/plotting-network-graphs-using-python-bc62f0d93b3f)

Za **AI ekstrakciju relacija**: Colab primjer [Network Extraction Chat GPT](https://colab.research.google.com/drive/1Ek-mLoBF11wzKfoL4UYDntvovlwCu-jB?usp=sharing); za rad s API-jem u Pythonu koristite `python-dotenv` i varijable iz `.env` za ključeve.

---

## Rezultati i implikacija

Obrada podataka vodi do konkretnih rezultata: tablice mjera (centralnost, gustoća, koeficijent klasteriranja), vizualizacije grafa, particije u zajednice. Ti rezultati omogućuju da odgovorimo na pitanja tipa: Tko je središnji? Koliko je mreža gusto povezana? Postoje li jasne grupe? **Implikacija** koju treba imati na umu: **odabir metode prikupljanja i alata ograničava i usmjerava tip pitanja na koja možemo odgovoriti**. Ankete su snažne za egocentrične mreže i percipirane veze; API-ji platformi za velike mreže korisnika i digitalne interakcije; **AI ekstrakcija** omogućuje brzo pretvaranje velikih tekstualnih korpusa u mrežne podatke, uz potrebu za validacijom i svjesnošću o pristranosti modela. Nema „najbolje” metode općenito — samo metoda prikladna za vaše pitanje i etički okvir.

---

Vidi primjer u skripti: [02_prikupljanje_podataka_ankete.ipynb](../code/02_prikupljanje_podataka_ankete.ipynb) — ili postojeći **Perak_Network_2.ipynb** (Google Forms → mreža).
