from numpy import *
#Problem 1:
def print_matrix(M_lol):
    print (array(M_lol))
#Problem 2:
def get_lead_ind(row):
    for i in range(len(row)):
        if (row[i] != 0):
            return i
    return len(row)
#Problem 3:
def get_row_to_swap(M, start_i):

    '''
    leading_nonzeros = {} 
    # dict stores the row index and index of first nonzero
    for i in range(start_i,len(M)):
        leading_nonzeros[i] = get_lead_ind(M[i]) 
    # minimum value (where first nonzero is) associated with the key (row)
    return min(leading_nonzeros, key=leading_nonzeros.get)
    '''
    first_nonzero_ind_list = []
    for j in range(start_i, len(M)):
        first_nonzero_ind_list.append(get_lead_ind(M[j]))
    return first_nonzero_ind_list.index(min(first_nonzero_ind_list)) + start_i
#Problem 4:
def add_rows_coefs(r1, c1, r2, c2):
    temp = []
    for k in range(len(r1)):
        temp.append(c1*r1[k] + c2*r2[k])
    return temp
#Problem 5:
def eliminate(M, row_to_sub, best_lead_ind):
    for a in range(row_to_sub+1, len(M)):
        factor = M[a][best_lead_ind] / M[row_to_sub][best_lead_ind]
        for b in range(len(M[a])):
            M[a][b] = M[a][b] - factor*M[row_to_sub][b]
    return M
#Problem 6:
def forward_step(M):
    """Takes in a matrix M, (list of lists)
    and applies the forward step of gaussian elimination
    to it, and modifies M to be the matrix obtained
    after the foreward step is applied 
    """
    for n in range(len(M)):
        ind = get_row_to_swap(M,n)
        M[n], M[ind] = M[ind], M[n]
        print(array(M))
        best_lead_ind_1 = get_lead_ind(M[n])
        eliminate(M, n, best_lead_ind_1)
        print(array(M))
        print("====================================================")

    backward_step(M)


#Problem 7:

def backward_step(M):
    """Takes in an arbitrary Matrix M and applies the backward
    step of Gaussian Elimination to it."""
    # to get the rref
    # no swapping here
    for r in range(len(M)-1, 0, -1):
        for r1 in range(r-1, -1, -1):
            try:
                M[r1] = add_rows_coefs(M[r1], 1, M[r], -1*(M[r1][best_lead_ind])/(M[r][best_lead_ind]))
            except IndexError:
                return 
M = [[5,  6, 7,  8],[0,0, 1, 1],[0, 0, 5, 2],[0, 0, 7, 0]]
forward_step(M)
backward_step(M)
print(M)
    


#Problem 8:
import copy
def solve(M, b):
    #making the augmented matrix:
    augmented = copy.deepcopy(M)
    for c in range(len(augmented)):
        augmented[c].append(b[c])
    #applying GE to the augmented matrix:

    forward_step(augmented)
    
    #solving for x:
    x = []
    for k in range(len(augmented)):
        x.append(augmented[k][-1])
    return x
'''
[[  1.    0.    0.   75. ]
 [  0.   16.    0.  160. ]
 [  0.    0.    3.5 -38.5]]
 '''

            

