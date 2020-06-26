'''
- Solve any given matrices of 3x3
- Fixed values are the ones that are non-zeors
'''
import numpy as np
from auxilary import *
import copy


def solve(mat):
    '''
    The main Calling function with the algorithm.

    Algorithm:
        + The algo is divided into states, the matrix moves among them
    
    States:
        + Magic exist and ready to solve
        12 17 10
        11  _  _
        _   _  _

        + Magic exist and not ready to solve (option needed) --> add option
        5  7  16
        _  _  _
        _  _  _

        NOTE: the differnce between the first two is that to be on the first state
        you have got to have 4 numbers and magic number

        + add option...hard logic
        
        + option added and option needed

        + option added and magic exist
    '''

    #Assign data
    Neigh = meetTheNeighbours(mat) #neighbours of each cell, unchangable
    orig_mat = copy.deepcopy(mat) #original matrix, unchangeable

    #Check for magic
    magic = checkForMagic(mat)

    if magic and non_zeros >= 4:
        #state 1
        pass
    if magic and non_zeros < 4:
        #state 2..add option first and come back later
        pass
    while magic:
        force_Exist, forced_idx_x,forced_idx_y,val = checkForForced(mat,Neigh,magic)
        if force_Exist:
            #update the orig_mat
            mat[forced_idx_x][forced_idx_y] = val

            #check for violation
            if checkNoViolation(mat, magic):
                #check if all done
                if allDone(mat):
                    print("all done")
                    print (mat)
                    return
            else:
                #TODO: logic_3...go back a step
                pass
        else:
            #TODO: logic_1: add the best option
            pass
    
if __name__ == "__main__":
    #GLOBAL VARIABLES
    # orig_mat = np.zeros([3,3])
    # magic = 0


    #mat = np.arange(9).reshape(3, 3)
    mat = np.zeros([3,3])
    mat[0,0] = 12
    mat[0,1] = 17
    mat[0,2] = 10
    mat[1,0] = 11
    
    solve(mat)
    