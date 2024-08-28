import numpy as np

# here we define the four parts of the K operator, each one works on a different part of the healthy brain G
k_a = np.array(
    [
        [1.0, 0.5, 0.2, 0.7],
        [0.5, 1.0, 0.3, 0.4],
        [0.2, 0.3, 1.0, 0.9],
        [0.7, 0.4, 0.9, 1.0],
    ]
)

k_b = np.array(
    [
        [0.1, 0.1, 0.1, 0.1],
        [0.1, 0.1, 0.1, 0.1],
        [0.1, 0.1, 0.1, 0.1],
        [0.1, 0.1, 0.1, 0.1],
    ]
)

k_c = np.array(
    [
        [1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0],
    ]
)


k_d = np.array(
    [
        [1.0, 0.5, 0.2, 0.7],
        [0.5, 1.0, 0.3, 0.4],
        [0.2, 0.3, 1.0, 0.9],
        [0.7, 0.4, 0.9, 1.0],
    ]
)
# combine matrices into a 3D array 4x4x4
tensor = np.array([k_a, k_b, k_c, k_d])

# # print the tensor shape (4x4x4)
# print("Tensor shape:", tensor.shape)

# # Print the entire tensor
# print("\nTensor:")
# print(tensor)
