### Viikolla 6 tehdyt asiat
- etäisyyslaskennassa potenssi vaihdettu kertolaskuun
- siirretty datan esikäsittelyyn liittyvät toiminnot datan latauksen yhteyteen, jotta esikäsittelyyn ei mene turhaa aikaa itse etäisyyslaskennassa
- poistettu turhia luuppeja koodista (turhat if-ehdot, turhat enumarate & zip -funktiot)
- ResultsView -näkymän muokkaus siten, että käyttäjälle näytetään oikean arvon ja ennustearvon lisäksi myös kaikki k-naapurit listana
- StartView -näkymässä käyttäjä voi valita harjoitusdatan määrän kolmesta eri vaihtoehdosta (10k, 30k, 60k)

### Ohjelman edistyminen

Sain ohjaajalta hyviä vinkkejä etäisyyslaskennan optimointiin, näiden vinkkien sekä muutaman oman tietorakennemuutoksen ansiosta sain tiputettua etäisyyslaskentaan käytettävästä ajasta yli puolet pois aikaisempaan verrattuna.

Oikeastaan kaikki muutokset, joita kokeilin, lyhensivät selvästi laskenta-aikaa aikaisempaan verrattuna. Eniten vaikutusta oli kuitenkin selvästi sillä, että matriisit käsitellään jo datan lataamisen vaiheessa, eikä tähän työhön käytetä varsinaista laskenta-aikaa.

Tällä hetkellä laskennan kesto parametreilla 1/60 000 vie aikaa n. 45 sekuntia. Vaikka laskenta on edelleen suhteellisen hidas, olen todella tyytyväinen edistymiseen, sillä vielä ennen tämän viikon muutoksia oltiin samalla parametrimäärällä yli 100 sekunnissa.

### Viikolla 6 opitut asiat

Syvempi ymmärrys siitä, miten tietyt tietorakenteet, erilaiset looppaukset koodissa sekä näiden asioiden muokkaaminen vaikuttavat ohjelmakoodin ajamiseen menevään aikaan.

### Epäselväksi jääneet asiat / vaikeuksia tuottaneet asiat

### Seuraavaksi
- suorituskykytestit
- dokumentaatio
- koodin laadun parantaminen
- loppudemoon valmistautuminen
