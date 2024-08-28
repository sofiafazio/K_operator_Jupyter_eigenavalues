import numpy as np

# define the healthy brain as a 4x4 matrix, symmetric and with 1 on the diagonal


G = np.array(
    [
        [1.0, 0.32, 0.36, 0.30],
        [0.32, 1.0, 0.82, 0.92],
        [0.36, 0.82, 1.0, 0.40],
        [0.30, 0.92, 0.40, 1.0],
    ]
)
