
#Problem 1:
def list1_start_with_list2(list1, list2):
    if (len(list1) >= len(list2)):
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                return False
        return True
    else:
        return False


#Problem 2:
def match_pattern(list1, list2):
    if (len(list2) > len(list1)):
        return False
    else:
        for i in range(0, len(list1)):
            if list1[i : i + len(list2)] == list2:
                return True
        return False


#Problem 3:
def repeats(list0):
    for a in range(len(list0)):
        if (a < len(b) - 1):
            if (list0[a] == list0[a + 1]):
                return True
    return False


#Problem 4a:
def print_matrix_dim(M):
    print (str(len(M)) + 'x' + str(len(M[0])))

#Problem 4b:
import numpy as np
def mult_M_v(M, v):
    vector = np.zeros(len(v))
    for i in range(len(v)):
        product = 0
        for j in range(len(M[0])):
            product += (M[i][j] * v[j])
        vector[i] = product
    return vector




def matrix_mult(m1,m2):

    l1 = []
    M3 = []
    # number of rows of first equals number of cols of second
    if len(m1[0]) == len(m2):
        # loop through rows of M1
        for i in range(len(m1)):
        # loop through columns of M2
            for j in range(len(m2[0])):
                sums = 0
                # loop through rows
                for k in range(len(m2)):
                    sums += m1[i][k] * m2[k][j]

                l1.append(sums)
            M3.append(l1)
            l1 = []

        return M3





