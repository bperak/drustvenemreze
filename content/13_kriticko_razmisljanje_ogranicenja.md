# 13. Kritičko razmišljanje o društvenoj mrežnoj analizi i njenim ograničenjima

Društvena mrežna analiza daje moćne alate: možemo kvantificirati strukturu, identificirati centralne čvorove, pratiti širenje. No svaki alat ima **granice**. Odluke o tome tko ulazi u mrežu, što smatramo vezom i kako tumačimo brojke direktno utječu na zaključke. **Kritičko razmišljanje** o SNA uključuje svjesnost o **metodološkim** ograničenjima (granice uzorka, kauzalnost), **epistemološkim** pitanjima (što zapravo mjerimo kada kažemo „centralnost” ili „utjecaj”) i **etičkim** obvezama (suglasnost, anonimizacija, transparentnost). Ovo poglavlje sumira ta ograničenja i daje smjernice za odgovornu praksu — kako u istraživanju tako i u interpretaciji i objavi rezultata.

---

## Teorijski koncept

SNA je **metodologija**, ne neutralsna „činjenica”. Rezultati ovise o **odlukama** istraživača: granice mreže, definicija veze, izbor mjera, način prikupljanja podataka. **Kritičko razmišljanje** znači: **(1)** eksplicitno navoditi te odluke i njihov utjecaj; **(2)** ne pretjerivati u kauzalnim tvrdnjama kada imamo samo korelacije ili strukturalne opise; **(3)** provoditi prikupljanje i objavu u skladu s etikom i pravom. Time SNA ostaje koristan alat, ali se izbjegava njegova **reifikacija** — tretiranje mjera kao da nužno opisuju „stvarnu” moć ili utjecaj bez obzira na kontekst.

---

## Definicije

- **Granice mreže**: Odluka **tko ili što** ulazi u uzorak — koji ljudi, koje stranice, koji vremenski period — **utječe na sve** brojke i zaključke. Čvorovi izvan granice ne ulaze u izračun; rubni čvorovi mogu imati drugačiju ulogu nego „unutarnji”. Granice treba obrazložiti i navesti kao ograničenje.
- **Anonimizacija**: Postupak uklanjanja ili zamjene **identifikatora** (imena, ID-ova) tako da pojedinci ne mogu biti prepoznati u objavljenim podacima. Za zaštitu ispitanika i u skladu s GDPR-om.
- **Pseudonimizacija**: Zamjena identifikatora **lažnim** ID-ovima (npr. P1, P2), uz mogućnost — u određenim uvjetima — ponovnog povezivanja s izvornim podacima. Razlikuje se od potpune anonimizacije; pravni i etički zahtjevi mogu propisivati jedan ili drugi pristup.

---

## Ključni istraživači

Brojni autori u metodologiji SNA (**Wasserman & Faust**, **Borgatti**) raspravljaju **ograničenja** mjera, uzorkovanja i interpretacije. **Etičke smjernice** za istraživanje društvenih medija i online podataka nude organizacije poput **AoIR** (Association of Internet Researchers) i nacionalna tijela za etiku istraživanja; važno je upoznati se s aktualnim verzijama smjernica i s institucionalnim zahtjevima (etičko povjerenstvo).

---

## Recentna literatura

- **Lazer, D. et al. (2014).** The parable of Google Flu: Traps in big data analysis. *Science*. Klasičan primjer ograničenja velikih podataka i pretjeranog povjerenja u algoritme; poučan za kritički odnos prema „big data” i mrežnim metrikama.
- **Smjernice o etici istraživanja društvenih medija** (AoIR, 2019 i kasnije); **GDPR** u akademskom istraživanju — što smijemo skupljati, kako čuvati, kada anonimizirati i kako dokumentirati.

---

## Problemi

- **Granice uzorka i selektivnost**: Tko nije u mreži? Ako proučavamo samo aktivne korisnike platforme, gubimo one koji ne sudjeluju; ako proučavamo samo one koji su odgovorili na anketu, imamo selektivnost odgovora. Rezultati vrijede za **definiranu** populaciju, ne nužno za „društvo” općenito.
- **Kauzalnost**: Mreža **korelacija** (tko s kime povezan) **nije** uzročnost. Ljudi sličnih stavova često se međusobno povezuju (homofilija); struktura može **odražavati** stavove, a ne nužno **uzrokovati** ih. Treba biti oprezan u jeziku („povezano s”, „može doprinijeti” umjesto „uzrokuje” osim ako dizajn to podržava).
- **Etička pitanja**: Suglasnost ispitanika, anonimizacija pri objavi, poštivanje ToS platformi, transparentnost metode — sve to dio je odgovorne prakse. Istraživanje bez etičke provjere može nanijeti štetu i ugroziti valjanost znanosti.
- **Reproducibilnost i transparentnost**: Dokumentiranje koraka (što smo skupljali, kako smo čistili podatke, koje mjere smo računali) omogućuje drugima da provjere i repliciraju rezultate. Bez toga zaključci teško mogu biti evaluirani.

---

## Implikacija

Rezultate SNA treba **interpretirati uz napomenu o granicama**: za koju populaciju vrijede, koje su odluke utjecale na strukturu i na brojke, što mjere zapravo predstavljaju. Prikupljanje i objavu podataka treba provoditi u skladu s **etikom** i **pravom** (GDPR, ToS, institucionalne smjernice). Kritičko razmišljanje nije „protiv” SNA — omogućuje njezinu **odgovornu** i **kredibilnu** primjenu.

---

Vidi primjer: [13_etika_anonimizacija.ipynb](../code/13_etika_anonimizacija.ipynb)
