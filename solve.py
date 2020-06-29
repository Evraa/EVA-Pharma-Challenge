'''
- Solve any given matrices of 3x3
- Fixed values are the ones that are non-zeors
'''
import numpy as np
from auxilary import *
import copy

    

def solve(mat, state):
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
    MAX_ITR = 100000
    MIN_IIR = 1
    ITR_CHECK = 100
    howManyTimes = 0
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
                        print("all done..\n")
                        print (mat)
                        print (f"the sum is: {magic}")
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
                            print("all done..\n")
                            print (mat)
                            print (f"the sum is: {magic}")
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
            ev_terminate = False
            while not ev_terminate:
                for i in range(MIN_IIR, MAX_ITR):
                    if not optionExist(mat,i):
                        mat[option_x, option_y] = i
                        if solveForced(mat, neighbours ):
                            return True
                        else:
                            mat = copy.deepcopy(orig_mat)
                    if i % ITR_CHECK == 0:
                        print (f'iteration from {MIN_IIR} to {i} did not give the deisred solution')
                        ev_key = str(input ("press 'Y' or 'y' for increasing to double it, any other key for termination: \n"))
                        if ev_key != 'y' and ev_key != 'Y':
                            return False
            print ("Sorry: no solution exist!")
        if len(option_list) == 2:
            option_1_x = option_list[0] // 3
            option_1_y = option_list[0] % 3
            option_2_x = option_list[1] // 3
            option_2_y = option_list[1] % 3
            mat = copy.deepcopy(orig_mat)
            while True:
                for i in range (MIN_IIR, MAX_ITR):
                    print ("working on it...")
                    if not optionExist(mat,i):
                        for j in range (1,1000):
                            if not optionExist(mat,j) and i != j:
                                mat[option_1_x, option_1_y] = i
                                mat[option_2_x, option_2_y] = j
                                if solveForced(mat, neighbours ):
                                    return True
                                else:
                                    mat = copy.deepcopy(orig_mat)
                                    mat[option_1_x, option_1_y] = j
                                    mat[option_2_x, option_2_y] = i
                                    if solveForced(mat, neighbours ):
                                        return True
                                    else:
                                        mat = copy.deepcopy(orig_mat)
                    if i % ITR_CHECK == 0:
                        print (f'iteration from {MIN_IIR} to {i} did not give the deisred solution')
                        ev_key = str(input ("press 'Y' or 'y' for increasing to double it, any other key for termination: \n"))
                        if ev_key != 'y' and ev_key != 'Y':
                            return False
                             
        if len(option_list) == 3:
            permutations = [[0,1,2],[0,2,1],[1,0,2],[2,0,1],[1,2,0],[2,1,0]]
            memoize = np.zeros([100,100,100])
            options_x = []
            options_y = []
            for i in range(3):
                options_x.append(option_list[i] // 3)
                options_y.append(option_list[i] % 3)

            mat = copy.deepcopy(orig_mat)
            while True:
                for i in range (1, 100):
                    print ("working on it...")
                    if not optionExist(mat,i):
                        for j in range (MIN_IIR, 100):
                            if not optionExist(mat,j) and i!=j:
                                for k in range (MIN_IIR, 100):
                                    if not optionExist(mat,k) and k!=j and k != i:
                                        if not weveBeenHere(memoize,i,j,k):
                                            for perm in permutations:
                                                mat[options_x[perm[0]], options_y[perm[0]]] = i
                                                mat[options_x[perm[1]], options_y[perm[1]]] = j
                                                mat[options_x[perm[2]], options_y[perm[2]]] = k
                                                if solveForced(mat, neighbours ):
                                                    if state == 5:
                                                        if howManyTimes >= 2:
                                                            print (f"this was solution number: 3")
                                                            return True
                                                        else:
                                                            howManyTimes += 1
                                                            print (f"this was solution number: {howManyTimes}")
                                                            
                                                    else:
                                                        return True
                                                else:
                                                    mat = copy.deepcopy(orig_mat)
                                            markThese(memoize,i,j,k)    
                   

        if len(option_list) == 0:
            print ("Error: no options asln!")
            return


def solve_ch_6(mat):
    '''
    A separate function for challenge 6
    because it has certain/special constraints

    Logic:
        + will start with four places
            o1 o2 o3
            _  o4  _
            _   _  _
        + these will be the options we have
        + so brutely we'll iterate four times to find the desired solutions
        + with memoization and fast checking for faster iterations
    '''

    #Assign data
    neighbours = meetTheNeighbours(mat) #neighbours of each cell, unchangable
    options = []
    for _ in range(9): options.append(0)
    MAX_ITR = 100
    howManyTimes = 0
    #Preparing the option cells
    options[0] = 1
    options[1] = 2
    options[2] = 3
    options[4] = 4
    options_x = [0,0,0,1]
    options_y = [0,1,2,1]
    #Prepare Permutations and memoize
    permutations = getMeFourPermutaions()
    memoize = np.zeros([MAX_ITR,MAX_ITR,MAX_ITR,MAX_ITR])
    while True:
        for i in range (1, MAX_ITR):
            if not optionExist(mat,i):
                print (f"working on it 1...{i}")
                for j in range (1, MAX_ITR):
                    if not optionExist(mat,j) and i!=j:
                        print (f"working on it 2...{i} of {j}")
                        for k in range (1, MAX_ITR):
                            if not optionExist(mat,k) and k!=j and k != i:
                                # print ("working on it 3...")
                                for l in range (1, MAX_ITR):
                                    if not optionExist(mat,l) and l != k and l != j and l != i:
                                        if not weveBeenHere_6(memoize,i,j,k,l):
                                            for perm in permutations:
                                                mat[options_x[perm[0]], options_y[perm[0]]] = i
                                                mat[options_x[perm[1]], options_y[perm[1]]] = j
                                                mat[options_x[perm[2]], options_y[perm[2]]] = k
                                                mat[options_x[perm[3]], options_y[perm[3]]] = l
                                                if solveForced_6(mat, neighbours ):
                                                    if howManyTimes >= 2:
                                                        print (f"this was solution number: 3")
                                                        return True
                                                    else:
                                                        howManyTimes += 1
                                                        print (f"this was solution number: {howManyTimes}")
                                                            
                                                else:
                                                    mat = np.zeros([3,3])
                                            markThese_6(memoize,i,j,k,l)    
