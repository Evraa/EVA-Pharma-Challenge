'''
- Solve any given matrices of 3x3
- Fixed values are the ones that are non-zeors
'''
import numpy as np
from auxilary import *



def solve(mat):
    '''
    The main Calling function with the algorithm.

    Algorithm:
        + Assign needed data (Neigh,...)
        + Check if we have a Magic
            + if so, loop until all forced elements are filled
            + if not done yet, TODO: add options
        + if no magic, TODO: add options
    '''

    #Assign data
    Neigh = meetTheNeighbours(mat)

    #Check for magic
    magic = checkForMagic(mat)

    if magic:
        forced_idx_x,forced_idx_y,val = checkForForced(mat,Neigh,magic)
        
        print (forced_idx_x,forced_idx_y,val)

if __name__ == "__main__":
    #GLOBAL VARIABLES
    # orig_mat = np.zeros([3,3])
    # magic = 0


    #mat = np.arange(9).reshape(3, 3)
    mat = np.zeros([3,3])
    mat[0,0] = 2
    mat[0,1] = 7
    mat[0,2] = 6
    mat[1,0] = 9
    
    solve(mat)
    