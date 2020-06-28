import numpy as np
import copy, math
def meetTheNeighbours(mat):
    '''
    returns the neighbours of each cell

    neighbours:
        is a list of 9 elements
        0 -> [0,0]
        1 -> [0,1]
        2 -> [0,2]
        3 -> [1,0]
        4 -> [1,1]
        5 -> [1,2]
        6 -> [2,0]
        7 -> [2,1]
        8 -> [2,2]
    '''
    neighbours = []
    neighbours.append([ [[0,1],[0,2]], [[1,0],[2,0]], [[1,1],[2,2]] ])
    neighbours.append([ [[1,1],[2,1]], [[0,0],[0,2]]])
    neighbours.append([ [[0,1],[0,0]], [[1,2],[2,2]], [[1,1],[2,0]] ])
    neighbours.append([ [[1,1],[1,2]], [[0,0],[2,0]]])
    neighbours.append([ [[0,1],[2,1]], [[1,0],[1,2]], [[0,0],[2,2]], [[0,2],[2,0]] ])
    neighbours.append([ [[1,1],[1,0]], [[0,2],[2,2]]])
    neighbours.append([ [[0,0],[1,0]], [[2,1],[2,2]], [[1,1],[0,2]] ])
    neighbours.append([ [[2,0],[2,2]], [[0,1],[1,1]]])
    neighbours.append([ [[2,1],[2,0]], [[1,2],[0,2]], [[1,1],[0,0]] ])

    return neighbours

def checkForMagic (mat):
    '''
    Return magic if exist, othw. returns false
    dummy operation
    '''
    #row 1
    if mat[0,0]!=0 and mat[0,1]!=0 and mat[0,2]!=0:
        return mat[0,0] + mat[0,1] + mat[0,2]
    #row 2
    if mat[1,0]!=0 and mat[1,1]!=0 and mat[1,2]!=0:
        return mat[1,0] + mat[1,1] + mat[1,2]
    #row 3
    if mat[2,0]!=0 and mat[2,1]!=0 and mat[2,2]!=0:
        return mat[2,0] + mat[2,1]!=0 + mat[2,2]
    #col 1
    if mat[0,0]!=0 and mat[1,0]!=0 and mat[2,0]!=0:
        return mat[0,0] + mat[1,0] + mat[2,0]
    #col 2
    if mat[0,1]!=0 and mat[1,1]!=0 and mat[2,1]!=0:
        return mat[0,1] + mat[1,1] + mat[2,1]
    #col 3
    if mat[0,2]!=0 and mat[1,2]!=0 and mat[2,2]!=0:
        return mat[0,2] + mat[1,2] + mat[2,2]
    #diagonal right
    if mat[0,0]!=0 and mat[1,1]!=0 and mat[2,2]!=0:
        return mat[0,0] + mat[1,1] + mat[2,2]
    #diagonal left
    if mat[0,2]!=0 and mat[1,1]!=0 and mat[2,0]!=0:
        return mat[0,2] + mat[1,1] + mat[2,0]
    
    return False


def checkNoViolation (mat, magic=0):
    '''
    Checks if this matrix does not break any of the restrictions
    '''
    #count uniques
    npn_zero_elements = []
    for i in mat:
        for j in i:
            if j!=0:
                npn_zero_elements.append(j)

    unique_elements = len(np.unique(npn_zero_elements))
    if unique_elements != len(npn_zero_elements) :
        return False

    #Check row summation is the same
    sum_x = mat.sum(axis=0)
    for element in sum_x:
        if element > magic:
            return False
    
    #Check column summation is the same
    sum_y = mat.sum(axis=1)
    for element in sum_y:
        if element > magic:
            return False

    #check diagonals
    if mat[0,0]+mat[1,1]+mat[2,2] > magic or mat[0,2]+mat[1,1]+mat[2,0] > magic:
        return False    
    return True

