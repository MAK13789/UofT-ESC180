#Problem 1:
def sum_cubes(k):
    output = 0
    for i in range(1, k + 1):
        output += i**3
    return (output)


#Problem 2:
def sum_cubes_num_terms(n):
    j = 1
    while True:
        if sum_cubes(j) >= n:
            return (j)
        j += 1


#Problem 3:
def moving_average(measurements):
    output_list = []
    for k in range(1, len(measurements)-1):
        average = (measurements[k-1] + measurements[k] + measurements[k+1]) / 3
        output_list.append(average)
    return output_list


#Problem 4:
def match(pattern, text):
    for a in range(0, len(text)):
        for b in range(0, len(text)):
            if (a < b):
                temp = text[a : b]
                if (temp == pattern):
                    return True
            if (a >= b):
                temp_1 = text[a : len(text)]
                temp_2 = text[0 : b]
                temp_3 = temp_1 + temp_2
                if (temp_3 == pattern):
                    return True
    return False


#Problem 5:
def get_cols(M):
    cols = []
    for c in range(len(M)):
        temp_7 = []
        for d in range(len(M)):
            temp_7.append(M[d][c])
        cols.append(temp_7)
    return (cols)
def share_n1(M1, M2):
    M1_cols = get_cols(M1)
    M2_cols = get_cols(M2)
    num = 0
    for e in range(0, len(M1_cols)):
        for f in range(0, len(M2_cols)):
            if (M1_cols[e] == M2_cols[f]):
                num += 1
    if num >= len(M1_cols) - 1:
        return True
    else:
        return False
