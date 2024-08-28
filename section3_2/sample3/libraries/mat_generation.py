import numpy as np


def generate_matrix():
    """
    this is the definition of 4x4 matrix, it is not symmetric because we are trying here different
    weights from i->j and j->i and we put 1 on the diagonal to consider the connections of every agglomerate with
    itself, also to maintain the analogy with the connectivity matrices
    """
    indices = np.random.rand(
        1, 12
    )  # 12 numbers because they do not have to repeat here, because I do not
    # want a symmetric matrix
    matrix = np.array(
        [
            [1.0, indices[0, 0], indices[0, 1], indices[0, 2]],
            [indices[0, 3], 1.0, indices[0, 4], indices[0, 5]],
            [indices[0, 6], indices[0, 7], 1.0, indices[0, 8]],
            [indices[0, 9], indices[0, 10], indices[0, 11], 1.0],
        ]
    )
    return matrix


# G = generate_matrix()

# print(G)
