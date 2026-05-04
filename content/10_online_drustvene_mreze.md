# 10. Online društvene mreže i analiza njihovih podataka

Instagram, X (Twitter), Facebook, LinkedIn i slične platforme **jesu** društvene mreže u smislu kolegija: čvorovi su korisnici (ili stranice, hashtagovi), veze su sljedbenici, prijatelji, likeovi, retweetovi. One nude ogromne količine podataka za istraživanje — ali i **izazove**: ograničenja API-ja, etička pitanja, reprezentativnost (tko uopće je na platformi) i nestabilnost pravila pristupa. Ovo poglavlje uvodi **karakteristike** online društvenih mreža, **načine** na koje možemo doći do podataka (API-ji, javni datasetovi, mock podaci), **ograničenja** s kojima se susrećemo i **primjene** u kulturološkom i komunikacijskom istraživanju, uključujući hrvatski i srednjoeuropski kontekst.

U **kulturalnim studijama** online mreže nisu samo „tehnički graf”: one su **mjesto** gdje se kultura obnavlja, osporava i komercijalizira; gdje se identiteti **performiraju**; gdje algoritmi i poslovni modeli oblikuju tko je **vidljiv** i čija se priča **cirkulira**. Mrežna analiza tu služi kao **most** između kvantitativnog opisa strukture (tko s kime, koliko gusto) i kvalitativnog tumačenja (što ta struktura znači za moć, pripadnost i smisao).

---

## Teorijski koncept

**Online društvene mreže** jesu platforme na kojima korisnici stvaraju profile, povezuju se s drugima (prijatelji, sljedbenici) i ostvaruju interakcije (poruke, likeovi, dijeljenja). Za istraživača one su i **predmet** proučavanja (kako ljudi koriste platforme, kako se formiraju zajednice) i **izvor podataka** za analizu mreža. Karakteristike koje ih razlikuju od „klasičnih” mreža uključuju **velik obujam**, **digitalni trag** (automatski bilježene interakcije), **globalni doseg** i **promjenjiva pravila** (algoritmi, uvjeti korištenja, API-ji). Istraživanje online mreža zahtijeva poznavanje tih karakteristika i etičnu pažnju: što smijemo dohvatiti, kako zaštititi korisnike i kako transparentno izvještavati metode.

### Kulturalne studije i „platformski” obrat

Od 2010-ih nadalje sve se češće govori o **platformskim studijima** (*platform studies*): ne pita se samo *što* korisnici objavljuju, nego **kakvu infrastrukturu** platforma nudi, kako **moderira**, kako **monetizira pažnju** i kako **arhivira** (ili briše) kulturni sadržaj. Za kulturalne studije to znači da **graf veza** (npr. retweetovi) uvijek leži unutar **dizajna sučelja**, pravila zajednice i ekonomskih interesa vlasnika platforme. Zaključak o „zajednici” iz same mrežne slike mora se suodnositi s pitanjem: **čija je platforma**, tko profitira od vidljivosti i što API uopće dopušta vidjeti.

Korisne su i tradicije koje nisu „platformsko” nazvane, ali su bliske: **participatorna kultura** (npr. Jenkins — kako obožavatelji i amateri **koproduciraju** smisao), **medijacija** (Couldry & Hepp — digitalni mediji kao **slojevi** koji preoblikuju svakodnevicu), te studije **javnosti** i **afektivnosti** na mrežama (npr. Papacharissi — kako se na Twitteru/X-u oblikuje „privremena” politička i kulturna javnost). Mrežna analiza može **operacionalizirati** „tko se čuje uz koga” — ali tumačenje ostaje **hermeneutički** korak: brojevi ne zamjenjuju čitanje sadržaja i konteksta.

### Kultura kao mrežna praksa: vidljivost, performacija, cirkulacija

Na platformama **identitet** i **pripadnost** često se pokazuju kroz **pratnj**, **mention**, **hashtag** i **dijeljenje**. Iz perspektive kulturalnih studija bitne su tri dimenzije:

1. **Performacija** — profil i interakcije nisu „transparentan” odnos prema „istinskom ja”; oni su **izvedba** unutar normi platforme (što se smije prikazati, što algoritam nagrađuje).
2. **Cirkulacija** — kulturni artefakt (meme, vijest, najava predstave) postaje znanstveno zanimljiv i kao **put** kojim prolazi kroz mrežu čvorova, ne samo kao tekst na jednom čvoru.
3. **Vidljivost i marginalizacija** — centralnost u mreži može značiti **kulturni/politički kapital**, ali i rizik od **doxinga** ili napada; istraživač mora razmotriti tko će od **objave rezultata** biti ugrožen.

