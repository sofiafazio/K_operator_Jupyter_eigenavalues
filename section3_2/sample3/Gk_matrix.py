import numpy as np
from libraries.mat_generation import generate_matrix

# here I generate a 4x4 matrix not symmetric with 1 on the diagonal
# this is the already diseased matrix for the second part of the analysis of section 4: where we compute
# the K operator

# Gk = generate_matrix()

# print(Gk)


Gk = np.array(
    [
        [1.0, 0.86, 0.24, 0.62],
        [0.60, 1.0, 0.64, 0.96],
        [0.90, 0.31, 1.0, 0.88],
        [0.92, 0.05, 0.20, 1.0],
    ]
)
