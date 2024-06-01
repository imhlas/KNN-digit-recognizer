### Viikolla 3 tehdyt asiat

- Uudet luokat KNN ja DistanceCalculator
  
  -  DistanceCalculator hoitaa ohjelmassa varsinaista laskentaa, KNN luokka määrittää mitä lasketaan. Tällä hetkellä KNN laskee etäisyyden summana distance_AB + distance_BA.

  -  Etäisyydet ja niitä vastaavat numerot tallentuvat tällä hetkellä listaan, josta KNN luokka hakee naapurit järjestämällä listan etäisyyksien mukaan.

- Matriisi sisältäen valmiiksi laskettuja etäisyyksiä & lista mahdollisista liikkeistä koordinaatistossa.
 
- Koodin dokumentointi

### Ohjelman edistyminen

- Ohjelma edistyi tällä viikolla mielestäni hyvin. Sain ohjaajalta hyviä vinkkejä etäisyyslaskentaan ja otinkin valmiin etäisyysmatriisin käytön ja koordinaatiston liikkeitä kuvaavan pistelistan mukaan ohjelmaani.

- Sain myös toteutettua alustavan KNN-algotimin, jossa k määräytyy tällä hetkellä käyttäjän valinnan mukaan käyttöliittymässä. Tämä valittu määrä k-naapureita näytetään laskennan jälkeen käyttöliittymässä.

### Viikolla 3 opitut asiat

- Erilaiset toteutustavat etäisyyslaskennassa

- KNN algoritmi

### Epäselväksi jääneet asiat / vaikeuksia tuottaneet asiat
-
### Seuraavaksi

- Ohjelma ei sisällä vielä yhtäkään testiä, tätä on tarkoitus edistää ensi viikolla

- Laskennassani on vielä asioita, joiden tiedän hidastavan laskentaa. Esimerkiksi etäisyydet tallennetaan listaan, joka sortataan k-naapureiden löytämiseksi ja tiedän tämän vievän ylimääräistä aikaa. Tähän olisi tarkoitus ensi viikolla kokeilla kekoa ja sen vaikutusta laskenta-aikaan. Lisäksi tavoite pyrkiä löytämään muita keinoja laskennan optimoimiseen.



