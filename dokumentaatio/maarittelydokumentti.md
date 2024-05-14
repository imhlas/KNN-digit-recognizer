# MÄÄRITTELYDOKUMENTTI

**Tekijä:** Iida Lassila  
**Kurssi:** Algoritmit ja tekoäly (kesä 2024)  
**Opinto-ohjelma:** Tietojenkäsittelytieteen kandidaatti (TKT)  
**Käytettävä ohjelmointikieli:** Python
**Vertaisarvioitavien projektien ohjelmointikieli:** Python
**Dokumentaatiossa käytettävä kieli:** suomi

## Harjoitustyön ydin

Käsinkirjoitettujen numeroiden tunnistaminen käyttäen k:n lähimmän naapurin algoritmia ja modifioitua Hausdorffin etäisyyttä

## Ratkaistava ongelma

Harjoitustyöni ratkaisee käsinkirjoitettujen numeroiden tunnistusongelman. Ohjelma tunnistaa ja ymmärtää sille syötteenä annetut kuvat, jotka ovat käsinkirjoitettuja numeroita (0-9).

Tähän päästäkseen ohjelmassa käytetään k:n lähimmän naapurin menetelmää, joka ratkaisee luokitteluongelman. Luokitteluongelmassa käsinkirjoitettu numero luokitellaan oikeaksi numeraaliseksi arvoksi (0-9) ja on siten osa tunnistusongelmaa.

## Käytettävät algoritmit ja tietorakenteet

Projektissani toteutan k:n lähimmän naapurin (k-NN) algoritmin käyttäen erilaisia etäisyysmittauksia. Kurssin ohjeistuksen perusteella aion kokeilla toteutuksessani muokatusta Hausdorffin etäisyydestä kertovan artikkelin mittaa D22 ja D23.

Tietorakenteista tulen käyttämään ainakin Pythonin NumPy -kirjaston vektoreita datan käsittelyyn ja laskentaan.

MNIST-tietokantaa tulee todennäköisesti käsittelemään Pythonin keras kirjastolla, jonka avulla voidaan ladata MNIST -tietokanta ja jakaa se opetus- ja testisetteihin.

Tulen myös hyödyntämään matplotlib -kirjastoa datan tutkimisessa ja visualisoinnissa.

## Mitä syötteitä ohjelma saa ja miten niitä käytetään

Ohjelma saa syötteinä MNIST-datasetin harmaasävykuvia, jotka muunnetaan mustavalkoisiksi kuviksi käsittelyn helpottamiseksi. Syötteitä käytetään opetusdatana k-NN-algoritmin opettamiseen ja testausdatana algoritmin suorituskyvyn arvioimiseen. Tunnistamattoman kuvan kohdalla ohjelma käyttää k-NN-algoritmia, jossa tunnistamaton kuva luokitellaan samaksi kuin k sitä lähimmät naapurit datasetissä perustuen valittuihin etäisyysmittauksiin.
