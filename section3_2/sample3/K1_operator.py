import numpy as np


# here I want to generate a matrix that is not symmetric and does not have 1 on the diagonal

# def generate_matrix():
#     """
#     this is the definition of 4x4 matrix, it is symmetric because we are trying here to have to have the same
#     weights from i->j and j->i and we put 1 on the diagonal to consider the connections of every agglomerate with
#     itself, also to maintain the analogy with the connectivity matrices
#     """
#     matrix = np.array(np.random.rand(4, 4))
#     return matrix


# mat = generate_matrix()
# print(mat)

K1 = np.array(
    [
        [0.60, 0.40, 0.04, 0.54],
        [0.04, 0.49, 0.96, 0.56],
        [0.60, 0.88, 0.16, 0.41],
        [0.06, 0.00, 0.32, 0.38],
    ]
)
