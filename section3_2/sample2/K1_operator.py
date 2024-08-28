import numpy as np


# here we generate K operator as a matrix that is not symmetric and does not have 1 on the diagonal
# for the first part of the analysis of section 4

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
        [0.07, 0.20, 0.38, 0.27],
        [0.10, 0.19, 0.35, 0.90],
        [0.92, 0.68, 0.78, 0.18],
        [0.98, 0.83, 0.09, 0.59],
    ]
)
