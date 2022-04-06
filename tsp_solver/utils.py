from math import sqrt
from random import randrange

 # Initialize given number of nodes and random distance edges between them
def initialize_problem_space(N):
    edges = []
    for i in range(N):
        dists = []
        for j in range(i + 1):
            if i == j:
                dists.append(0)
            else:
                dists.append(randrange(19) + 1)
        edges.append(dists)
    return edges


def path_cost(distance_matrix, path):
    """Caclulate total length of the given path, using the provided distance matrix.
    
    Parameters
    ----------
    distance_matrix : NxN 2d array (numpy or list of lists)
        Matrix of distance between nodes, only left triangle part is used.
    path : sequence of integers
        Path in the graph of nodes. Values are node indices, 0 .. N-1
    Returns
    -------
    Length of the path. If path is empty or contains only 1 node, returns integer 0.
    """

    ipath = iter(path)
    try:
        j = next(ipath)
    except StopIteration:
        #empty path
        return 0
    
    dist = 0    
    for i in ipath:
        if i >= j:
            dist += distance_matrix[i][j]
        else:
            dist += distance_matrix[j][i]
        j = i
    return dist

def calculate_distance(c1, c2):
    """
    Calculate euclidian distance between 2 coordinates
    c1: coordinate tuple in the form (x, y)
    c2: coordinate tuple in the form (x, y)
    returns: float distance, euclidian distance between c1 and c2 up to 5 decimal points
    """
    x_diff = (c1[0] - c2[0]) ** 2
    y_diff = (c1[1] - c2[1]) ** 2
    dist = sqrt(x_diff + y_diff)

    return round(dist, 5)

def create_distance_matrix(coords):
    dists = []
    prev_coords = []
    for i, coord in enumerate(coords):
        x, y = coord["x"], coord["y"]
        temp_dist = []
        for c in prev_coords:
            temp_dist.append(calculate_distance(c, (x, y)))
        temp_dist.append(0.0)
        dists.append(temp_dist)

        prev_coords.append((x, y))
    return dists