# 9. Dinamika mreža i promjene u vremenu

Mreže nisu statične. Ljudi stječu i gube prijatelje; na platformama se broj sljedbenika mijenja; suradnje i koautorstva nastaju i prestaju. **Dinamika mreža** odnosi se na proučavanje **promjena** u strukturi mreže tijekom vremena: koji se čvorovi i bridovi pojavljuju ili nestaju, kako se mijenjaju gustoća, centralnost ili zajednice. Takva pitanja važna su za razumijevanje evolucije zajednica, širenja fenomena ili stabilnosti odnosa. Ovo poglavlje uvodi osnovne koncepte vremenskih mreža, načine na koje ih modeliramo (niz snimaka, vremenski označeni bridovi) i tipične metode analize, uz napomenu o dostupnosti podataka i izboru vremenske rezolucije.

U **kulturalnim studijima** dinamika mreže nije samo tehničko pitanje (što se događa s bridovima), nego i pitanje **kako se kultura reproducira, transformira i osporava** kroz odnose: tko s kim ulazi u vezu, kada se mreža zatvara pred novim glasovima, kako platforme arhiviraju ili brišu prošlost. Analiza u vremenu povezuje mrežnu strukturu s **poviješću prakse**, s **politikom platformi** i s načinom na koji se **identitet, pripadnost i značenje** preoblikuju kroz interakcije.

---

## Teorijski koncept

**Dinamička analiza** društvenih mreža pretpostavlja da je graf **funkcija vremena**: na svakom trenutku t možemo definirati skup čvorova i bridova. Promjene mogu uključivati **dodavanje ili uklanjanje** čvorova i bridova, **promjenu težine** ili **reorganizaciju** zajednica. Cilj je opisati i, ako je moguće, objasniti te promjene: Jesu li neki čvorovi sve centralniji? Raspadaju li se zajednice ili se stvaraju nove? Koji događaji (npr. kriza, nova platforma) koreliraju s promjenama? Time dinamika mreža povezuje SNA s longitudinalnim istraživanjima i s pitanjima evolucije društvenih i kulturnih struktura.

Iz perspektive teorije kulture, vremenska dimenzija podsjeća da **nema „zamrznutog” kulturnog poretka** izvan procesa: ono što danas izgleda kao stabilna scena (npr. žanr, subkultura, „algoritamska zajednica”) nastaje iz niza poteza, rituala, cirkulacije tekstova i institucionalnih odluka. Mrežni snimci mogu vizualizirati **trenutak** u tom procesu; usporedba snimaka pomaže učitati **tenziju između kontinuiteta i prijeloma** — što u kulturalnim studijima često teoriziramo kao odnos dominantnog, rezidualnog i emergentnog (Williams), kao promjenu **pozicija čitanja** publike (Hall) ili kao **mobilnost** kulturnih elemenata kroz globalizirane medijske i migracijske tokove (Appadurai).

---

## Dinamika mreža i kulturalni studiji

**1. Mreža kao povijest odnosa, ne samo kao „slika”.**  
Kulturalni studiji dugo naglašavaju da su značenje i moć **relacijske** — proizlaze iz pozicija unutar polja, iz rasa, spola, klase, jezika i institucija. Dinamička mreža formalizira tu relacijsku intuiciju: umjesto jednog statičnog grafa, dobivamo **niz ili tijek** grafova koji pokazuju tko je bio povezan s kim i kada. To je blisko **etnografskom** pristupu koji prati kako se zajednice sklapaju i raspadaju (npr. fanovske scene, aktivizam, umjetničke suradnje), ali dodaje **agregirani** pregled strukture koja se inače teško drži u glavi.

**2. Platforme, arhivi i „što se može mjeriti”.**  
Online kulturna produkcija često ovisi o platformama koje **mijenjaju API, pravila skladištenja ili vidljivost** sadržaja. Longitudinalna mrežna analiza tada nije neutralna: ona mjeri **on što platforma još dopušta izvući** u vrijeme t₁, t₂, … Nestanak čvorova ili bridova može biti **kulturni događaj** (odlazak zajednice na drugu platformu, brisanje računa, shadowban) koliko i „prirodna” socijalna promjena. Kulturalni studiji upozoravaju da se **arhivabilnost** i **trajnost** same po sebi politički i ekonomski uvjetuju — dinamika mreže u podacima odražava i **dinamiku moći platforme**.

