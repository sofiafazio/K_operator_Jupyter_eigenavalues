import numpy as np

# define the healthy brain as a 4x4 matrix 4x4 matrix, it is not symmetric because we are trying here different
# weights from i->j and j->i and we put 1 on the diagonal to consider the connections of every agglomerate with
# itself, also to maintain the analogy with the connectivity matrices


G = np.array(
    [
        [1.0, 0.34, 0.62, 0.58],
        [0.69, 1.0, 0.42, 0.12],
        [0.71, 0.38, 1.0, 0.47],
        [0.13, 0.31, 0.63, 1.0],
    ]
)
