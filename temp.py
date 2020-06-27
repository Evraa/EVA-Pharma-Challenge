exit_main = False
        option_occur = []
        while not exit_main:
            magic = checkForMagic(mat)
            while not magic:
                option_exist, state = addOption(mat, neighbours, 0, orig_mat, options)
                if option_exist:
                    option_occur.append(state)
                else:
                    print ("Error: no more options!")
                    return
                magic = checkForMagic(mat)
        #since we have magic
        #we need to force the answer
            exit_force = False
            step_back = False
            option_mat = copy.deepcopy(mat)
            while not exit_force:
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
                            exit_main = True
                            exit_force = True
                            step_back = False
                            return
                    else:
                        #move step backward
                        exit_force = True
                        step_back = True
                #force does not exist, and we ain't done yet...
                step_back = True
            if step_back:
                #Try first to increment the last option
                mat = copy.deepcopy(option_mat)
                inc_option = incrementOption (mat, neighbours, magic, orig_mat, options, option_occur)
                magic = checkForMagic(mat)
                if not inc_option:
                    removeOption(mat, options,option_occur)
