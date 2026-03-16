# 4. Socijalni kapital i društvene mreže

Koncept **socijalnog kapitala** odgovara na pitanje: zašto neki ljudi i zajednice uspijevaju bolje od drugih ne samo zbog novca ili obrazovanja, nego zbog **veza** — povjerenja, reciprociteta, mreža podrške i pristupa informacijama. Te veze nisu samo „dodatak”; one stvaraju resurse: tko može zatražiti pomoć, tko doznaje za priliku, tko može mobilizirati druge. Istraživanje društvenih mreža pruža alat da tu ideju operacionaliziramo: struktura mreže — gustoća, broj veza, položaj „mostova” — može se mjeriti i povezivati s ishodima na razini pojedinca ili zajednice. Ovo poglavlje povezuje klasične teorije socijalnog kapitala (Putnam, Lin) s mrežnim mjerama i pokazuje kako kulturološki i komunikacijski kontekst daje tom mjerenju smisao.

---

## Teorijski koncept

Socijalni kapital označava **vrijednost koju donose društvene veze**: povjerenje, norme reciprociteta, mreže podrške i pristup resursima (informacije, poslovi, pomoć). U SNA-u taj se koncept prevodi u **strukturu mreže**: gustoća veza, broj jakih i slabih veza, položaj čvora (npr. betweenness kao „most” između grupa). Time možemo testirati hipoteze: imaju li ljudi s bogatijom mrežom pristup boljim informacijama? Je li kohezivnija zajednica sklonija kolektivnom djelovanju? Različiti autori naglašavaju različite aspekte — od povjerenja i sudjelovanja u zajednici (Putnam) do pristupa resursima kroz poziciju u mreži (Lin) — ali zajedničko im je da **veze i njihov oblik** nisu epifenomen nego dio objašnjenja društvenih i kulturnih ishoda.

---

## Definicije

- **Socijalni kapital**: U literaturi se definira na više načina. **Nan Lin** ga povezuje s resursima dostupnim kroz odnose s drugima: informacije, utjecaj, emocionalna podrška. **Robert Putnam** naglašava sklonost građana sudjelovati u zajedničkim aktivnostima i povjerenje prema drugima; u tom smislu socijalni kapital je i svojstvo zajednice. U mrežnoj analizi često operacionaliziramo kapital putem **strukture**: broj veza, tip veza (jake/slabe), položaj u mreži (centralnost, betweenness).
- **Bonding (povezivanje unutar grupe)**: Veze koje ojačavaju koheziju unutar jedne grupe — prijateljstva, obitelj, bliska zajednica. Povezuju se s emocionalnom podrškom i zajedničkim identitetom.
- **Bridging (povezivanje između grupa)**: Veze koje spajaju različite grupe ili segmente društva. Čvorovi s visokim betweenness često imaju „bridging” ulogu; povezuju se s pristupom novim informacijama i inovacijama.

Razlíka bonding / bridging važna je za pitanja inkluzije, širenja ideja i društvene kohezije.

---

## Ključni istraživači

- **Robert D. Putnam** u knjizi *Bowling Alone: The Collapse and Revival of American Community* raspravlja o „nestanku” društvenog kapitala u SAD-u — smanjenju sudjelovanja u udrugama, crkvama, lokalnim aktivnostima — i o posljedicama za demokraciju i zajednicu. Njegov rad popularizirao je pojam i potaknuo empirijska istraživanja na razini zajednica.
- **Nan Lin** u *Social Capital: A Theory of Social Structure and Action* daje teorijski okvir u kojem je socijalni kapital resurs koji proizlazi iz **pozicije u mreži** i **pristupa** drugim akterima. Time se koncept izravno povezuje s mjerenjem mrežne strukture (centralnost, raznovrsnost veza, weak ties).

Oba pristupa — Putnamov na razini zajednice i Linov na razini pojedinca i mreže — korisna su za dizajn istraživanja i interpretaciju rezultata.

---

## Recentna literatura