def checkForForced (mat, neighbours, magic):
    '''
    return the index of one of the FORCED cells
    if non exist, returns False
    '''
    n,m = mat.shape
    for i in range(n):
        for j in range(m):
            if mat[i,j] == 0:
                #Check for its neighbours
                idx = (i*3) + j
                for neighbour in neighbours[idx]:
                    neighbour_0 = neighbour[0]
                    neighbour_1 = neighbour[1]
                    #exist
                    if mat[neighbour_0[0]][[neighbour_0[1]]] != 0 and\
                        mat[neighbour_1[0]][[neighbour_1[1]]] != 0:
                        #valid
                        value = magic - mat[neighbour_0[0]][[neighbour_0[1]]] - mat[neighbour_1[0]][[neighbour_1[1]]]
                        if value > 0:
                            if not optionExist(mat, value):
                                return True, i,j, value
    return False, None, None, None

def allDone (mat):
    '''
    Check on count of zeros
    '''
    for row in mat:
        for element in row:
            if element == 0:
                return False
    return True
    
def getBestOption(mat, neighbours):
    max_cells = 0
    cell_with_max_neighbours_x = None
    cell_with_max_neighbours_y = None
    N,M = mat.shape
    for i in range(N):
        for j in range(M):
            if j == 1 and i == 1:
                continue
            if mat[i,j] == 0:
                idx = (i*3) + j
                neighbour_count = 0
                for neighbour in neighbours[idx]:
                    neighbour_0 = neighbour[0]
                    neighbour_1 = neighbour[1]
                    if mat[neighbour_0[0]][[neighbour_0[1]]] != 0:
                        neighbour_count += 1
                    if mat[neighbour_1[0]][[neighbour_1[1]]] != 0:
                        neighbour_count += 1
                if neighbour_count > max_cells:
                    max_cells = neighbour_count
                    cell_with_max_neighbours_x = i
                    cell_with_max_neighbours_y = j
    #special check for the center point needs to be at last
    if mat[1,1] == 0:
        idx = 4
        neighbour_count = 0
        for neighbour in neighbours[idx]:
            neighbour_0 = neighbour[0]
            neighbour_1 = neighbour[1]
            if mat[neighbour_0[0]][[neighbour_0[1]]] != 0:
                neighbour_count += 1
            if mat[neighbour_1[0]][[neighbour_1[1]]] != 0:
                neighbour_count += 1
        if neighbour_count > max_cells:
            max_cells = neighbour_count
            cell_with_max_neighbours_x = 1
            cell_with_max_neighbours_y = 1

    if cell_with_max_neighbours_x is not None:
        return True, cell_with_max_neighbours_x, cell_with_max_neighbours_y
    return False, None, None

def optionExist (mat, option):
    non_zeros = np.where(mat == option)
    if len(non_zeros[0]) >= 1:
        return True
    return False

def resultIsValid(mat, magic):
    
    #Check row summation is the same
    sum_x = mat.sum(axis=0)
    if sum_x[0] != sum_x[1] or sum_x[1] != sum_x[2] or sum_x[2] != magic:
        return False
    
    #Check column summation is the same
    sum_y = mat.sum(axis=1)
    if sum_y[0] != sum_y[1] or sum_y[1] != sum_y[2] or sum_y[2] != magic:
        return False
    
    #check diagonals
    if mat[0,0]+mat[1,1]+mat[2,2] != magic or mat[0,2]+mat[1,1]+mat[2,0] != magic:
        return False    
    return True


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
        if options[idx] > magic and magic != 0:
            #one step back
            return False, 0
        else:   
            mat[option_x, option_y] = options[idx] 
            return True, idx

    else:
        #Report problem!
        print ("Error: no options are available")
        print ("matrix: ")
        print (mat)   
        return False, 1


