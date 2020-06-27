'''
- Solve any given matrices of 3x3
- Fixed values are the ones that are non-zeors
'''
import numpy as np
from auxilary import *
import copy


                
def solveForced(mat, neighbours ):
    main_exist = False
    magic = checkForMagic(mat)
    orig_mat = copy.deepcopy(mat)
    terminate_counter = 0
    while not main_exist:
        if terminate_counter == 9 :
            return False
        force_Exist, forced_idx_x,forced_idx_y,val = checkForForced(mat,neighbours,magic)
        if force_Exist:
            #update the mat
            mat[forced_idx_x][forced_idx_y] = val
            #check for violation
            if checkNoViolation(mat, magic):
                #check if all done
                if allDone(mat):
                    if resultIsValid (mat, magic):
                        print("all done")
                        print (mat)
                        return True
                    else:
                        mat = copy.deepcopy(orig_mat)
                        return False
            else:
                mat = copy.deepcopy(orig_mat)
                return False
        else:
            terminate_counter += 1

    

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
    MAX_ITR = 100
    #Check for magic
    magic = checkForMagic(mat)
    
    #Non zero elements
    non_zeros = np.where(mat != 0)

    #STATE 1: fill forced with no added options
    #Logic:
        # + Just filling the forced cells
    if magic and len(non_zeros[0]) >= 4:
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
    
    #STATE 2..add option first and come back later
    #Logic:
    #   + Find the best option available, the one cell close to most number of cells
    #   + try values from 1 to magic, except the unique/already used values
    #   + other cells will be forced for sure
    #   + did we reach a solution?
    #   + if not, try another option untill they're all done...
    #   + if no solution found, then exit...
    if magic and len(non_zeros[0]) < 4:
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
   
    #STATE 3: no magic, then option needed
#   Logic:
#       + find the position of your options
#       + 3 options are needed in the worst case
#       + try every permutation of these numbers and increment them inorder to find the working set
    if not magic:
        option_list = findListOfOptions(mat, neighbours, orig_mat,options)

        if len(option_list) == 1:
            option_x = option_list[0] // 3
            option_y = option_list[0] % 3
            for i in range(1, MAX_ITR):
                
                if not optionExist(mat,i):
                    mat[option_x, option_y] = i
                    if solveForced(mat, neighbours ):
                        return True
                    else:
                        mat = copy.deepcopy(orig_mat)
            print ("Sorry: no solution exist!")
        if len(option_list) == 2:
            pass
        if len(option_list) == 3:
            pass
        if len(option_list) == 0:
            print ("Error: no options asln!")
            return



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
    # mat[2,1] = 7
    mat [2,2] = 11
    # mat[1,1] = 1
    solve(mat)
    