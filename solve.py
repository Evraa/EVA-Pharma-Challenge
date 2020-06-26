'''
- Solve any given matrices of 3x3
- Fixed values are the ones that are non-zeors
'''
import numpy as np


def check (mat, magic=0):
    '''
    Checks if this matrix obey the rules (unique elements/summation)
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

def checkForMagic (mat):
    '''
    Return magic if exist, othw. returns false
    dummy operation
    '''

    if mat[0,0]!=0 and mat[0,1]!=0 and mat[0,2]!=0:
        return mat[0,0] + mat[0,1] + mat[0,2]

    if mat[1,0]!=0 and mat[1,1]!=0 and mat[1,2]!=0:
        return mat[1,0] + mat[1,1] + mat[1,2]

    if mat[2,0]!=0 and mat[2,1]!=0 and mat[2,2]!=0:
        return mat[2,0] + mat[2,1]!=0 + mat[2,2]

    if mat[0,0]!=0 and mat[1,0]!=0 and mat[2,0]!=0:
        return mat[0,0] + mat[1,0] + mat[2,0]

    if mat[0,1]!=0 and mat[1,1]!=0 and mat[2,1]!=0:
        return mat[0,1] + mat[1,1] + mat[2,1]

    if mat[0,2]!=0 and mat[1,2]!=0 and mat[2,2]!=0:
        return mat[0,2] + mat[1,2] + mat[2,2]

    if mat[0,0]!=0 and mat[1,1]!=0 and mat[2,2]!=0:
        return mat[0,0] + mat[1,1] + mat[2,2]

    if mat[0,2]!=0 and mat[1,1]!=0 and mat[2,0]!=0:
        return mat[0,2] + mat[1,1] + mat[2,0]
    
    return False



def solve(mat):
    print (checkForMagic(mat))

if __name__ == "__main__":
    #mat = np.arange(9).reshape(3, 3)
    mat = np.zeros([3,3])
    mat[0,0] = 2
    mat[0,1] = 7
    mat[0,2] = 6
    mat[1,0] = 9
    
    solve(mat)
    