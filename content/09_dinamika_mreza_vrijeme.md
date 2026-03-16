# 9. Dinamika mreža i promjene u vremenu

Mreže nisu statične. Ljudi stječu i gube prijatelje; na platformama se broj sljedbenika mijenja; suradnje i koautorstva nastaju i prestaju. **Dinamika mreža** odnosi se na proučavanje **promjena** u strukturi mreže tijekom vremena: koji se čvorovi i bridovi pojavljuju ili nestaju, kako se mijenjaju gustoća, centralnost ili zajednice. Takva pitanja važna su za razumijevanje evolucije zajednica, širenja fenomena ili stabilnosti odnosa. Ovo poglavlje uvodi osnovne koncepte vremenskih mreža, načine na koje ih modeliramo (niz snimaka, vremenski označeni bridovi) i tipične metode analize, uz napomenu o dostupnosti podataka i izboru vremenske rezolucije.

---

## Teorijski koncept

**Dinamička analiza** društvenih mreža pretpostavlja da je graf **funkcija vremena**: na svakom trenutku t možemo definirati skup čvorova i bridova. Promjene mogu uključivati **dodavanje ili uklanjanje** čvorova i bridova, **promjenu težina** ili **reorganizaciju** zajednica. Cilj je opisati i, ako je moguće, objasniti te promjene: Jesu li neki čvorovi sve centralniji? Raspadaju li se zajednice ili se stvaraju nove? Koji događaji (npr. kriza, nova platforma) koreliraju s promjenama? Time dinamika mreža povezuje SNA s longitudinalnim istraživanjima i s pitanjima evolucije društvenih i kulturnih struktura.

---

## Definicije

- **Vremenska mreža (temporal network)**: Mreža u kojoj je **vrijeme** eksplicitno uključeno. Dva su uobičajena pristupa: **(1)** niz **snimaka** (snapshots) grafa na vremenskim točkama t₁, t₂, …; **(2)** graf u kojem su na bridovima (ili čvorovima) **vremenske oznake** — npr. kada je veza nastala ili koliko je trajala. Izbor ovisi o dostupnim podacima i o pitanju (npr. evolucija zajednica vs. vremenski poredak interakcija).
- **Stabilnost**: Koliko se mjere (npr. centralnost pojedinih čvorova, modularnost, broj zajednica) **mijenjaju** između vremenskih točaka. Niska stabilnost može značiti da je mreža u brzoj promjeni ili da je mjera osjetljiva na male promjene u podacima.
- **Evolucija zajednica**: Pitanje kako se **zajednice** (klasteri) mijenjaju u vremenu: spajaju li se, dijele, nestaju. Zahtijeva usporedbu particija na različitim vremenskim točkama (npr. pomoću mjera sličnosti particija).

---

## Ključni istraživači

- **National Research Council** (ur.) u publikaciji *Dynamic Social Network Modeling and Analysis* daje pregled ranih pristupa modeliranju i analizi dinamičkih mreža u sociologiji i srodnim disciplinama.
- Literatura o **temporalnim mrežama** i **evolving graphs** u fizici i informatici (npr. **Holme, Saramäki**) razvija formalne modele i mjere za mreže s vremenskom dimenzijom.

---

## Recentna literatura

- **Holme, P., & Saramäki, J. (2012).** Temporal networks. *Physics Reports*. Opsežan pregled koncepta i mjera za vremenske mreže.
- Korisno tražiti radove od cca. 2015. nadalje o **dinamici online mreža** (Twitter, koautorstvo, citiranje): kako mreže rastu, kako se zajednice mijenjaju, koji su uzorci stabilnosti i promjene.

---

## Problemi

- **Dostupnost vremenskih podataka**: Za dinamičku analizu potrebni su podaci na **više vremenskih točaka** ili s vremenskim oznakama. Ankete se obično provode u jednom trenutku; platforme ponekad nude povijest, ali API-ji često ograničavaju pristup. Retrospektivni podaci („tko ste poznavali prije pet godina?”) podložni su pristranosti sjećanja.
- **Odabir vremenske rezolucije**: Dnevno, tjedno, godišnje? Previše fina rezolucija može dati bučne podatke; previše gruba gubi važne prijelaze. Odluka ovisi o tipu procesa koji proučavamo.
- **Agregacija vs. fine-grained analiza**: Ponekad agregiramo sve interakcije u jedan graf za cijelo razdoblje; drugi put analiziramo snimke. Različiti pristupi odgovaraju na različita pitanja (npr. ukupna struktura vs. redoslijed događaja).

---

## Primjer u stvarnom svijetu

- **Evolucija mreže sljedbenika**: Kako se mreža praćenja nekog korisnika ili teme mijenja mjesecima ili godinama; tko postaje centralniji, kako se klasteri reorganiziraju.
- **Promjene u koautorstvu**: Mreža koautorstva u nekoj znanstvenoj disciplini kroz desetljeća; pojavljivanje novih „hubova”, raspad ili stapanje grupa.
- **Metode**: Usporedba **snimaka** na t₁, t₂, … (izračun mjera za svaki snimak, usporedba); **vremenske serije** metrika (npr. gustoća, broj zajednica) za opis trenda; u naprednijim pristupima — modeli koji eksplicitno modeliraju nastanak i nestanak bridova u vremenu.

---

Vidi primjer: [09_dinamika_mreza.ipynb](../code/09_dinamika_mreza.ipynb)
