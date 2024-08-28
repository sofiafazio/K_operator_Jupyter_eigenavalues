import numpy as np
from libraries.mat_generation import generate_matrix

# define the K operator for the first part of the section 4: where we compute the corrupted brain G_k
# for the simpler model, only a 4x4 matrix to represent the whole brain, thus a 4x4
# matrix for the K operator

# K1 = generate_matrix()

# print(K1)

K1 = np.array(
    [
        [1.0, 0.70, 0.20, 0.16],
        [0.70, 1.0, 0.70, 0.51],
        [0.20, 0.70, 1.0, 0.60],
        [0.16, 0.51, 0.60, 1.0],
    ]
)
