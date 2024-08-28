import numpy as np

# define the four parts of the healthy brain G, it is symmetric because we have to have the same weights
# from i->j and j->i and I we put 1 on the diagonal to consider the connections of every agglomerate with
# itself, also to maintain the analogy with the connectivity matrices


healthy_a = np.array(
    [
        [1.0, 0.57, 0.29, 0.17],
        [0.57, 1.0, 0.61, 0.67],
        [0.29, 0.61, 1.0, 0.27],
        [0.17, 0.67, 0.27, 1.0],
    ]
)
healthy_b = np.array(
    [
        [1.0, 0.12, 0.31, 0.96],
        [0.12, 1.0, 0.28, 0.96],
        [0.31, 0.28, 1.0, 0.99],
        [0.96, 0.96, 0.99, 1.0],
    ]
)

healthy_c = np.array(
    [
        [1.0, 0.85, 0.09, 0.78],
        [0.85, 1.0, 0.14, 0.58],
        [0.09, 0.14, 1.0, 0.35],
        [0.78, 0.58, 0.35, 1.0],
    ]
)

healthy_d = np.array(
    [
        [1.0, 0.60, 0.83, 0.86],
        [0.60, 1.0, 0.87, 0.32],
        [0.83, 0.87, 1.0, 0.15],
        [0.86, 0.32, 0.15, 1.0],
    ]
)
# combine matrices into a 3D array 4x4x4
healthy_matrices = np.array([healthy_a, healthy_b, healthy_c, healthy_d])
