# 14. Analiza Twittera/X uporabom programskih alata

Platforma **X** (ranije Twitter) jedna je od najčešće korištenih u istraživanju društvenih medija: relativno otvoreni format (kratke poruke, hashtagovi, retweetovi) omogućuje analizu tema, aktera i mreža interakcija. Ovo poglavlje daje **praktičan uvod** u dohvaćanje i analizu podataka s X-a: što je API, kako graditi mreže (retweet, mention, ko-pojavljivanje hashtagova), koje osnovne metrike i vizualizacije koristiti. Naglasak je na **etičnoj i pravno usklađenoj** praksi — korištenje API-ja u skladu s uvjetima, zaštita identiteta, korištenje .env za ključeve — te na **kulturološki relevantnim** primjerima (npr. hrvatski hashtagovi vezani uz kulturne događaje ili javne teme), uz poštivanje ToS i etike.

---

## Teorijski koncept

Analiza X-a (Twittera) u kontekstu SNA obično uključuje: **(1)** dohvaćanje podataka putem **API-ja** (tweetovi, korisnici, relacije); **(2)** gradnju **grafa** u kojem su čvorovi korisnici ili hashtagovi, a bridovi retweetovi, mentioni ili ko-pojavljivanja; **(3)** izračun **mjera** (centralnost, gustoća, zajednice) i **vizualizaciju**. Cilj može biti opis strukture konverzacije oko nekog hashtaga, identifikacija centralnih aktera ili usporedba mreža u različitim vremenskim periodima. Teorijski okvir isti je kao u prethodnim poglavljima (centralnost, zajednice, difuzija); specifičnost je u **operacionalizaciji** na platformi X i u tehničkim i etičkim ograničenjima pristupa podacima.

---

## Definicije

- **X API (Twitter API) v2**: Trenutno glavno **programsko sučelje** za dohvaćanje tweetova, metapodataka i (u ograničenom obimu) informacija o korisnicima. Zahtijeva **registraciju** na developer.twitter.com (sada X Developer) i korištenje **API ključeva**; ograničen je **kvotama** (broj zahtjeva po vremenu). Postoje besplatni i plaćeni tierovi; uvjeti se mijenjaju, pa je nužno provjeriti službenu dokumentaciju.
- **Retweet mreža**: Graf u kojem su **čvorovi** korisnici (ili njihovi ID-ovi), a **usmjereni brid** od A do B znači „A je retweetirao B”. Često se analizira tko je koga retweetirao u kontekstu nekog hashtaga ili događaja. In-degree u toj mreži pokazuje tko je „najviše retweetiran”.
- **Hashtag**: Oznaka teme u obliku #riječ. **Ko-pojavljivanje hashtagova** (koji hashtagovi se pojavljuju u istom tweetu) može se tretirati kao mreža: čvorovi = hashtagovi, bridovi = ko-pojavljivanje, opcionalno s težinom (broj puta). Korisno za mapiranje tema i povezanosti diskursa.

---

## Ključni istraživači

- **Matthew A. Russell** u *Mining the Social Web* daje praktične primjere rada s Twitter API-jem (u verziji koja je bila aktualna u vrijeme izdanja); korisno za logiku obrade, uz napomenu da se sintaksa API-ja mijenja (v1.1 → v2).
- **Službena dokumentacija X Developer** (developer.twitter.com) primarni je izvor za trenutno API ponašanje, autentifikaciju i kvote.

---

## Recentna literatura

- **X API v2 dokumentacija** (2020. i kasnije); napomene o **migraciji** s v1.1 na v2 i o promjenama u pristupu.
- **Bruns, A., & Burgess, J.** i suradnici — brojni radovi o **Twitter** metodologiji; **tweepy** dokumentacija za Python. Radovi o **etici** prikupljanja Twitter/X podataka (AoIR, GDPR) važni su za dizajn istraživanja.

---

## Problemi

- **Plaćeni i besplatni tierovi**: Mogućnosti API-ja znatno se razlikuju između besplatnog i plaćenog pristupa; za neke tipove istraživanja potrebna je pretplata ili partnerstvo.
- **Kvote**: Ograničen broj zahtjeva po 15 minuti / danu; velike studije zahtijevaju planiranje i eventualno uzorkovanje.
- **ToS**: Što smije i ne smije objaviti, kako dugo čuvati podatke, kako identificirati korisnike u publikacijama — sve to regulirano je uvjetima korištenja i etičkim smjernicama.
- **Kulturološki i jezični bias**: Podaci na engleskom ili s velikih tržišta često su nadzastupljeni; analiza hrvatskih ili manjih jezičnih zajednica zahtijeva svjesno odabir ključnih riječi i hashtagova te napomenu o ograničenjima općenitosti.

---

## Kako doći do podataka

- **Registracija** na developer.twitter.com (X Developer), stvaranje projekta i aplikacije, dobivanje **API ključeva** (API Key, API Secret, Bearer Token, te za OAuth Access Token i Secret ako koristite korisnički kontekst).
- **Ključeve nikad ne stavljati u kod**; koristiti **.env** datoteku i učitavanje putem `os.getenv()` ili `python-dotenv`. .env ne commitati u repozitorij.
- **tweepy** (Python biblioteka) ili izravni **requests** prema API endpointima; dokumentacija za v2 opisuje potrebne zaglavlja i parametre.
- Za **vježbu** bez stvarnog API poziva: **mock podaci** (lista parova korisnik–retweetirao) ili **javni datasetovi** (npr. arhive na archive.org, akademski datasetovi) u skladu s licencama.

---

## Alati

- **Python**: **tweepy** za X API; **requests** za HTTP; **pandas** za tablice; **NetworkX** za graf. Graf gradimo tako da **čvorovi** budu korisnici (ili hashtagovi), **bridovi** retweet/mention/ko-pojavljivanje; za usmjerene mreže koristimo `nx.DiGraph()`.
- **Vizualizacija**: NetworkX + matplotlib za statične grafove; za interaktivne mogu se koristiti pyvis, Gephi ili export u format pogodan za D3.js.

---

## Kulturološki primjeri

Analiza **hrvatskih** (ili srednjoeuropskih) **hashtagova** vezanih uz kulturne događaje, medijske teme ili javne debate ilustrira primjenu u kulturološkom i komunikacijskom kontekstu. Primjeri mogu uključivati: festivale, izložbe, književne nagrade, lokalne medije ili reakcije na odredene događaje. Uvijek u skladu s **ToS** platforme i s **etičkim** načelima (anonimizacija gdje je potrebno, transparentnost metode).

---

Vidi primjer: [14_twitter_x_primjer.ipynb](../code/14_twitter_x_primjer.ipynb)
