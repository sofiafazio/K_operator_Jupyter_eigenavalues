import numpy as np
from libraries.mat_generation import generate_matrix

# here I generate a 4x4 matrix not symmetric with 1 on the diagonal
# this is the healthy matrix for the second part of the analysis of section 4: where we compute the K operator

# GforK = generate_matrix()
# print(GforK)
GforK = np.array(
    [
        [1.0, 0.64, 0.41, 0.58],
        [0.43, 1.0, 0.29, 0.67],
        [0.53, 0.61, 1.0, 0.77],
        [0.45, 0.54, 0.11, 1.0],
    ]
)
