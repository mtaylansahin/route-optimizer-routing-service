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