def incrementOption (mat, neighbours, magic, orig_mat, options, option_occur):
    '''
    Increments the last option we have created
    '''
    last_option_idx = len(option_occur) - 1
    last_option = option_occur[last_option_idx]

    options[last_option] += 1
    while optionExist (mat, options[last_option]):
        options[last_option] += 1
    if options[last_option] > magic:
        #one step back
        return False, 0

    option_x = last_option // 3
    option_y = last_option % 3
    mat[option_x, option_y] = options[last_option]
    return True, 1

def removeOption (mat, options, option_occur):
    '''
    Remove the last existed/created option we have
    '''
    last_option_idx = len(option_occur) - 1
    last_option = option_occur[last_option_idx]
    option_x = last_option // 3
    option_y = last_option % 3

    mat[option_x, option_y] = 0
    option_occur.remove(last_option)
    options[last_option] = 0

    return True

def checkForCross(mat):
    #check for cross!
    if mat[0,1] != 0 and mat[1,1] != 0 and mat[2,1] != 0:
        #Vertical
        if mat[1,0] != 0 or mat[1,2] != 0:
            return True
    if mat[1,0] != 0 and mat[1,1] != 0 and mat[1,2] != 0:
        #Horizontal
        if mat[0,1] != 0 or mat[2,1] != 0:
            return True
    return False


def findListOfOptions(mat, neighbours, orig_mat,options):
    option_list = []
    #Add first option
    option_exist, state = addOption(mat, neighbours, 0, orig_mat, options)
    #if found, append it
    if option_exist: option_list.append(state)
    #do we reach magic?
    magic = checkForMagic(mat)
    #how many numbers do we have?
    non_zeros = np.where(mat != 0)
    crossExist = False
    if len(non_zeros[0]) == 4:
        crossExist = checkForCross(mat)
    while not magic or len(non_zeros[0]) < 4 or crossExist:
        option_exist, state = addOption(mat, neighbours, 0, orig_mat, options)
        if option_exist: option_list.append(state)
        magic = checkForMagic(mat)
        non_zeros = np.where(mat != 0)
        crossExist = False
    
    return option_list 

def markThese(memoize,i,j,k):
    memoize[i,j,k] = -1
    memoize[i,k,j] = -1
    memoize[j,i,k] = -1
    memoize[k,i,j] = -1
    memoize[j,k,i] = -1
    memoize[k,j,i] = -1
    return

def markThese_6(memoize,i,j,k,l):
    memoize[i,j,k,l] = -1
    memoize[i,k,j,l] = -1
    memoize[j,i,k,l] = -1
    memoize[k,i,j,l] = -1
    memoize[j,k,i,l] = -1
    memoize[k,j,i,l] = -1

    memoize[i,j,l,k] = -1
    memoize[i,k,l,j] = -1
    memoize[j,i,l,k] = -1
    memoize[k,i,l,j] = -1
    memoize[j,k,l,i] = -1
    memoize[k,j,l,i] = -1

    memoize[i,l,j,k] = -1
    memoize[i,l,k,j] = -1
    memoize[j,l,i,k] = -1
    memoize[k,l,i,j] = -1
    memoize[j,l,k,i] = -1
    memoize[k,l,j,i] = -1

    memoize[l,i,j,k] = -1
    memoize[l,i,k,j] = -1
    memoize[l,j,i,k] = -1
    memoize[l,k,i,j] = -1
    memoize[l,j,k,i] = -1
    memoize[l,k,j,i] = -1
    return

def weveBeenHere(memoize,i,j,k):
    if memoize[i,j,k] == -1:
        return True
    if memoize[i,k,j] == -1:
        return True
    if memoize[j,i,k] == -1:
        return True
    if memoize[i,j,k] == -1:
        return True
    if memoize[k,i,j] == -1:
        return True
    if memoize[j,k,i] == -1:
        return True
    if memoize[k,j,i] == -1:
        return True
    
    return False

