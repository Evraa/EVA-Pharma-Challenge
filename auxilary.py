import numpy as np

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
                    if mat[neighbour_0[0]][[neighbour_0[1]]] != 0 and\
                        mat[neighbour_1[0]][[neighbour_1[1]]] != 0:
                        return True, i,j,(magic - mat[neighbour_0[0]][[neighbour_0[1]]] -\
                            mat[neighbour_1[0]][[neighbour_1[1]]])
    return False

def allDone (mat):
    '''
    Check on count of zeros
    '''
    for row in mat:
        for element in row:
            if element == 0:
                return False
    return True
    
