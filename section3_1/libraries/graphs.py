# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:06:39 2012

@author: deniz
"""
###########################################
#####    GRAPH VISUALISATION TOOL  ########
###########################################

""" a 2D environment to represent graphs 
To visualize up to 8 node graphs !!!"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

new_mpl = int(mpl.__version__[2]) > 2
print(new_mpl)

""" if A represents a weighted graph for the sake of visualisation 
we use integers like 1,2,3,4 """


def arrow(x1, x2, line_wd, weight_on=True, Directed=True):
    # the curved arrow  : The convention j ---> i => x2 ----> x1
    n = 100
    coord_mid = np.array([(x2[0] + x1[0]) / 2, (x2[1] + x1[1]) / 2])
    ###### location and direction of the arrow : 1 -->> 2 ####
    # detect the quadrant of the point two when 1 is the origin
    color = "r"  # indirected
    quad = 1.0
    if Directed:
        if (x2[1] - x1[1]) < 0.0:
            quad = 1.0
            color = "r"
        else:
            color = "g"
            quad = -1.0
    #######  Coordinates of the curve ####
    L = np.linalg.norm(np.array(x1) - np.array(x2))
    curve_x = np.linspace(-L / 2, L / 2, n)
    angle = np.linspace(-np.pi / 2, np.pi / 2, n)
    curve_y = 0.2 * L * np.cos(angle) * quad
    curve_coord = np.array([curve_x, curve_y])
    ########### Rotate the curve #######
    theta = np.arctan((x2[1] - x1[1]) / (x2[0] - x1[0]))
    # angle always positive
    if theta < 0.0:
        theta += np.pi
    ## rotation by theta
    M_rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    curve_new = np.dot(M_rot, curve_coord)
    ## shift of the center
    for i in range(n):
        curve_new[:, i] = curve_new[:, i] + coord_mid[:]
    ############## PLOT ###########
    ## The arrow
    if Directed:
        if quad == 1.0:
            dx = curve_new[0][95] - curve_new[0][92]
            dy = curve_new[1][95] - curve_new[1][92]
            if new_mpl:
                plt.arrow(
                    curve_new[0][92],
                    curve_new[1][92],
                    dx,
                    dy,
                    width=0.0008 * line_wd + 0.001,
                    length_includes_head=True,
                    color=color,
                    alpha=1.0,
                )
            else:
                plt.arrow(
                    curve_new[0][92],
                    curve_new[1][92],
                    dx,
                    dy,
                    width=0.008 * line_wd + 0.01,
                    length_includes_head=True,
                    color=color,
                    alpha=1.0,
                )

        else:
            dx = curve_new[0][2] - curve_new[0][5]
            dy = curve_new[1][2] - curve_new[1][5]
            if new_mpl:
                plt.arrow(
                    curve_new[0][5],
                    curve_new[1][5],
                    dx,
                    dy,
                    width=0.0008 * line_wd + 0.001,
                    length_includes_head=True,
                    color=color,
                    alpha=1.0,
                )
            else:
                plt.arrow(
                    curve_new[0][5],
                    curve_new[1][5],
                    dx,
                    dy,
                    width=0.008 * line_wd + 0.01,
                    length_includes_head=True,
                    color=color,
                    alpha=1.0,
                )

    #    ## the curve
    plt.plot(
        curve_new[0][3:96],
        curve_new[1][3:96],
        color=color,
        linewidth=2 * line_wd,
        alpha=0.5,
    )
    ## weight value on curve
    if weight_on:
        plt.text(
            curve_new[0][50], curve_new[1][50], str(line_wd), fontsize=12, alpha=1.0
        )
    plt.grid()


def graph_draw(A, Directed=True, Weighted=True, Index_on=True, Weight_on=True):
    """A : NxN matrix
    ----Options:(True or False)----
    -Directed
    -Weighted
    -Index_on
    -Weight_on

    This visualiser is appropriate for visualizing up to 10 node
    graphs. A is the matrix that represents the graph. The convention
    is if A_ij=1, then there is a connection 'from' the jth node 'to' the ith
    node.
    """
    #    ''' A is the adjecency matrix (or weight matrix)  of a Graph G'''
    #    ''' No self connections. TODO: self sonnections '''
    #    ''' TO DO: exitatory inhibitory networks with different colors '''
    #    ''' TO DO: positions of nodes as input or generated randomly
    #               for larger number of nodes '''
    #### generate angles on a circle: NODE POSITIONs ####
    n = np.shape(A)[0]
    angles = np.linspace(0, (2 * np.pi * (n - 1)) / n, n)
    position = [np.exp(angles * 1j).real, np.exp(1j * angles).imag]
    plt.plot(position[0], position[1], "bo", markersize=30.0, alpha=0.5)
    ##### index postions  #####
    if Index_on:
        ## index positions
        p_index = [1.21 * np.exp(angles * 1j).real, 1.21 * np.exp(1j * angles).imag]
        for i in range(n):
            plt.text(p_index[0][i], p_index[1][i], str(i + 1), fontsize=22)
    ###### Draw curves (+arrows) from nodes to nodes ####
    for i in range(n):  ## Coloumn index : FROM
        coord1 = [position[0][i], position[1][i]]
        for j in range(n):  ## Row index : TO
            ## differentiate in and out
            if (i > j or i < j) and np.abs(A[i, j]) > 0.0:
                coord2 = [position[0][j], position[1][j]]
                ## set different linewidths for weighted graphs
                if Weighted:
                    line_wd = np.abs(A[i, j])
                else:
                    line_wd = 2.0
                ## for better visualization in directed:
                # different in and out colors

                arrow(coord1, coord2, line_wd, Weight_on, Directed)

        plt.xlim([-1.5, 1.5])
        plt.ylim([-1.5, 1.5])
        plt.axis("off")
        plt.box(True)


### Test
