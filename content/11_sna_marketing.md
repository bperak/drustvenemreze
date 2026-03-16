# 11. Primjena društvene mrežne analize u marketinškim istraživanjima

Tko u mreži potrošača ili korisnika platforme ima najveći „doseg”? Kako se informacija o brendu ili proizvodu širi od usvajača do drugih? Marketing i brendovi sve više ovise o **word-of-mouth** i o **influencerima** — pojedincima čiji stavovi i preporuke dosežu širu mrežu. Društvena mrežna analiza pruža alate da te **mrežne pozicije** identificiramo i da mapiramo širenje poruka. Ovo poglavlje uvodi primjenu SNA u marketinškim istraživanjima: od definicije „influencera” u mrežnom smislu do metoda identifikacije ključnih čvorova i do etičkih i metodoloških ograničenja takvih analiza.

---

## Teorijski koncept

SNA u marketingu služi nekoliko ciljeva: **(1) identifikacija influencera** — čvorova s visokom centralnošću ili velikim dosegom u mreži preporuka ili sljedbenika; **(2) mapiranje širenja** informacija o brendovima ili kampanjama kroz veze (povezano s difuzijom, pogl. 8); **(3) segmentacija** potrošača na temelju mrežnog položaja (npr. tko je u jezgru, tko na periferiji). Teorijski okvir često kombinira klasičnu SNA literaturu (centralnost, weak ties, mostovi) s marketing literaturom o word-of-mouth i viralnom marketingu. Važno je razlikovati **mrežnu** definiciju utjecaja (položaj, doseg) od **stvarnog** utjecaja na ponašanje; SNA nudi proxy mjere koje se mogu validirati ili koristiti u kombinaciji s drugim podacima.

---

## Definicije

- **Influencer (u mrežnom smislu)**: Čvor (pojedinac, stranica, račun) s **visokom centralnošću** ili **velikim dosegom** u relevantnoj mreži — npr. mreža sljedbenika, preporuka proizvoda ili interakcija (like, dijeljenje). Često se operacionalizira putem **degree** (broj direktnih veza), **betweenness** (most između grupa) ili **eigenvector** (povezan s drugim „važnim” čvorovima). To ne jamči stvarni utjecaj na kupnju ili stav, ali identificira kandidate za kampanje ili daljnje mjerenje.
- **Viralni marketing**: Strategija koja se oslanja na **širenje poruke kroz mrežu** veza — korisnici prenose poruku drugima, koji prenose dalje. Povezano s teorijom difuzije (pogl. 8) i s dizajnom kampanja koje ciljaju „konektore” ili rané usvajače.

---

## Ključni istraživači

Klasična SNA literatura (**Wasserman & Faust**, **Borgatti** i suradnici) daje metodologiju i mjere; primjena na **potrošače** i **brendove** razvijena je u marketinškoj literaturi o word-of-mouth, mrežama preporuka i utjecaju. Radovi o **mrežama preporuka** i **difuziji inovacija** u kontekstu proizvoda povezuju se s Rogersom i s empirijskim studijama širenja kupovnih navika.

---

## Recentna literatura

- **Trusov, M., Bucklin, R. E., & Pauwels, K. (2009).** Effects of word-of-mouth versus traditional marketing: Findings from an online social network. *Journal of Marketing*. Jedan od utjecajnih radova o mjerenju utjecaja word-of-mouth u online mrežama.
- Korisno tražiti radove od cca. 2015. nadalje o **influencer marketingu** i **mrežama na društvenim medijima**: kako brendovi identificiraju partnere, kako mjeriti uspjeh kampanja i koja su etička pitanja targetiranja i transparentnosti.

---

## Problemi

- **Granica između „utjecaja” i popularnosti**: Visok broj sljedbenika ili centralnost ne znači nužno da netko mijenja ponašanje drugih. Može biti i obrnuto: popularni su zato što odražavaju već postojeće preference. Treba biti oprezan u jeziku i u zaključcima.
- **Etika targetiranja**: Korištenje mrežnih podataka za ciljano oglašavanje ili manipulaciju može izazvati pitanja privatnosti i autonomije. Transparentnost i suglasnost važni su u istraživanju i u praksi.
- **Reprezentativnost**: Podaci s platformi ne predstavljaju nužno sve potrošače ili cijelo tržište; jezična, dobna i kulturna pristranost utječu na općenitost zaključaka.

---

## Primjer u stvarnom svijetu

- **Mreža preporuka proizvoda**: Tko kome preporučuje proizvod (anketa ili digitalni trag); iz gradnje grafa identificiraju se čvorovi s visokim betweenness ili degree kao potencijalni „širitelji” preporuke.
- **Identifikacija ključnih čvorova za kampanju**: Ako želimo da poruka dosegne što više ljudi ili specifične segmente, možemo odabrati čvorove koji imaju pristup tim segmentima (npr. mostovi između zajednica). Mock podaci ili javni datasetovi pogodni su za vježbu bez etičkih rizika.

---

Vidi primjer: [11_marketing_primjer.ipynb](../code/11_marketing_primjer.ipynb)