- **Lin, N. (2001).** *Social Capital: A Theory of Social Structure and Action*. Cambridge University Press. (I novija izdanja i nadogradnje.)
- Korisno je tražiti radove od otprilike 2015. nadalje o **mjerenju socijalnog kapitala u online mrežama** i putem digitalnih podataka: kako broj prijatelja ili sljedbenika, tipovi interakcija ili struktura mreže koreliraju s percipiranom podrškom, informacijskim pristupom ili kolektivnim djelovanjem.

---

## Problemi

- **Operacionalizacija**: „Socijalni kapital” je apstraktan pojam; u istraživanju ga moramo pretvoriti u mjerljive varijable. Moguće je mjeriti strukturu (gustoća, betweenness) ili percipiranu podršku (ankete). Nije nužno da se te dvije stvari podudaraju: netko može imati puno veza, ali malo povjerenja ili obrnuto. Treba biti jasan što zapravo mjerimo.
- **Kauzalnost**: Povezanost između mrežne strukture i ishoda (npr. pronalazak posla) ne dokazuje uzročnost; moguće je da i veze i ishod ovise o trećem čimbeniku (npr. osobina ličnosti). Pažnja na dizajn istraživanja i interpretaciju.

---

## Primjer u stvarnom svijetu

- Mjerenje **gustoće** i **broja veza** u lokalnoj zajednici (npr. koliko ljudi poznaje susjede, sudjeluje u udrugama) i povezivanje s percipiranom kvalitetom života ili spremnošću za kolektivnu akciju.
- **Povezanost između udruga** ili institucija: tko s kime surađuje, dijele resurse ili informacije. Betweenness može identificirati „hub” organizacije.
- **Pristup informacijama** kroz mrežu: u anketi pitati tko je od koga doznao za priliku (posao, događaj); zatim graditi mrežu i analizirati putove informacija.

U kulturološkom kontekstu primjeri uključuju mreže umjetnika, izdavača ili kulturnih ustanova i pitanja pristupa resursima i utjecaju.

---

## Kulturologija i komunikacija

Kulturološki i komunikacijski studiji koriste koncept socijalnog kapitala za analizu **povjerenja**, **razmjene znanja** i **kolektivnog djelovanja** unutar institucija (muzeji, mediji, udruge) i zajednica. Pitanja tipa: Tko ima pristup odlučivanju? Kako se informacije i norme šire kroz kulturne scene? Kako mreže podrške utječu na kreativnost ili na mobilizaciju? — povezuju se s mjerenjem mrežne strukture i s teorijom bonding / bridging.

---

## Kako doći do podataka, modelirati mrežu i koje alate koristiti

Podatke za proučavanje socijalnog kapitala često prikupljamo putem **anketa** s pitanjima tipa name generator („Navedi ljude s kojima razgovaraš o važnim stvarima” ili „Tko ti može pomoći u potrazi za poslom”). Iz odgovora gradimo **egocentrične mreže** (jedan ispitanik + njegove veze) ili **cijelu mrežu** ako anketa obuhvaća definiranu populaciju. Čvorovi su obično osobe; bridovi mogu biti različitih tipova (emocionalna podrška, informacije, suradnja). Alati za analizu uključuju NetworkX, UCINet i Gephi za vizualizaciju i izračun gustoće, stupnja i betweenness.

---

## Rezultati i implikacija

Tipični rezultati uključuju **indekse gustoće** (koliko je mreža povezana), **broj jakih i slabih veza** (Granovetterov koncept weak ties), **betweenness** za identificiranje „mostova” između grupa. **Implikacija**: struktura mreže — tko je s kime povezan i u kojoj poziciji — povezana je s pristupom resursima, informacijama i mogućnošću kolektivnog djelovanja. Time socijalni kapital postaje ne samo metafora nego mjerljiv koncept s primjenama u istraživanju zajednica, institucija i kulture.

---

Vidi primjer: [04_socijalni_kapital_primjer.ipynb](../code/04_socijalni_kapital_primjer.ipynb)
