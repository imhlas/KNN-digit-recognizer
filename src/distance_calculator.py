import math 


class DistanceCalculator:
    def __init__(self, distances, moves):

        """
        Alustaa DistanceCalculator-luokan.

        Args:
            distances: Matriisi etäisyyksistä.
            moves: Lista mahdollisista liikkeistä koordinaatistossa.
        """

        self.distances = distances
        self.moves = moves

    def calculate_distance(self, point1, point2):
        """
        Laskee etäisyyden kahden pisteen välillä.

        Args:
            point1: Ensimmäisen pisteen koordinaatit (x, y).
            point2: Toisen pisteen koordinaatit (x, y).

        Returns:
            Etäisyys pisteiden välillä.
        """
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    
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

        for point_A in image_a_point_list:
            x, y = point_A

            if image_b_matrix[x][y] == 1:
                continue #siirrytään seuraavaan pisteeseen, koska täydellinen match löytyi

            match_found = False
            #jos täydellistä matchia ei löytynyt, liikutaan ympäristössä ja etsitään lähintä pistettä
            for move in self.moves:
                new_x = x + move[0]
                new_y = y + move[1]

                if 0 <= new_x < 28 and 0 <= new_y < 28:
                    if image_b_matrix[new_x][new_y] == 1:
                        #löydettiin läheltä piste, tallennetaan etäisyys valmiista matriisista
                        distance = self.distances[2+move[0]][2+move[1]]
                        sum_distances += distance
                        match_found = True
                        break
                        #lähellä oleva match löytyi, siirrytään seuraavaan pisteeseen

            if not match_found:
                min_distance = 1000000
                for point_B in image_b_point_list:
                    distance = self.calculate_distance(point_A, point_B)
                    if distance < min_distance:
                        min_distance = distance
                sum_distances += min_distance
        
        return sum_distances