**3. Participatorna kultura i evolucija veza.**  
Istraživanja participatorne kulture (npr. fanovskih praksi, remiksa, kolektivnog stvaranja znanja) pokazuju da se **uloge** (tko je „organizator”, tko „amatuer”, tko „profesionalac”) i **topologija suradnje** mijenjaju: novi događaji (konvencija, skandal, nova sezona serije) mogu brzo preusmjeriti pažnju i preoblikovati mrežu mentiona, citiranja ili zajedničkog rada. Dinamički snimci mogu ilustrirati **faze** takvog ciklusa (npr. koncentracija pažnje na malu jezgru, zatim difuzija na rubove).

**4. Afekt, pažnja i „brza” vremenska skala.**  
Kulturni fenomeni na društvenim mrežama često imaju **intenzivna, kratkotrajna** dinamička lica (viralnost, trendovi). Tu se vremenska rezolucija analize izravno dodiruje s pitanjem **kako se afekt i javnost sklapaju u digitalnom okruženju** — ne kao stabilna publika, nego kao **pulsirajući** skup veza i reakcija. Mreža u vremenu nije samo sociološki „ego mreža kroz godine”; može biti i **satni ili dnevni** snimak koji povezuje kulturne studije s proučavanjem **događaja** i **ritma** medijskog života.

**5. Etika i tumačenje promjene.**  
Kada brid nestane, istraživač ne smije pretpostaviti da je „odnos nestao u stvarnosti”: možda je nestao **trag** u korpusu. Kulturalni studiji naglašavaju **refleksivnost** i **situiranost** znanja; dinamička SNA treba spariti kvantitativne usporedbe s **kvalitativnim** kontekstom (intervjui, arhiva, diskursna analiza) kako bi se promjene mreže čitale kao **kulturne i političke**, a ne samo kao brojčane fluktuacije.

---

## Definicije

- **Vremenska mreža (temporal network)**: Mreža u kojoj je **vrijeme** eksplicitno uključeno. Dva su uobičajena pristupa: **(1)** niz **snimaka** (snapshots) grafa na vremenskim točkama t₁, t₂, …; **(2)** graf u kojem su na bridovima (ili čvorovima) **vremenske oznake** — npr. kada je veza nastala ili koliko je trajala. Izbor ovisi o dostupnim podacima i o pitanju (npr. evolucija zajednica vs. vremenski poredak interakcija).
- **Stabilnost**: Koliko se mjere (npr. centralnost pojedinih čvorova, modularnost, broj zajednica) **mijenjaju** između vremenskih točaka. Niska stabilnost može značiti da je mreža u brzoj promjeni ili da je mjera osjetljiva na male promjene u podacima. U kulturalnim studijima stabilnost se često mora **kvalitativno** povezati s pitanjem: stabilnost **čega** — javnog diskursa, institucija, alata za prikupljanje?
- **Evolucija zajednica**: Pitanje kako se **zajednice** (klasteri) mijenjaju u vremenu: spajaju li se, dijele, nestaju. Zahtijeva usporedbu particija na različitim vremenskim točkama (npr. pomoću mjera sličnosti particija). Kulturno relevantno je pitati i **tko** ostaje u istoj zajednici kroz snimke, a **tko** „ispada” iz vizualizacije zbog marginalizacije ili gubitka podataka.
- **Preklapanje snimaka (npr. Jaccardov indeks bridova)**: Jednostavna mjera koliko se skup bridova u t₁ podudara s bridovima u t₂. Korisna kao prvi signal **kontinuiteta vs. promjene** strukture prije složenijih modela.

---

## Ključni istraživači i smjerovi

