import numpy as np

# define the healthy brain matrix for the first part of the section 4: where we compute G_k, the corrupted
# brain
# for the simpler model, only a 4x4 matrix representing the whole brain


G = np.array(
    [
        [1.0, 0.32, 0.36, 0.30],
        [0.32, 1.0, 0.82, 0.92],
        [0.36, 0.82, 1.0, 0.40],
        [0.30, 0.92, 0.40, 1.0],
    ]
)
