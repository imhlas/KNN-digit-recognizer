import numpy as np

def d1(min_distances):
    return np.min(min_distances)

def d2(min_distances):
    return np.percentile(min_distances, 50)

def d3(min_distances):
    return np.percentile(min_distances, 75)

def d4(min_distances):
    return np.percentile(min_distances, 90)

def d5(min_distances):
    return np.max(min_distances)

def d6(min_distances, lengt_A):
    return np.sum(min_distances) / lengt_A

distance_functions = {
    'd1': d1,
    'd2': d2,
    'd3': d3,
    'd4': d4,
    'd5': d5,
    'd6': d6
}

def f1(d_ab, d_ba):
    return min(d_ab, d_ba)

def f2(d_ab, d_ba):
    return max(d_ab, d_ba)

def f3(d_ab, d_ba):
    return (d_ab + d_ba) / 2

def f4(d_ab, d_ba, n_a, n_b):
    return (n_a * d_ab + n_b * d_ba) / (n_a + n_b)

combination_functions = {
    'f1': f1,
    'f2': f2,
    'f3': f3,
    'f4': f4
}

def directed_hausdorff(A, B, distance_metric):
    min_distances = []

    for pointA in A:
        distances = []
        for pointB in B:
            distance = np.linalg.norm(np.array(pointA) - np.array(pointB))
            distances.append(distance)
        min_distances.append(min(distances))

    if distance_metric == 'd6':
        return distance_functions[distance_metric](min_distances, len(A))
    else:
        return distance_functions[distance_metric](min_distances)


def undirected_hausdorff(A, B, distance_metric, combination_metric):
    d_AB = directed_hausdorff(A, B, distance_metric)
    d_BA = directed_hausdorff(B, A, distance_metric)
    if combination_metric == 'f4':
        return combination_functions[combination_metric](d_AB, d_BA, len(A), len(B))
    else:
        return combination_functions[combination_metric](d_AB, d_BA)