- **National Research Council** (ur.) u publikaciji *Dynamic Social Network Modeling and Analysis* daje pregled ranih pristupa modeliranju i analizi dinamičkih mreža u sociologiji i srodnim disciplinama.
- Literatura o **temporalnim mrežama** i **evolving graphs** u fizici i informatici (npr. **Holme, Saramäki**) razvija formalne modele i mjere za mreže s vremenskom dimenzijom.
- **Manuel Castells** u *The Rise of the Network Society* povezuje mrežnu logiku s transformacijom kapitalizma i medija; dinamički aspekt ovdje nije formalni graf, nego **povijesna** teza o tome kako se prostor, vrijeme i moć preoblikuju kroz mreže — korisno kao **teorijski okvir** uz koji se empirijski snimci mogu tumačiti.
- **Henry Jenkins** (participatorna kultura, konvergencija) i radovi iz **fan studies** pružaju bogate primjere **promjenjivih** mreža suradnje, citiranja i distribucije tekstova između amatera i profesionalaca.
- **danah boyd** i istraživanja **platformiziranog** društvenog života upozoravaju na to kako **dizajn platformi** oblikuje vidljivost veza i trajnost podataka — što je metodološki uvjet za bilo koju longitudinalnu mrežnu analizu kulturnih praksi online.

---

## Recentna literatura

- **Holme, P., & Saramäki, J. (2012).** Temporal networks. *Physics Reports*. Opsežan pregled koncepta i mjera za vremenske mreže.
- Korisno tražiti radove od cca. 2015. nadalje o **dinamici online mreža** (Twitter/X, koautorstvo, citiranje): kako mreže rastu, kako se zajednice mijenjaju, koji su uzorci stabilnosti i promjene.
- Za **kulturni kontekst** digitalnog života i javnosti: **Papacharissi, Z.** (npr. *Affective Publics*) — o dinamici pažnje i političkog izražavanja; **Gillespie, T.** o **governance** platformi i kategorijama koje filtriraju vidljivost; **van Dijck, J.** o **kulturi povezivosti** i komodifikaciji društvenosti. Ti tekstovi ne zamjenjuju formalnu analizu grafova, ali pomažu **objasniti** zašto se mreže u podacima ponašaju onako kako se ponašaju.

---

## Problemi

- **Dostupnost vremenskih podataka**: Za dinamičku analizu potrebni su podaci na **više vremenskih točaka** ili s vremenskim oznakama. Ankete se obično provode u jednom trenutku; platforme ponekad nude povijest, ali API-ji često ograničuju pristup. Retrospektivni podaci („tko ste poznavali prije pet godina?”) podložni su pristranosti sjećanja.
- **Odabir vremenske rezolucije**: Dnevno, tjedno, godišnje? Previše fina rezolucija može dati bučne podatke; previše gruba gubi važne prijelaze. Odluka ovisi o tipu procesa koji proučavamo — i o **kulturnoj skali** (događaj vs. desetljeće subkulture).
- **Agregacija vs. fine-grained analiza**: Ponekad agregiramo sve interakcije u jedan graf za cijelo razdoblje; drugi put analiziramo snimke. Različiti pristupi odgovaraju na različita pitanja (npr. ukupna struktura vs. redoslijed događaja).
- **Selekcija i reprezentativnost**: Tko je uopće u korpusu kroz vrijeme? Migracije korisnika, jezične barijere i ekonomija pažnji mogu učiniti da „dinamika mreže” u stvari mjeri **dinamiku uzorka**, a ne cijelu scenu.
- **Privatnost**: Longitudinalni podaci često su osjetljiviji od presječnih; ponovna uporaba ili dijeljenje snimaka može **identificirati** pojedince kroz vrijeme čak i uz pseudonime.

---

## Primjer u stvarnom svijetu

- **Evolucija mreže sljedbenika**: Kako se mreža praćenja nekog korisnika ili teme mijenja mjesecima ili godinama; tko postaje centralniji, kako se klasteri reorganiziraju.
- **Promjene u koautorstvu**: Mreža koautorstva u nekoj znanstvenoj disciplini kroz desetljeća; pojavljivanje novih „hubova”, raspad ili stapanje grupa.
- **Kulturne scene i suradnje**: Mreža suradnika na festivalima, u nezavisnoj glazbi ili u **crossover** fanovskih praksi — snimci prije/poslije ključnog događaja (otkazivanje, skandal, nova sezona) pokazuju pomicanje **jezgre** i **periferije**.
- **Metode**: Usporedba **snimaka** na t₁, t₂, … (izračun mjera za svaki snimak, usporedba); **vremenske serije** metrika (npr. gustoća, broj zajednica) za opis trenda; **preklapanje bridova** između snimaka; u naprednijim pristupima — modeli koji eksplicitno modeliraju nastanak i nestanak bridova u vremenu.

---

Vidi primjer: [09_dinamika_mreza.ipynb](../code/09_dinamika_mreza.ipynb)
