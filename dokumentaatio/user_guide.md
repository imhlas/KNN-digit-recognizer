### Asennus

- kloonaa repositorio
- asenna riippuvuudet

  ```poetry install```

- aktivoi virtuaaliympäristö

  ```poetry shell```

### Komentorivityökalut

- ohjelman käynnistäminen
  
  ```poetry run invoke start```

- yksikkötestien ajaminen (ilman testikattavuusraporttia)

  ```poetry run invoke test```

- yksikkötestien ja testikattavuusraportin ajaminen

  ```poetry run invoke coverage-report```

### Käyttöliittymä

Ohjelma käynnistyy aloitusnäkymään, josta käyttäjä voi valita, montako harjoituskuvaa ohjelmassa käytetään mallin kouluttamiseen:

![start_view1](kuvat/start_view1.png)

Harjoitusdatan valinnan jälkeen ohjelma lataa käytettävän datan ja esikäsittelee sen. Datan lataaminen kestää useita kymmeniä sekunteja, käyttäjä saa näkymään ilmoitusviestin. Kun ohjelmassa käytettävä data on ladattu, pääsee käyttäjä määrittämään testidatan määrän sekä k-arvon:

![start_view2](kuvat/start_view2.png)


**Ohjelma toimii tällä hetkellä hyvin hitaasti suurilla syötteillä, joten ohjelmaa kannattaa ajaa melko pienillä syötteillä**

Tulokset aukeavat uuteen näkymään:

![results_view](kuvat/result_view.png)

Tulosnäkymästä käyttäjä voi tarkastella, montako käsinkirjoitettua numeroa pystyttiin ennustamaan oikein ja montako ennustettiin väärin. Lisäksi näkymässä näytetään laskentaan käytetty aika.

Taulukosta käyttäjä pystyy tarkastelemaan yksityiskohtaisemmin, mitkä satunnaisesti valitut käsinkirjoitetut numerot valikoituvat testaukseen ja minkä ennusteen algoritmi niille antoi. Taulukko näyttää myös kaikki naapuriarvot, joita laskennassa saatiin.
