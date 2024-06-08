### Viikolla  tehdyt asiat

- Lisätty testeja luokille KNN sekä luokalle DistanceCalculator
- Optimoitu etäisyyslaskentaa ja pyritty nopeuttamaan laskentaan käytettävää aikaa seuraavilla asioilla
    - Etäisyyksien tallentaminen kekoon listan sijaan. Oletin tämän vähentävän laskenta-aikaa paljonkin, mutta lopulta ei ollut suurin vaikuttava tekijä
    - Neliöjuuren poistaminen laskennasta. KNN kannalta neliöjuuren ottamisella ei ole merkitystä, joten jätin sen kokonaan pois sekä valmiista etäisyysmatriisista että muiden etäisyyksien laskennasta. Tämä ei kuitenkaan juurikaan vaikuttanut laskenta-aikaan.
    - Harjoituskuvien muuttaminen (0,1) matriiseista (False, True) matriiseiksi. Tämä auttoi nopeuttamaan laskentaan käytettyä aikaa huomattavasti, 1/10k datalla laskenta-aika nopeutui noin 20 sec.
    - Valmiin etäisyysmatriisin kasvattaminen 5x5 matriisista 7x7 matriisiksi. Tällä saavutettiin myös merkittävää kehitystä laskennan optimoimisessa, 1/10k datalla laskenta nopeutui noin 10 sec.

- Käyttöliittymän kehittäminen

### Ohjelman edistyminen

- Ohjelma edistyi mielestäni hyvin. Vaikka ohjelman käyttämä aika etäisyyslaskennassa on edelleen melko hidasta, onnistuin mielestäni kuitenkin parantamaan laskenta-aikaa tekemilläni muutoksilla merkittävästi.

### Viikolla 3 opitut asiat

- Testaukseen liittyvien asioiden palauttelu mieleen
- Laskennan optimointiin liittyvät kehitysmahdollisuudet

### Epäselväksi jääneet asiat / vaikeuksia tuottaneet asiat
-
### Seuraavaksi

- Laskenta-aikaa olisi hyvä edelleen pyrkiä nopeuttamaan. Ohjelmani käyttää tällä hetkellä valmista etäisyysmatriisia koossa 7x7, tarkoitus olisi kokeilla kasvattaa etäisyysmatriisin kokoa tätäkin suuremmaksi ja katsoa miten vaikuttaa laskenta-aikaan.
- Testejä olisi hyvä tehdä lisää, näistä jäänyt hieman velkaa edellisiltä viikoilta.
