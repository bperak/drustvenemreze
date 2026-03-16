# 10. Online društvene mreže i analiza njihovih podataka

Instagram, X (Twitter), Facebook, LinkedIn i slične platforme **jesu** društvene mreže u smislu kolegija: čvorovi su korisnici (ili stranice, hashtagovi), veze su sljedbenici, prijatelji, likeovi, retweetovi. One nude ogromne količine podataka za istraživanje — ali i **izazove**: ograničenja API-ja, etička pitanja, reprezentativnost (tko uopće je na platformi) i nestabilnost pravila pristupa. Ovo poglavlje uvodi **karakteristike** online društvenih mreža, **načine** na koje možemo doći do podataka (API-ji, javni datasetovi, mock podaci), **ograničenja** s kojima se susrećemo i **primjene** u kulturološkom i komunikacijskom istraživanju, uključujući hrvatski i srednjoeuropski kontekst.

---

## Teorijski koncept

**Online društvene mreže** jesu platforme na kojima korisnici stvaraju profile, povezuju se s drugima (prijatelji, sljedbenici) i ostvaruju interakcije (poruke, likeovi, dijeljenja). Za istraživača one su i **predmet** proučavanja (kako ljudi koriste platforme, kako se formiraju zajednice) i **izvor podataka** za analizu mreža. Karakteristike koje ih razlikuju od „klasičnih” mreža uključuju **velik obujam**, **digitalni trag** (automatski bilježene interakcije), **globalni doseg** i **promjenjiva pravila** (algoritmi, uvjeti korištenja, API-ji). Istraživanje online mreža zahtijeva poznavanje tih karakteristika i etičnu pažnju: što smijemo dohvatiti, kako zaštititi korisnike i kako transparentno izvještavati metode.

---

## Definicije

- **Online društvena mreža**: Platforma (aplikacija ili web servis) u kojoj su **čvorovi** korisnici (ili stranice, grupe, hashtagovi), a **veze** definiraju odnos tipa prijateljstvo, sljedbenik, ili interakcija (like, komentar, retweet). Struktura se može analizirati istim alatima kao i druge mreže, ali operacionalizacija (što točno je brid) ovisi o platformi i istraživačkom pitanju.
- **API (Application Programming Interface)**: Tehničko sučelje putem kojega **programski** dohvaćamo podatke s platforme (npr. popis sljedbenika, tweetovi). Korištenje API-ja uvijek je uvjetovano **uvjetima korištenja** (ToS) platforme i često **kvotama** (koliko zahtjeva po satu/dan). Pristup se u posljednje vrijeme sve češće ograničava ili stavlja u plaćene tierove.

---

## Ključni istraživači

- **David Easley i Jon Kleinberg** u *Networks, Crowds, and Markets* obrađuju online kontekst: kako mreže na platformama funkcioniraju, kako se formiraju grupe i kako se informacije šire.
- **Matthew A. Russell** u *Mining the Social Web* daje **praktičan** vodič za dohvaćanje i analizu podataka s Facebooka, Twittera, LinkedIna i drugih platformi — uključujući osnove API-ja i obrade u Pythonu. Važno je imati na umu da se API-ji i politike platformi mijenjaju, pa je potrebno provjeriti ažurirane izvore.

---

## Recentna literatura

- **Russell, M. A. (2018).** *Mining the Social Web* (3. izd.). O'Reilly. Praktični primjeri i kod.
- **Bruns, A., & Burgess, J. (2015)** i kasniji radovi o **Twitter** analizi: hashtagovi, retweet mreže, metodologija.
- Radovi o **Instagram API**, **Facebook Graph API**, **X (Twitter) API v2** (2020.+): što je moguće dohvatiti, koja su ograničenja. Posebno korisna literatura o **etici** i **GDPR**-u pri istraživanju društvenih medija (npr. smjernice AoIR).

---

## Problemi

- **Ograničenja API-ja**: Kvote, plaćeni pristup, zabrana nekih tipova podataka. Dokumentacija se mijenja; istraživač mora provjeriti trenutne uvjete i planirati istraživanje u skladu s njima.
- **Etika i suglasnost**: Javni profili nisu nužno „javni” u smislu da istraživač može slobodno skupljati i objavljivati podatke. Potrebno je razmotriti suglasnost, anonimizaciju i transparentnost; mnoge institucije zahtijevaju etičku provjeru.
- **Pristranost**: Tko je na platformi? Korisnici nisu reprezentativni za cijelu populaciju; jezična, dobna i geografska pristranost utječu na zaključke. Treba eksplicitno navoditi granice općenitosti.
- **Zastarjelost dokumentacije**: API-ji i uvjeti korištenja mijenjaju se; knjige i članci brzo zastarjevaju. Redovita provjera službenih stranica platformi i recentne literature nužna je.

---

## Kulturologija i komunikacija

Istraživanje **kulturnih zajednica**, **medijskih događaja**, **aktivizma** i **identiteta** na platformama važno je za kulturološke i komunikacijske studije. Primjeri uključuju: analizu hashtagova vezanih uz kulturne festivale ili institucije; mreže korisnika koji raspravljaju o određenim temama; ulogu influencera u širenju sadržaja. **Hrvatski i srednjoeuropski kontekst** može uključivati proučavanje lokalnih hashtagova, medijskih kuća, kulturnih ustanova ili javnih debata — uz poštivanje etike i prava.

---

## Kako doći do podataka

- **Javni API-ji**: X (Twitter) nudi API s ograničenjima (kvote, plaćeni tierovi); Facebook i Instagram strogo ograničavaju pristup za istraživanje. Uvijek u skladu s **ToS** i **GDPR**.
- **Javni datasetovi**: Arhive tweetova, SNAP datasetovi, ICWSM dataseti — korisni za učenje i za istraživanja koja ne zahtijevaju vlastito skupljanje. Provjeriti licence i etičke smjernice.
- **Mock podaci**: Za vježbu i demonstraciju metoda dovoljni su **sintetički** ili anonimizirani primjeri; time izbjegavamo etičke i pravne rizike dok vježbamo analizu.

---

## Alati

**Python**: `tweepy` (X API), `requests` za generičke API pozive; `pandas` za obradu tabličnih podataka; **NetworkX** za gradnju grafa i analizu. Alternativa: korištenje **gotovih datasetova** (npr. SNAP, ICWSM) ako odgovaraju istraživačkom pitanju.

---

Vidi primjer: [10_online_mreze_primjer.ipynb](../code/10_online_mreze_primjer.ipynb)
