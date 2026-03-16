# 8. Difuzija inovacija i utjecaj u društvenim mrežama

Kako se nova ideja, navika ili proizvod širi od pojedinaca do šire populacije? Zašto neke poruke postaju „viralne”, a druge nestanu? Pitanja **difuzije** — širenja neke karakteristike kroz veze u mreži — središnja su za komunikologiju, marketing, javno zdravstvo i proučavanje društvenih pokreta. Mreža nije samo pozornica; **struktura** mreže utječe na to tko će što prihvatiti i kada. **Utjecaj** pojedinaca — sposobnost da promijene ponašanje ili mišljenje drugih — često se povezuje s **položajem** u mreži: centralni čvorovi ili „mostovi” između grupa mogu imati posebnu ulogu. Ovo poglavlje uvodi klasične teorije difuzije (Rogers, Gladwell), povezuje ih s mrežnim mjerama i raspravlja ograničenja i etičke aspekte mjerenja „utjecaja”.

---

## Teorijski koncept

**Difuzija inovacija** opisuje proces kojim se nova ideja, praksa ili proizvod širi kroz populaciju putem **veza** između ljudi: usvajanje ovisi o tome što drugi u mreži rade ili preporučuju. Teorija i modeli difuzije (npr. Rogersove faze, S-krivulja usvajanja) povezuju se s mrežnom strukturom: tko ima više veza, tko povezuje različite grupe, koliko je mreža gusto ili rijetko povezana. **Utjecaj** u tom kontekstu označava sposobnost pojedinca (ili čvora) da potakne druge na promjenu ponašanja ili mišljenja. U mrežnoj analizi utjecaj se često **operacionalizira** putem mjera centralnosti (degree, betweenness, eigenvector) ili putem modela širenja (tko bi „zarazio” najviše drugih kada bi prvi usvojio inovaciju). Važno je imati na umu da su to **proxy** mjere: položaj u mreži ne jamči stvarni kauzalni utjecaj, ali pruža hipoteze i smjernice za istraživanje.

---

## Definicije

- **Difuzija**: Širenje neke **karakteristike** (informacija, inovacija, ponašanje, virus) kroz **veze** u mreži. Jedinice (čvorovi) prelaze iz jednog stanja u drugo (npr. „nije čuo” → „čuo”; „nije usvojio” → „usvojio”) pod utjecajem susjeda ili putem bridova. Modeli difuzije opisuju uvjete i brzinu tog širenja.
- **Utjecaj**: Sposobnost pojedinca ili čvora da **promijeni** ponašanje ili mišljenje drugih. U empirijskom istraživanju često se mjeri posredno: položaj u mreži (centralnost, broj direktnih veza, uloga mosta) ili rezultat modela širenja („ako bi ovaj čvor prvi usvojio, koliko bi drugih uslijedilo?”).
- **Tipping point**: Trenutak u procesu difuzije kada **brzina** usvajanja naglo raste i inovacija prelazi na širu populaciju. Gladwell i drugi povezuju ga s ulogom posebnih tipova aktera („konektori”, „maveni”) i s gustoćom mreže.

---

## Ključni istraživači

- **Everett M. Rogers** u knjizi *Diffusion of Innovations* (prvo izdanje 1962., kasnija ažurirana) opisuje **faze** difuzije i **tipove usvajača** (inovatatori, rana većina, kasna većina, zaostali). Njegov rad temelj je za proučavanje širenja inovacija u poljoprivredi, zdravstvu, tehnologiji i medijima.
- **Malcolm Gladwell** u *The Tipping Point* popularizira ideju da mali broj posebno povezanih ili uvjerljivih pojedinaca — „maveni”, „konektori”, „prodavači” — može potaknuti epidemiju promjene. Knjiga je više esejištička nego strogo znanstvena, ali je utjecajna na rasprave o viralnosti i utjecaju.

Oba autora povezuju se s mrežnim pristupom: struktura veza i položaj aktera objašnjavaju zašto se neke stvari šire brzo, a druge ne.

---

## Recentna literatura

- **Rogers, E. M. (2003).** *Diffusion of Innovations* (5. izd.). Free Press. Standardna referenca.
- **Centola, D. (2018).** *How Behavior Spreads: The Science of Complex Contagions*. Princeton University Press. Suvremeni pristup difuziji ponašanja i ulozi mrežne strukture (npr. potreba za višestrukim kontaktima za složene kontagije).
- Korisno tražiti radove od cca. 2015. nadalje o **viralnosti** i **utjecaju** na društvenim medijima: mjerenje širenja hashtagova, retweetova, dezinformacija; etički i metodološki izazovi.

---

## Problemi

- **Kauzalnost**: Korelacija između položaja u mreži i usvajanja ne dokazuje da je **mreža** uzrok. **Homofilija** — slični se međusobno povezuju i slično se ponašaju — može stvarati iluziju „utjecaja”: ljudi mogu usvojiti nešto zato što su slični onima koji su već usvojili, a ne nužno zato što su „pod utjecajem”. Kontrolirani dizajni i longitudinalni podaci pomažu u razlučivanju.
- **Mjerenje utjecaja**: Broj sljedbenika ili centralnost **ne mjeri** izravno stvarni utjecaj na ponašanje ili mišljenje. To su proxy mjere; njihova valjanost ovisi o kontekstu i o istraživačkom pitanju. Treba biti oprezan u jeziku („potencijalni utjecaj”, „položaj pogodan za širenje”) i u zaključcima.

---

## Primjer u stvarnom svijetu

- **Širenje hashtaga na X/Twitteru**: Tko prvi koristi hashtag, tko ga preuzima, kako se mreža retweetova ili mentiona širi. Analiza vremenskog slijeda i mrežne pozicije ranih usvajača.
- **Adopcija inovacije u organizaciji**: Tko uvodi novu praksu ili alat; kako se širi po odjelima. Mreža suradnje ili komunikacije može predvidjeti put širenja.
- **Modeliranje**: **Simulacije** difuzije (npr. SI, SIR ili slični modeli) na stvarnom grafu omogućuju procjenu „utjecaja” čvora: ako bi taj čvor prvi bio „zarazio”, koliko bi drugih u konačnici bilo „zaraženo”? Centralnost (npr. eigenvector ili betweenness) često korelira s tim simulacijama i koristi se kao jednostavniji proxy.

---

Vidi primjer: [08_difuzija_utjecaj_primjer.ipynb](../code/08_difuzija_utjecaj_primjer.ipynb)
