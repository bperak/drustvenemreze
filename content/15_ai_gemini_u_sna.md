# 15. Generativni AI (Google Gemini) u mrežnoj analizi i interpretaciji

Veliki jezični modeli (LLM) i **multimodalni** modeli poput **Google Geminija** sve se češće koriste u istraživačkom radu: za **pomoć u kodiranju**, **sažimanje literature**, **generiranje hipoteza**, **pisanje skica interpretacije** mrežnih mjera ili za **oblikovanje pitanja** za kvalitativno čitanje sadržaja. Ovo poglavlje ne predstavlja zamjenu za statistiku ili teoriju grafova — model **ne “vidi”** vašu mrežu osim ako mu eksplicitno ne pošaljete opis — nego uvodi **odgovornu** uporabu AI alata kao **pomoćnika** u radu koji već temelji na SNA-u, u skladu s etikom i s poglavljima o ograničenjima (pogl. 13) i online podacima (pogl. 10).

---

## Teorijski koncept

**Generativni AI** u kontekstu SNA može:

- **Ubrzati pripremu** — npr. predložiti Python kod za NetworkX uz jasno zadane bridove i tip grafa (uvijek **provjeriti** i testirati izlaz).
- **Strukturirati tekst** — npr. pretvoriti tablicu mjera u **nacrt** odjeljka rezultata (uz ljudsku reviziju i citiranje izvora).
- **Podržati hermeneutiku** — npr. na temelju **anonimiziranog** ili **mock** opisa mreže predložiti **moguća** kulturološka čitanja (ne “istine”).
- **Pomoći u učenju** — objasniti pojmove (centralnost, modularnost) drugim jezikom ili primjerima.

Model **nije** pouzdan izvor činjenica o literaturi, zakonima ili API-ima platformi: može **halucinirati** citate i zastarjele podatke. **Ne smije** se tretirati kao etičko povjerenstvo ili kao zamjena za institucionalnu suglasnost ispitanika. Za **osobne podatke** s društvenih mreža (sadržaji tweetova, identifikatori) slanje u javni API treba biti **svjesna odluka** unutar GDPR-a, etike i pravila vaše ustanove — često je bolje slati samo **agregate**, **mock** ili **anonimizirane** sažetke.

---

## Google Gemini i Google AI Studio

