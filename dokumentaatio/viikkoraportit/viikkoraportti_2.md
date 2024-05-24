### Viikolla 2 tehyt asiat

- Alustava käyttöliittymä Tkinterillä
- MNISTLoader datan latausta sekä muokkausta varten
- distance_metrics -tiedosto eri etäisyysmittojen säilyttämiseen
- MNIST-datan ja etäisyysmittojen laskennan testailua

### Ohjelman edistyminen

Ohjelma on edistynyt käyttöliittymän, MNIST-datan latauksen ja etäisyysmittojen laskennan suhteen. Tämä vei aikaa paljon odotettua enemmän, joten testien sekä varsinaisen algoritmin toteutukseen ei ole vielä päästy.

Käyttöliittymä näyttää tällä hetkellä yhden etukäteen valitun numeron sekä sen etäisyydet ennalta valittuun joukkoon numeroita. Laskennassa käytetään etäisyysmittaa d6.

### Viikolla 2 opitut asiat

- Paljon kertausta vektoreiden käsittelystä ylipäätään, vektoreiden etäisyyksien laskemisesta, pisteiden etäisyyksien laskemisesta ym.
- Hausdorff-artikkelin teorian syventäminen
- MNIST-datan muokkaaminen ohjelman edellyttämään muotoon.

### Epäselväksi jääneet asiat / vaikeuksia tuottaneet asiat

- MNIST-datan lataaminen ohjelmaan. En päässyt käsiksi MNIST-dataan alkuperäisen urlin kautta, paketteja klikatessa sivustolle aukeaa vain Forbidden-ikkuna. Päädyin käyttämään sklearn -datasettiä, mikä saattaa olla jopa parempi vaihtoehto, sillä ymmärtääkseni siitä on ”putsattu” alkuperäisen sivuston ylimääräiset kentät.

- Etäisyysmittojen käyttäminen. Minulla oli/on haasteita ymmärtää, missä muodossa tuo MNIST-data olisi järkevintä välittää etäisyysmittojen laskentaan. Päädyin muokkaamaan alkuperäistä dataa pistejoukoiksi laskennan helpottamiseksi. Olen edelleen hieman epävarma, onko minulla tässä yhtään oikea suunta siinä, miten data muutetaan mustavalkoiseksi ja siitä edelleen pistejoukoksi.

Yritin etsiä valmiita funktioita tuon artikkelin mukaisen laskennan toteuttamiseen, mutta kirjoitin laskennan lopulta käsin jokaiselle pisteelle erikseen. Voisin veikata, että tämä tulee lisäämään laskennassa käytettävää aikaa.

### Seuraavaksi

- KNN algoritmi
- yksikkötestejä


