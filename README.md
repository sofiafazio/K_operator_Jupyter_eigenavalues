# K_operator_Jupyter_eigenavalues

## Folder section3_1:
- for the healthy brain, namely G_matrices: 4 random symmetric matrices with 1 on diagonal in order to have undirected graphs, thus same weights from j-->i and i-->j. 
- for the K operator, k_operator: operator composed of four parts, each one working on one part of the healthy brain. 

The graphs saved in tha main: 
- healthy_i: graphs showing the healthy brain;
- i_k_elwise: they are matrices obtained post element-wise multiplication between the K operator and the matrices of the healthy brain (the name was given in the sense of application of an operator, e.g. A^{k}, thus the first part of the operator K applied the the matrix A, that is the first part of the healthy brain G);
- i_k_matmul: matrices obtained post matrix row by column multiplication between the K operator and the healthy brain (same consideration on the name ass above).

Text files: 
- healthy_i: matrices of the healthy brain;
- k_i: the four different parts of the K operator;
- eigenvalues and eigenvectors of the product matrices.

## Folder section3_2 sample1:

In this folder we uploaded graphs and data relative to the section 4 of the article.
We have two parts of the analysis.

#### first part: computing the diseased brain from and healthy brain and the K operator 
Firstly we defined a symmetric 4x4 G matrix for the healthy initial brain and a symmetric K operator, with 1 on the diagonal in order to consider the connections of every agglomerate with itself and to keep the analogy with the connectivity matrices. The numbers out of the diagonal are randomly selected. 

In the graphs: 
- healthy_G = graph of the healthy initial brain in of the first analysis 
- elementw_KG = K * G element wise application of the K operator on the healthy brain, in order to obtain the corrupted brain 
- rowbycol_KG = K @ G matrix multiplication application of the K operator on the healthy brain in order to obtain the corrupted brain 

In the text files:
- G: matrix representing the healthy initial brain;
- K1: matrix representing the K operator for the computation of the corrupted brain, applying K1 to the healthy brain; 
- K1G: matrix representing the diseased brain after the application of K1 on G, using the element-wise multiplication;
- K1_at_G: matrix representing the diseased brain after the application of K1 on G, using the row by column multiplication; 
- eigenvalues_and_eigenvectors.txt sums up the eigenvalues and eigenvectors of the two different product matrices K1G and K1_at_G.

#### second part: computing K operator from an healthy brain and an already diseased brain 
Secondly we supposed to have the healthy brain G and the diseased brain Gk, matrices are defined with the same method as above, they are symmetric and with 1 on the diagonal in order to consider the connections of every agglomerate with itself and to keep the analogy with the connectivity matrices. The numbers out of the diagonal are randomly selected. 

In the graphs: 
- healthy_G_forK: graph of the healthy initial brain in of the second analysis, in order to compute the K operator 
- inverse_G_forK: graph of the inverse of the G matrix, thus G^{-1}

In the text files: 
- GforK: matrix of the healthy brain, the one used to compute the K operator;
- Gk: matrix of the already diseased brain, used to compute the K operator;
- G_1: inverse matrix of G, the name was given to recall the operation of inversion, G^{-1};
- K_elementw: K operator computed from the application of the element-wise multiplication between Gk and G^{-1};
- K_matmul: K operator obtained from the application of the matrix multiplication row by column between Gk and G^{-1}.
- K_matrices_eigenval_eigenvec.txt: sums up the eigenvalues and eigenvectors of the two different K operator obtaind with the two different matrix multiplication methods.

## Folder section3_2 sample2: 
In this folder we uploaded a second try for the graphs and data relative to the section 4 of the article.
We modified only the fisrt part of the analysis, where we define the K operator and we defined it not symmetric and without 1 on the diagonal. 

#### first part: computing the diseased brain from an healthy brain and a the K operator
We defined a symmetric 4x4 G matrix for the healthy initial brain with 1 on the diagonal in order to consider the connections of every agglomerate with itself and to keep the analogy with the connectivity matrices, the numbers out of the diagonal are randomly selected. 
Then, we defined a K operator that is NOT symmetric and has not 1 on the diagonal, so we expect that it will change also the connections of the agglomerates with themselves.   

In the graphs: 
- healthy_G: matrix of the healthy initial brain in of the first analysis;
- elementw_KG: K * G element wise application of the K operator on the healthy brain;
- rowbycol_KG: K @ G matrix multiplication application of the K operator on the healthy brain.
Here the K operator used is the one named K1.

In the text files:
- G: matrix representing the healthy initial brain, this is symmetric and with 1 on the diagonal; 
- K1: matrix representing the K operator for the computation of the corrupted brain, applying K1 to the healthy brain, this is not symmetric and has not 1 on the diagonal;
- K1G: matrix representing the diseased brain after the application of K1 on G, using the element-wise multiplication;
- K1_at_G: matrix representing the diseased brain after the application of K1 on G, using the row by column multiplication; 
- eigenvalues_and_eigenvectors.txt sums up the eigenvalues and eigenvectors of the two different product matrices K1G and K1_at_G.

## Folder section3_2 sample3:

In this folder we uploaded a third try for the graphs and data relative to the section 4 of the article.
We have two parts of the analysis. 

In this folder we uploaded graphs and data relative to the section 4 of the article.
We have two parts of the analysis.

#### first part: computing the diseased brain from and healthy brain and the K operator 
Firstly we defined a 4x4 G matrix for the healthy initial brain and a K operator, both not symmetric in order to try here different weights from i->j and j->i. But the G matric has 1 on the diagonal to consider the connections of every agglomerate with itself, also to maintain the analogy with the connectivity matrices. 

In the graphs: 
- healthy_G: graph of the healthy initial brain in of the first analysis 
- elementw_KG: K * G element wise application of the K operator on the healthy brain, in order to obtain the corrupted brain 
- rowbycol_KG: K @ G matrix multiplication application of the K operator on the healthy brain in order to obtain the corrupted brain 

In the text files:
- G: matrix representing the healthy initial brain, not symmetric, has 1 on the diagonal;
- K1: matrix representing the K operator for the computation of the corrupted brain, applying K1 to the healthy brain, not symmetric, does not have 1 on the diagonal.
- K1G: matrix representing the diseased brain after the application of K1 on G, using the element-wise multiplication;
- K1_at_G: matrix representing the diseased brain after the application of K1 on G, using the row by column multiplication; 
- eigenvalues_and_eigenvectors.txt sums up the eigenvalues and eigenvectors of the two different product matrices K1G and K1_at_G.

#### second part: computing K operator from an healthy brain and an already diseased brain 
Secondly we supposed to have the healthy brain G and the diseased brain Gk, matrices are defined with the same method as above, they are not symmetric but they do have 1 on the diagonal, in order to consider the connections of every agglomerate with itself, also to maintain the analogy with the connectivity matrices.

In the graphs: 
- healthy_G_forK: graph of the healthy initial brain in of the second analysis, in order to compute the K operator;
- inverse_G_forK: graph of the inverse of the G matrix, thus G^{-1}.

In the text files: 
- GforK: matrix of the healthy brain, the one used to compute the K operator;
- Gk: matrix of the already diseased brain, used to compute the K operator;
- G_1: inverse matrix of G, the name was given to recall the operation of inversion, G^{-1};
- K_elementw: K operator computed from the application of the element-wise multiplication between Gk and G^{-1};
- K_matmul: K operator obtained from the application of the matrix multiplication row by column between Gk and G^{-1}.
- K_matrices_eigenval_eigenvec.txt: sums up the eigenvalues and eigenvectors of the two different K operator obtaind with the two different matrix multiplication methods.