**Gemini** je obitelj modela koju nudi Google; **Google AI Studio** ([aistudio.google.com](https://aistudio.google.com/)) je web sučelje za isprobavanje modela i **izdavanje API ključa** za razvojne aplikacije. Besplatna razina tipično omogućuje ograničen broj zahtjeva (kvote se mijenjaju; provjerite službenu dokumentaciju). Za kolegij je dovoljno **besplatnog ključa** za vježbu i male eksperimente.

### Kako dobiti besplatan API ključ (Google AI Studio)

1. Otvorite u pregledniku **[Google AI Studio](https://aistudio.google.com/)** (ponekad se u adresi pojavi i `makersuite.google.com`, preusmjerava na isto sučelje).
2. **Prijavite se** Google računom (npr. studentski `@student.*` ili osobni Gmail).
3. U sučelju potražite **Get API key** / **Create API key** (izbornik s lijeve strane ili gumb na početnoj strani).
4. Odaberite **Create API key in a new project** ili povežite ključ s postojećim Google Cloud projektom (za učenje dovoljan je novi projekt).
5. Kopirajte prikazani **API key** i spremite ga u **`.env`** u korijenu ovog repozitorija (datoteka se **ne** commita u git):

   ```env
   GEMINI_API_KEY=paste_your_key_here
   ```

   (Neke upute koriste i naziv `GOOGLE_API_KEY` — važno je da u kodu učitate **istu** varijablu koju ste postavili; u bilježnici poglavlja 15 koristimo `GEMINI_API_KEY`.)

6. U Pythonu učitajte varijable iz `.env` pomoću paketa **`python-dotenv`** (vidi bilježnicu) ili postavite istu varijablu u sustavu okruženja prije pokretanja Jupytera.

7. **Sigurnost:** ključ je tajna — ne dijelite ga u chatu, ne umetajte u javni kod. Ako ključ procuri, u Google AI Studio / Cloud konzoli **rotirajte** (opozovite stari i izdajte novi).

Za ažurirane limite i uvjete pogledajte službenu stranicu [Google AI for Developers](https://ai.google.dev/) (cjenik, dokumentacija, politika korištenja).

---

## Definicije

- **API ključ**: Tajni niz znakova koji aplikaciji dopušta pozive prema Googleovom API-ju u vaše ime; vezan je uz projekt i kvote.
- **Prompt**: Tekstualna (ili multimodalna) uputa modelu; kvaliteta i **ograničenja** (npr. „odgovaraj samo na hrvatskom”, „ne tvrdi kauzalnost”) snažno oblikuju izlaz.
- **Halucinacija**: Kada model izgleda uvjerljivo tvrdi nešto **netočno** ili nepotkrijepljeno; zato se citati i brojke **provjeravaju** u izvorima.

---

## Što AI *ne* zamjenjuje

- **Odluku o bridu i granicama mreže** — to ostaje metodološki korak istraživača (pogl. 1–6, 13).
- **Etičku i pravnu procjenu** — posebno za podatke s platformi (pogl. 10, 13, 14).
- **Replikaciju** — kolega mora moći ponoviti analizu iz **transparentnog** koda i podataka, ne iz “razgovora s modelom”.

---

## Alati

- **Python**: paket **`google-generativeai`** za poziv Geminija iz koda; **`python-dotenv`** za učitavanje `GEMINI_API_KEY` iz `.env`.
- **Google AI Studio**: brzo testiranje promptova bez pisanja koda.

---

## Ovo poglavlje kao prijelaz: stari i novi način razmišljanja o cijelom svezku

**Stari način** (još uvijek važeći jezgra) znači: formalizirate mrežu, računate mjere u softveru, interpretirate uz literaturu i etiku — sve transparentno u kodu i metodologiji. **Novi način** dodaje **asistiranu** komponentu: isti koraci, ali uz LLM koji ubrzava pisanje, kodiranje i „mozganje” uz **obveznu** ljudsku provjeru, posebno za citate, kauzalnost i zaštitu podataka.

Kako se AI uklapa u ostala poglavja (kratka karta):

| Poglavlje | Uloga AI-a (uz provjeru) |
|-----------|---------------------------|
| [1](01_uvod_drustvene_mreze_teorija_grafova.md), [5](05_mreze_usmjerene_tezine.md) | tutor za pojmove grafa i NetworkX sintaksu |
| [2](02_prikupljanje_obrada_podataka.md) | ekstrakcija entiteta, čišćenje tablica |
| [3](03_mjere_mrezne_strukture.md), [6](06_analiza_zajednica.md) | objašnjenje mjera i algoritama, nacrt interpretacije particije |
| [4](04_socijalni_kapital.md) | kategorije veza, verbalni most prema bonding/bridging |
| [7](07_vizualizacija_mreza.md) | kod i stilovi prikaza, pristupačnost |
| [8](08_difuzija_inovacija_utjecaj.md), [9](09_dinamika_mreza_vrijeme.md) | hipoteze, narativ trendova, **ne** zamjena za dokaz |
| [10](10_online_drustvene_mreze.md), [14](14_analiza_twittera_alati.md) | tehnička pomoć i interpretacija **agregata/mock** |
| [11](11_sna_marketing.md), [12](12_drustvene_mreze_politika.md) | nacrti izvještaja uz rizik metrike i sigurnosti |
| [13](13_kriticko_razmisljanje_ogranicenja.md) | okvir za **ograničenja** samog AI-a u istraživanju |

Svako od tih poglavlja sada ima i odlomak **„AI u ovom poglavlju”** koji tumači taj prijelaz u njegovom kontekstu.

---

Vidi primjer: [15_ai_gemini_primjer.ipynb](../code/15_ai_gemini_primjer.ipynb)

**Poveznice:** [Online društvene mreže (10)](10_online_drustvene_mreze.md) · [Kritičko razmišljanje (13)](13_kriticko_razmisljanje_ogranicenja.md) · [Twitter/X (14)](14_analiza_twittera_alati.md)
