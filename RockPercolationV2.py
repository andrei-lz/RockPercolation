# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:23:33 2020

@author: jbru
"""
## Simulate a drop of liquid percolating down through a mixture of
## sand and rock.
##
## Generate a random 100x100 matrix of 0's and 1's where 1 corresponds
## to rock and 0 corresponds to sand.  Generate the values in the
## matrix independently, based on a given probability p that each
## space is occupied by rock.
##
## A drop of liquid starts in the middle of the top layer (row 1,
## column 50).  It then moves according to the following four options,
## where options with lower numbers have higher precedence.
##
## 1. If the space directly below is sand, move there.
## 2. If the space below and to the left is sand, move there.
## 3. If the space below and to the right is sand, move there.
## 4. If the space directly to the right is sand, move there.
##
## If none of these moves can be made, the drop of liquid is stuck.
##
## Use simulation to calculate the average depth to which the liquid
## drops before getting stuck, and the proportion of the time that the
## drop reaches the bottom layer.

import numpy as np 
import matplotlib.pyplot as plt 
#import matplotlib.animation as animation 

## The density of rocks in the sand.
# p = 1 - 0.599

## The number of simulation replications.
nrep_list = [1e2, 5e2, 1e3, 2e3, 4e3]
nrep = 1e3

## The total depth across the simulation replications.
TD = 0

## The number of times that the bottom is reached.
NB = 0

# Grid size
N_list = [10, 50, 100, 200, 400]
N = 400

nb_list = []
td_list = []

x = np.arange(0, 1, 0.01)

for p in np.arange(0, 1, 0.01):
    NB = 0
    TD = 0
    ## Simulation replications.
    for i in range(int(nrep)):
        ## Randomly lay out the rocks.
        M = (1*(np.random.uniform(0,1,size=N*N) < p)).reshape(N,N)
        ## The initial position of the droplet.
        r = 0
        c = int(N/2) -1
        ## Let the droplet percolate through the rocks.
        while r < N-1 and c < N-1:
            ## Always go straight down if possible.
            if (M[r+1,c] == 0): 
                r = r+1        
            ## Next try down/left.
            elif ( (c>1) & (M[r+1,c-1] == 0) ) :
                r = r+1
                c = c-1        
            ## Next try down/right.
            elif ( (c<N) & (M[r+1,c+1] == 0) ) :
                r = r+1
                c = c+1        
            ## Next try right.
            elif ( (c<100) & (M[r,c+1] == 0) ) :
                c = c+1        
            ## We're stuck
            else: 
                break 
        ## Keep track of how often we reach the bottom. 
        if (r==N-1) :
            NB = NB + 1 
        ## Keep track of the total of the final depths.
        TD = TD + r

    ## The estimated probability that we reach the bottom.
    NB = NB/nrep

    ## The average depth that is reached.
    TD = TD/nrep

    nb_list.append(NB)
    td_list.append(TD)

print("Reached Depth:", TD)
print("Probability of Reaching the Bottom:", NB)

plt.plot(x, nb_list)
plt.title("Graph Showing the Probability of Complete Percolation for Given Densities of Rock", fontSize=18)
plt.ylabel("Probability of Reaching the Bottom")
plt.xlabel("Density")
save_title = "n" + str(N) + "nrep" + str(nrep) +".png"
plt.savefig(save_title, bbox_inches="tight")
plt.close()