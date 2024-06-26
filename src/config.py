"""
Konfiguraatiotiedosto, joka sisältää valmiiksi lasketut etäisyydet ja liikkeet kooridinaatistossa.
"""

# Etäisyysmatriisi
distances = [ [32, 25, 20, 17, 16, 17, 20, 25, 32],
              [25, 18, 13, 10, 9, 10, 13, 18, 25],
              [20, 13, 8, 5, 4, 5, 8, 13, 20],
              [17, 10, 5, 2, 1, 2, 5, 10, 17],
              [16, 9, 4, 1, 0, 1, 4, 9, 16],
              [17, 10, 5, 2, 1, 2, 5, 10, 17],
              [20, 13, 8, 5, 4, 5, 8, 13, 20],
              [25, 18, 13, 10, 9, 10, 13, 18, 25],
              [32, 25, 20, 17, 16, 17, 20, 25, 32]]

# Liikkeet koordinaatistossa
moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1), (0, 2),
       (0, -2), (2, 0), (-2, 0), (-1, 2), (2, 1), (-1, -2), (1, -2), (-2, 1), (-2, -1),
       (1, 2), (2, -1), (-2, -2), (-2, 2), (2, -2), (2, 2),
       (0, 3), (0, -3),(3, 0), (-3, 0), (1, 3), (-3, -1),
       (1, -3), (3, 1), (-1, 3), (-1, -3),
       (-3, 1), (3, -1), (-3, 2), (3, 2), (2, -3), (-2, -3),
       (3, -2), (-3, -2),(2, 3), (-2, 3), (-3, -3), (-3, 3),
       (3, -3), (3, 3),(0, 4), (0, -4), (4, 0), (-4, 0),(1, 4),
       (1, -4), (-1, 4), (-1, -4),(4, 1), (4, -1), (-4, 1), (-4, -1),
       (2, 4), (2, -4), (-2, 4), (-2, -4),(4, 2), (4, -2), (-4, 2), (-4, -2),
       (3, 4), (3, -4), (-3, 4), (-3, -4),(4, 3), (4, -3), (-4, 3),
       (-4, -3),(4, 4), (4, -4), (-4, 4), (-4, -4)]