def weveBeenHere_6(memoize,i,j,k,l):
    if memoize[i,j,k,l] == -1:
        return True
    if memoize[i,k,j,l] == -1:
        return True
    if memoize[j,i,k,l] == -1:
        return True
    if memoize[i,j,k,l] == -1:
        return True
    if memoize[k,i,j,l] == -1:
        return True
    if memoize[j,k,i,l] == -1:
        return True
    if memoize[k,j,i,l] == -1:
        return True

    if memoize[i,j,l,k] == -1:
        return True
    if memoize[i,k,l,j] == -1:
        return True
    if memoize[j,i,l,k] == -1:
        return True
    if memoize[i,j,l,k] == -1:
        return True
    if memoize[k,i,l,j] == -1:
        return True
    if memoize[j,k,l,i] == -1:
        return True
    if memoize[k,j,l,i] == -1:
        return True

    if memoize[i,l,j,k] == -1:
        return True
    if memoize[i,l,k,j] == -1:
        return True
    if memoize[j,l,i,k] == -1:
        return True
    if memoize[i,l,j,k] == -1:
        return True
    if memoize[k,l,i,j] == -1:
        return True
    if memoize[j,l,k,i] == -1:
        return True
    if memoize[k,l,j,i] == -1:
        return True

    if memoize[l,i,j,k] == -1:
        return True
    if memoize[l,i,k,j] == -1:
        return True
    if memoize[l,j,i,k] == -1:
        return True
    if memoize[l,i,j,k] == -1:
        return True
    if memoize[l,k,i,j] == -1:
        return True
    if memoize[l,j,k,i] == -1:
        return True
    if memoize[l,k,j,i] == -1:
        return True
    
    return False

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
                        print("all done..\n")
                        print (mat)
                        print (f"the sum is: {magic}")
                        return True
                    else:
                        mat = copy.deepcopy(orig_mat)
                        return False
            else:
                mat = copy.deepcopy(orig_mat)
                return False
        else:
            terminate_counter += 1


def getMeFourPermutaions():
    perm = []
    perm.append([0,1,2,3])
    perm.append([0,1,3,2])
    perm.append([0,2,1,3])
    perm.append([0,3,1,2])
    perm.append([0,2,3,1])
    perm.append([0,3,2,1])

    perm.append([1,0,2,3])
    perm.append([1,0,3,2])
    perm.append([2,0,1,3])
    perm.append([3,0,1,2])
    perm.append([2,0,3,1])
    perm.append([3,0,2,1])
    
    perm.append([1,2,0,3])
    perm.append([1,3,0,2])
    perm.append([2,1,0,3])
    perm.append([3,1,0,2])
    perm.append([2,3,0,1])
    perm.append([3,2,0,1])

    perm.append([1,2,3,0])
    perm.append([1,3,2,0])
    perm.append([2,1,3,0])
    perm.append([3,1,2,0])
    perm.append([2,3,1,0])
    perm.append([3,2,1,0])

    return perm

def solveForced_6(mat, neighbours ):
    main_exist = False
    magic = checkForMagic_6(mat)
    orig_mat = copy.deepcopy(mat)
    terminate_counter = 0
    while not main_exist:
        if terminate_counter == 9 :
            return False
        force_Exist, forced_idx_x,forced_idx_y,val = checkForForced_6(mat,neighbours,magic)
        if force_Exist:
            #update the mat
            mat[forced_idx_x][forced_idx_y] = val
            #check for violation
            if checkNoViolation_6(mat, magic):
                #check if all done
                if allDone(mat):
                    if resultIsValid_6 (mat, magic):
                        print("all done..\n")
                        print (mat)
                        print (f"the sum is: {magic}")
                        return True
                    else:
                        mat = copy.deepcopy(orig_mat)
                        return False
            else:
                mat = copy.deepcopy(orig_mat)
                return False
        else:
            terminate_counter += 1

