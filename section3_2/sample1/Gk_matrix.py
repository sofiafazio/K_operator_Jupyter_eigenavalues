import numpy as np
from libraries.mat_generation import generate_matrix

# define the corrupted brain for the second part of section 4: where we compute the K operator starting from
# an healthy brain and a corrupted brain
# for the simpler model, only a 4x4 matrix for the healthy brain, anothe 4x4
# matrix for the K operator and for the unhealthy brain as well.

# Gk = generate_matrix()

# print(Gk)


Gk = np.array(
    [
        [1.0, 0.13, 0.42, 0.7],
        [0.13, 1.0, 0.94, 0.09],
        [0.42, 0.94, 1.0, 0.73],
        [0.77, 0.09, 0.73, 1.0],
    ]
)
