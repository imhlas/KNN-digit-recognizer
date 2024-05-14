## MÄÄRITTELYDOKUMENTTI

**Tekijä:** Iida Lassila  
**Kurssi:** Algoritmit ja tekoäly (kesä 2024)  
**Opinto-ohjelma:** Tietojenkäsittelytieteen kandidaatti (TKT)  
**Käytettävä ohjelmointikieli:** Python  
**Vertaisarvioitavien projektien ohjelmointikieli:** Python  
**Dokumentaatiossa käytettävä kieli:** suomi  

### Harjoitustyön ydin

Harjoitustyön ydin on tunnistus/luokittelualgoritmi. Algoritmin tavoitteena on käsinkirjoitettujen numeroiden tunnistaminen käyttäen k:n lähimmän naapurin algoritmia ja modifioitua Hausdorffin etäisyyttä.

### Ratkaistava ongelma

Harjoitustyöni ratkaisee käsinkirjoitettujen numeroiden _tunnistusongelman_. Ohjelma tunnistaa ja ymmärtää sille syötteenä annetut kuvat, jotka ovat käsinkirjoitettuja numeroita (0-9).

Tähän päästäkseen ohjelmassa käytetään k:n lähimmän naapurin menetelmää, joka ratkaisee _luokitteluongelman_. Luokitteluongelmassa käsinkirjoitettu numero luokitellaan oikeaksi numeraaliseksi arvoksi (0-9) ja on siten osa tunnistusongelmaa.

### Käytettävät algoritmit ja tietorakenteet

Projektissani toteutan k:n lähimmän naapurin (k-NN) algoritmin käyttäen erilaisia etäisyysmittauksia. Kurssin ohjeistuksen perusteella aion kokeilla toteutuksessani muokatusta Hausdorffin etäisyydestä kertovan artikkelin mittaa D22 ja D23.

Tietorakenteista tulen käyttämään ainakin Pythonin NumPy -kirjaston vektoreita datan käsittelyyn ja laskentaan.

MNIST-tietokantaa tulee todennäköisesti käsittelemään Pythonin keras kirjastolla, jonka avulla voidaan ladata MNIST -tietokanta ja jakaa se opetus- ja testisetteihin.

Tulen myös hyödyntämään matplotlib -kirjastoa datan tutkimisessa ja visualisoinnissa.

### Mitä syötteitä ohjelma saa ja miten niitä käytetään

Ohjelma saa syötteinä MNIST-datasetin harmaasävykuvia, jotka muunnetaan mustavalkoisiksi kuviksi käsittelyn helpottamiseksi. Syötteitä käytetään opetusdatana k-NN-algoritmin opettamiseen ja testausdatana algoritmin suorituskyvyn arvioimiseen. Tunnistamattoman kuvan kohdalla ohjelma käyttää k-NN-algoritmia, jossa tunnistamaton kuva luokitellaan samaksi kuin k sitä lähimmät naapurit datasetissä perustuen valittuihin etäisyysmittauksiin.

### Aika- ja tilavaativuudet

Lähdeaineiston [2] perusteella KNN-algoritmin aikavaativuus yhdelle kyselypisteelle on O(nd), missä n on opetusdatan koko ja d on piirteiden määrä.

Tiedämme, että MNIST -tietokanta sisältää yhteensä 70 000 käsinkirjoitettua numeroa, josta 60 000 kpl kuuluu harjoitusdataan ja 10 000 kpl testidataan, joten n = 60 0000.

Lisäksi tiedetään, että MNIST -tietokanta sisältää kuvia, joissa jokainen kuva on 28x28 pikseliä eli d = 784.

Aikavaativuus O(nd) tarkoittaa, että jokaista kyselyä kohden KNN-algoritmin täytyy laskea etäisyys kyselypisteen ja jokaisen muun pisteen välillä datasetissä. Tämä kuulostaa siltä, että KNN suorittaminen voisi olla hidasta, mutta tässä vaiheessa projektia en oikeastaan osaa juurikaan asiaa arvioida.

### Viitteet

 [1] Dubuisson, M.-P., & Jain, A. K. (1994). A modified Hausdorff distance for object matching. _Proceedings of 12th International Conference on Pattern Recognition, 1,_ 566–568 vol.1. https://doi.org/10.1109/ICPR.1994.576361

[2] Laviale, Trevor (2023). Deep Dive on KNN: Understanding and Implementing the K-Nearest Neighbors Algorithm. https://arize.com/blog-course/knn-algorithm-k-nearest-neighbor/