def checkForForced_6 (mat, neighbours, magic):
    '''
    return the index of one of the FORCED cells
    if non exist, returns False
    '''
    n,m = mat.shape
    for i in range(n):
        for j in range(m):
            if mat[i,j] == 0:
                #Check for its neighbours
                idx = (i*3) + j
                for neighbour in neighbours[idx]:
                    neighbour_0 = neighbour[0]
                    neighbour_1 = neighbour[1]
                    #exist
                    if mat[neighbour_0[0]][[neighbour_0[1]]] != 0 and\
                        mat[neighbour_1[0]][[neighbour_1[1]]] != 0:
                        #valid
                        val1 = math.pow(mat[neighbour_0[0]][[neighbour_0[1]]],2)
                        val2 = math.pow( mat[neighbour_1[0]][[neighbour_1[1]]],2) 
                        value = math.pow(magic,2) - val1 - val2
                        if value > 0:
                            if not optionExist(mat, value):
                                return True, i,j, value
    return False, None, None, None

def checkNoViolation_6 (orig_mat, magic=0):
    '''
    Checks if this matrix does not break any of the restrictions
    '''
    #count uniques
    npn_zero_elements = []
    for i in orig_mat:
        for j in i:
            if j!=0:
                npn_zero_elements.append(j)

    unique_elements = len(np.unique(npn_zero_elements))
    if unique_elements != len(npn_zero_elements) :
        return False

    #Check row summation is the same
    mat = np.power(orig_mat,2)
    sum_x = mat.sum(axis=0)
    for element in sum_x:
        if element > magic:
            return False
    
    #Check column summation is the same
    sum_y = mat.sum(axis=1)
    for element in sum_y:
        if element > magic:
            return False

    #check diagonals
    if mat[0,0]+mat[1,1]+mat[2,2] > magic and mat[0,2]+mat[1,1]+mat[2,0] > magic:
        return False    
    return True

def checkForMagic_6 (orig_mat):
    '''
    Return magic if exist, othw. returns false
    dummy operation
    '''
    mat = np.power(orig_mat,2)
    #row 1
    if mat[0,0]!=0 and mat[0,1]!=0 and mat[0,2]!=0:
        return mat[0,0] + mat[0,1] + mat[0,2]
    #row 2
    if mat[1,0]!=0 and mat[1,1]!=0 and mat[1,2]!=0:
        return mat[1,0] + mat[1,1] + mat[1,2]
    #row 3
    if mat[2,0]!=0 and mat[2,1]!=0 and mat[2,2]!=0:
        return mat[2,0] + mat[2,1]!=0 + mat[2,2]
    #col 1
    if mat[0,0]!=0 and mat[1,0]!=0 and mat[2,0]!=0:
        return mat[0,0] + mat[1,0] + mat[2,0]
    #col 2
    if mat[0,1]!=0 and mat[1,1]!=0 and mat[2,1]!=0:
        return mat[0,1] + mat[1,1] + mat[2,1]
    #col 3
    if mat[0,2]!=0 and mat[1,2]!=0 and mat[2,2]!=0:
        return mat[0,2] + mat[1,2] + mat[2,2]
    #diagonal right
    if mat[0,0]!=0 and mat[1,1]!=0 and mat[2,2]!=0:
        return mat[0,0] + mat[1,1] + mat[2,2]
    #diagonal left
    if mat[0,2]!=0 and mat[1,1]!=0 and mat[2,0]!=0:
        return mat[0,2] + mat[1,1] + mat[2,0]
    
    return False

def resultIsValid_6(orig_mat, magic):
    
    #Check row summation is the same
    mat = np.power(orig_mat,2)
    sum_x = mat.sum(axis=0)
    if sum_x[0] != sum_x[1] or sum_x[1] != sum_x[2] or sum_x[2] != magic:
        return False
    
    #Check column summation is the same
    sum_y = mat.sum(axis=1)
    if sum_y[0] != sum_y[1] or sum_y[1] != sum_y[2] or sum_y[2] != magic:
        return False
    
    #check diagonals
    if mat[0,0]+mat[1,1]+mat[2,2] != magic and mat[0,2]+mat[1,1]+mat[2,0] != magic:
        return False    
    return True
