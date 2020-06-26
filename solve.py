'''
- Solve any given matrices of 3x3
- Fixed values are the ones that are non-zeors
'''
import numpy as np
from auxilary import *
import copy

def addOption (mat, neighbours, magic, orig_mat, options):
    '''
    Adds option to the best cell (cell with most effect)

    return True:
        if option is added successfully
    return False: in case of erros
        0: option extends magic
        1: no options at all !
    '''
    option_exist, option_x , option_y = getBestOption(mat,neighbours)
    
    if option_exist:
        idx = (option_x*3) + option_y
        options[idx] += 1
        while optionExist (mat, options[idx]):
            options[idx] += 1
        if options[idx] > magic:
            #one step back
            return False, 0
        else:   
            mat[option_x, option_y] = options[idx] 
            return True, 1

    else:
        #Report problem!
        print ("Error: no options are available")
        print ("matrix: ")
        print (mat)   
        return False, 1
                

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
        
        + option added and option needed

        + option added and magic exist
    '''

    #Assign data
    neighbours = meetTheNeighbours(mat) #neighbours of each cell, unchangable
    orig_mat = copy.deepcopy(mat) #original matrix, unchangeable
    options = []
    for _ in range(9): options.append(0)

    #Check for magic
    magic = checkForMagic(mat)
    
    #Non zero elements
    non_zeros = np.where(mat != 0)

    if magic and len(non_zeros[0]) >= 4:
        #state 1: fill forced with no added options
        main_exist = False
        while not main_exist:
            force_Exist, forced_idx_x,forced_idx_y,val = checkForForced(mat,neighbours,magic)
            if force_Exist:
                #update the mat
                mat[forced_idx_x][forced_idx_y] = val
                #check for violation
                if checkNoViolation(mat, magic):
                    #check if all done
                    if allDone(mat):
                        print("all done")
                        print (mat)
                        main_exist = True
        return
        
    if magic and len(non_zeros[0]) < 4:
        #state 2..add option first and come back later
        exit_main = False
        while not exit_main:
            # options_count = 0
            #add option
            option_exist, state = addOption(mat, neighbours, magic, orig_mat, options)
            if not option_exist:
                print ("Sorry, no solution available for this set of numbers")
                print (orig_mat)
                return 
            #check for forced
            force_Exist, forced_idx_x,forced_idx_y,val = checkForForced(mat,neighbours,magic)

            #I know force will exist
            exit_sub = False
            while force_Exist and not exit_sub:
                #update the mat
                mat[forced_idx_x][forced_idx_y] = val
                #check for violation
                if checkNoViolation(mat, magic):
                    #check if all done
                    if allDone(mat):
                        if resultIsValid (mat, magic):
                            print("all done")
                            print (mat)
                            exit_main = True
                            return
                else:
                    #increment the option
                    exit_sub = True
                force_Exist, forced_idx_x,forced_idx_y,val = checkForForced(mat,neighbours,magic)
            
            #if reached here, no force exist and not all elements are filled,
            #move backward with your options.

            #remove option
            mat = copy.deepcopy(orig_mat)
   
if __name__ == "__main__":
    #GLOBAL VARIABLES
    # orig_mat = np.zeros([3,3])
    # magic = 0


    #mat = np.arange(9).reshape(3, 3)
    mat = np.zeros([3,3])
    # mat[0,0] = 5
    mat[0,1] = 7
    mat[0,2] = 16
    mat[1,0] = 15
    
    solve(mat)
    