Zato **brid** u grafu nije neutralan: retweet, follow ili „zajednički hashtag” teorijski povezujemo s **praksom**, **diskurzom** ili **institucionalnom ulogom** — ali uvijek eksplicitno navodimo što smo pretpostavili.

### Jezik, lokalnost i „mali” digitalni prostori

U hrvatskom i širem **srednjoeuropskom** kontekstu važno je da platforme nisu jezikovno neutralne: veliki dijelovi istraživanja temelje se na **engleskom** ili „globalnom” Twitteru/X-u, dok su lokalni hashtagovi, mediji na manjim jezicima i **manje reprezentirani akteri** često **rijetki** u grafu ili potpuno izvan uzorka. To nije samo tehnički problem uzorka — to je **kulturno-politički** problem: **čija se kultura** uopće pojavljuje u podacima koje možemo prikupiti?

Primjeri istraživačkih tema iz kulturalnih studija uz mrežnu analizu:

- **Kulturne politike i institucije** — tko dijeli i komentira sadržaje muzeja, festivala, književnih nagrada; postoje li **mostovi** između „službenog” i „alternativnog” kruga?
- **Medijske mreže** — povezanost portala, novinara, političkih aktera oko **istog događaja** (npr. kulturna kontroverza).
- **Fan zajednice i memovi** — guste podmreže, brza cirkulacija, preklapanje s političkim temama.
- **Aktivizam i solidarnost** — koalicije hashtagova, retweet lanci tijekom protesta ili kampanja.

Uvijek treba spomenuti **granice općenitosti**: što je vidljivo na jednoj platformi u jednom trenutku **ne** predstavlja „cijelu kulturu” ili „cijelo društvo”.

---

## Definicije

- **Online društvena mreža**: Platforma (aplikacija ili web servis) u kojoj su **čvorovi** korisnici (ili stranice, grupe, hashtagovi), a **veze** definiraju odnos tipa prijateljstvo, sljedbenik, ili interakcija (like, komentar, retweet). Struktura se može analizirati istim alatima kao i druge mreže, ali operacionalizacija (što točno je brid) ovisi o platformi i istraživačkom pitanju.
- **API (Application Programming Interface)**: Tehničko sučelje putem kojega **programski** dohvaćamo podatke s platforme (npr. popis sljedbenika, tweetovi). Korištenje API-ja uvijek je uvjetovano **uvjetima korištenja** (ToS) platforme i često **kvotama** (koliko zahtjeva po satu/dan). Pristup se u posljednje vrijeme sve češće ograničava ili stavlja u plaćene tierove.
- **Operacionalizacija u kulturnom istraživanju**: Eksplicitno pravilo kojim iz **kulturne prakse** (npr. „javna podrška događaju”) izvodimo **čvorove** i **bridove** (npr. „retweet u intervalu od 7 dana”). Bez toga brojčane mjere teško je povezati s teorijskim pojmovima.

---

## Ključni istraživači

- **David Easley i Jon Kleinberg** u *Networks, Crowds, and Markets* obrađuju online kontekst: kako mreže na platformama funkcioniraju, kako se formiraju grupe i kako se informacije šire.
- **Matthew A. Russell** u *Mining the Social Web* daje **praktičan** vodič za dohvaćanje i analizu podataka s Facebooka, Twittera, LinkedIna i drugih platformi — uključujući osnove API-ja i obrade u Pythonu. Važno je imati na umu da se API-ji i politike platformi mijenjaju, pa je potrebno provjeriti ažurirane izvore.
- U **kulturalnim studijima i komunikologiji** često se citiraju **José van Dijck** (*The Culture of Connectivity*) o logikama platformi, **Nick Couldry** (medijacija, moć podataka), **Henry Jenkins** (participatorna kultura), **Zizi Papacharissi** (afektivna javnost na društvenim mrežama) — ne kao mrežni matematičari, nego kao **teorijski okvir** uz koji se mrežni nalazi čitaju.

---

## Recentna literatura

- **Russell, M. A. (2018).** *Mining the Social Web* (3. izd.). O'Reilly. Praktični primjeri i kod.
- **Bruns, A., & Burgess, J. (2015)** i kasniji radovi o **Twitter** analizi: hashtagovi, retweet mreže, metodologija.
- Radovi o **Instagram API**, **Facebook Graph API**, **X (Twitter) API v2** (2020.+): što je moguće dohvatiti, koja su ograničenja. Posebno korisna literatura o **etici** i **GDPR**-u pri istraživanju društvenih medija (npr. smjernice AoIR).
- **van Dijck, J. (2013).** *The Culture of Connectivity*. Oxford University Press. — logike platformi i korisničkih praksi.
- **Couldry, N., & Hepp, A. (2017).** *The Mediated Construction of Reality*. Polity. — kako mediji oblikuju društvenu stvarnost, uključujući digitalne slojeve.
- Za **metodologiju** kombiniranja kvantitativnih mreža s kvalitativnim čitanjem korisno je tražiti radove o **mixed methods** i **computational social science** u humanističkim disciplinama (digital humanities, medijske studije).

