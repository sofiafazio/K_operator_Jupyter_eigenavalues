import numpy as np


def generate_matrix():
    """
    this is the definition of 4x4 matrix, it is symmetric because we are trying here to have to have the same
    weights from i->j and j->i and we put 1 on the diagonal to consider the connections of every agglomerate with
    itself, also to maintain the analogy with the connectivity matrices
    """
    indices = np.random.rand(1, 6)
    matrix = np.array(
        [
            [1.0, indices[0, 0], indices[0, 1], indices[0, 2]],
            [indices[0, 0], 1.0, indices[0, 3], indices[0, 4]],
            [indices[0, 1], indices[0, 3], 1.0, indices[0, 5]],
            [indices[0, 2], indices[0, 4], indices[0, 5], 1.0],
        ]
    )
    return matrix


# generate four such matrices --> undirected, so with the same weights for i->j and j->i


G = generate_matrix()

print(G)
