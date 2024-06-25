# Testausdokumentti
## Yksikkötestaus

- yksikkötestit toteutuettu seuraaville luokille:
  - DataLoader-luokka
  - KNN-luokka
  - DistanceCalculator-luokka
- käyttöliittymää ei testata, tämän sai jättää kurssin ohjeistuksen mukaisesti testien ulkopuolelle

- sovellus sisältää omat komennot sekä yksikkötestien ajamiselle, että testikattavuusraportin tuottamiselle

## Testikattavuusraportti

![coverage](kuvat/coverage_report.png)

## Suorituskykytestaus

Suorituskyvyn testaamista toteutettiin projektissa ohjelman ulkopuolisella yksinkertaisella funktiolla, joka käytännössä ajoi KNN-luokan oliota erilaisilla parametreilla. Testauksessa tarkasteltiin seuraavia asioita:

-	miten k-arvon valinta vaikuttaa tunnistuksen oikeellisuuteen
-	miten testidatan koko vaikuttaa laskenta-aikaan
  
### k-arvon valinta

Suorituskykytestien perusteella optimaalinen k-arvo on 4 tai 5. Näillä arvoilla saavutettiin testeissä vähiten vääriä tunnistuksia, kun suodattimen arvona käytettiin lukua 127.

### testidatan koko

Koska ohjelman käyttämä laskenta-aika on melko suuri jo pienillä data-joukoilla, tässä testaamisessa käytettiin hyvin pieniä parametreja testidatalle. Testien perusteella nähtiin kuitenkin, että ohjelman käyttämä laskenta-aika kasvoi melko lineaarisesti suhteessa testidatan kokoon. 
