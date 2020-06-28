'''
- Read and parse inputs from terminal
- Call solve
- Output the final results
'''
from solve import *

def welcome():
    valid_entry = False
    print ("Welcome for EVA Pharma challange.")
    option = str(input ("Pick number from 1 to 6 to show the challange and its answer\
            \nIf you would like to enter a new matrix, please press 0,\
            \nbut make sure its solvable, or an Error message will come up...Thank You\
            \n"))

    if option == '0' or option == '1' or option == '2' or option == '3' or option == '4' or option == '5' or option == '6':
        valid_entry = True

    while not valid_entry:
        option = str(input ("Please make sure to pick number from 1 to 6, or even 0 for new inputs!"))
        if option == '0' or option == '1' or option == '2' or option == '3' or option == '4' or option == '5' or option == '6':
            valid_entry = True

    if option == '0':
        print ("please enter 9 numbers in that order:\n")
        print ("\t0 1 2")
        print ("\t3 4 5")
        print ("\t6 7 8")
        print("to enter an empty cell enter 0")
        mat = np.zeros([3,3])
        for i in range (3):
            for j in range (3):
                x = str(input (f'entry: [{i},{j}]: '))
                mat[i,j] = int(x)
                print (mat)
        return mat
    # if option == '1':
    # if option == '2':
    # if option == '3':
    # if option == '4':
    # if option == '5':
    # if option == '6':
        

if __name__ == "__main__":
    mat = welcome()
    print ("Solving: ")
    print (mat)
    solve(mat)
    