---

## Problemi

- **Ograničenja API-ja**: Kvote, plaćeni pristup, zabrana nekih tipova podataka. Dokumentacija se mijenja; istraživač mora provjeriti trenutne uvjete i planirati istraživanje u skladu s njima.
- **Etika i suglasnost**: Javni profili nisu nužno „javni” u smislu da istraživač može slobodno skupljati i objavljivati podatke. Potrebno je razmotriti suglasnost, anonimizaciju i transparentnost; mnoge institucije zahtijevaju etičku provjeru.
- **Pristranost**: Tko je na platformi? Korisnici nisu reprezentativni za cijelu populaciju; jezična, dobna i geografska pristranost utječu na zaključke. Treba eksplicitno navoditi granice općenitosti.
- **Zastarjelost dokumentacije**: API-ji i uvjeti korištenja mijenjaju se; knjige i članci brzo zastarjevaju. Redovita provjera službenih stranica platformi i recentne literature nužna je.
- **Tehno-determinizam**: Opis mreže (npr. „echo chamber”) lako postaje priča o **neizbježnom** ponašanju korisnika. Kulturalne studije podsjećaju da su **institucije**, **norme** i **materijalni uvjeti** uvijek prisutni — mreža je **jedan** sloj objašnjenja, ne cjelina.

---

## Kulturologija i komunikacija

Istraživanje **kulturnih zajednica**, **medijskih događaja**, **aktivizma** i **identiteta** na platformama važno je za kulturološke i komunikacijske studije. Primjeri uključuju: analizu hashtagova vezanih uz kulturne festivale ili institucije; mreže korisnika koji raspravljaju o određenim temama; ulogu influencera u širenju sadržaja. **Hrvatski i srednjoeuropski kontekst** može uključivati proučavanje lokalnih hashtagova, medijskih kuća, kulturnih ustanova ili javnih debata — uz poštivanje etike i prava.

### Od metrike do značenja

Kada interpretiramo **stupanj**, **međupoloženost** ili **zajednice** u kulturnom istraživanju, korisno je držati se tri pitanja:

1. **Što brid *kulturno* predstavlja** u mom istraživanju? (npr. solidarnost, konflikt, institucionalna podrška.)
2. **Što struktura *ne* vidi?** (privatne poruke, izbrisani tweetovi, korisnici izvan platforme.)
3. **Kako bi ovo** pročitali **sami sudionici** — slaže li se njihovo iskustvo s mojom mrežnom pričom?

Time se mrežna analiza uklapa u širi **kritički** i **refleksivni** stil kulturalnih studija, a ne reducira kulturu na graf.

---

## Kako doći do podataka

- **Javni API-ji**: X (Twitter) nudi API s ograničenjima (kvote, plaćeni tierovi); Facebook i Instagram strogo ograničavaju pristup za istraživanje. Uvijek u skladu s **ToS** i **GDPR**.
- **Javni datasetovi**: Arhive tweetova, SNAP datasetovi, ICWSM dataseti — korisni za učenje i za istraživanja koja ne zahtijevaju vlastito skupljanje. Provjeriti licence i etičke smjernice.
- **Mock podaci**: Za vježbu i demonstraciju metoda dovoljni su **sintetički** ili anonimizirani primjeri; time izbjegavamo etičke i pravne rizike dok vježbamo analizu. U pedagoškom kontekstu mock scenariji mogu **imitirati** kulturni događaj (festival, medijsku raspravu) bez stvarnih osoba.

---

## Alati

**Python**: `tweepy` (X API), `requests` za generičke API pozive; `pandas` za obradu tabličnih podataka; **NetworkX** za gradnju grafa i analizu. Alternativa: korištenje **gotovih datasetova** (npr. SNAP, ICWSM) ako odgovaraju istraživačkom pitanju.

Za **vizualizaciju** i interpretaciju u nastavi često se koriste `matplotlib` ili `plotly` (vidi poglavlje o vizualizaciji).

---

Vidi primjer: [10_online_mreze_primjer.ipynb](../code/10_online_mreze_primjer.ipynb)
