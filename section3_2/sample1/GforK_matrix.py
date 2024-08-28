import numpy as np
from libraries.mat_generation import generate_matrix

# define the healthy brain for the second part of section 4: where we compute the K operator starting from an
# healthy brain and a corrupted brain
# for the simpler model we have only a 4x4 matrix representing the whole brain

# GforK = generate_matrix()
# print(GforK)
GforK = np.array(
    [
        [1.0, 0.90, 0.31, 0.62],
        [0.90, 1.0, 0.38, 0.04],
        [0.31, 0.38, 1.0, 0.98],
        [0.62, 0.04, 0.98, 1.0],
    ]
)
