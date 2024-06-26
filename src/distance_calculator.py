"""
Tarjoaa toiminnallisuuden kahden kuvan välisen etäisyyden laskemiseksi
käyttäen määriteltyjä etäisyysmatriiseja ja liikkeiden listaa.
"""

class DistanceCalculator:
    """
    Luokka, joka laskee etäisyyden kahden kuvan välillä.
    """
    def __init__(self, distances, moves):

        """
        Alustaa DistanceCalculator-luokan.

        Args:
            distances: Matriisi etäisyyksistä.
            moves: Lista mahdollisista liikkeistä koordinaatistossa.
        """

        self.distances = distances
        self.moves = moves

    def distance_between_images(self, image_a_point_list, image_b_point_list, image_b_matrix):

        """
        Laskee etäisyyden kahden kuvan välillä.

        Args:
            image_a_point_list: Lista kuvan A pisteistä.
            image_b_point_list: Lista kuvan B pisteistä.
            image_b_matrix: Matriisi kuvan B pisteistä.

        Returns:
            Etäisyys kuvien välillä.
        """
        sum_distances = 0

        for point_a in image_a_point_list:
            x, y = point_a

            if image_b_matrix[x][y]:
                continue #siirrytään seuraavaan pisteeseen, koska täydellinen match löytyi

            match_found = False
            #jos matchia ei löytynyt, liikutaan ympäristössä ja etsitään lähintä pistettä
            for move in self.moves:
                new_x = x + move[0]
                new_y = y + move[1]

                if 0 <= new_x < 28 and 0 <= new_y < 28:
                    if image_b_matrix[new_x, new_y]:
                        #löydettiin läheltä piste, tallennetaan etäisyys valmiista matriisista
                        sum_distances += self.distances[4+move[0]][4+move[1]]
                        match_found = True
                        break
                        #lähellä oleva match löytyi, siirrytään seuraavaan pisteeseen

            if not match_found:
                min_distance = 1000000
                for point_b in image_b_point_list:
                    min_distance = min(min_distance, (point_a[0] - point_b[0]) *
                                       (point_a[0] - point_b[0]) + (point_a[1] - point_b[1]) *
                                       (point_a[1] - point_b[1]))

                sum_distances += min_distance

        return sum_distances
