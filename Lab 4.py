'''
#Problem 1:
def count_evens(L):
    count = 0
    for i in range(len(L)):
        is_even = L[i] % 2
        if (is_even == 0):
            count += 1
    return count
'''
'''
#Problem 2:
def list_to_str(lis):
    temp = "["
    for j in range(len(lis)):
        temp = temp + str(lis[j])
        if (j != len(lis) - 1):
            temp = temp + ", "
    temp = temp + "]"
    return temp
'''
'''
#Problem 3:
def lists_are_the_same(list1, list2):
    if (len(list1) != len(list2)):
        return False
    for a in range(len(list1)):
        if (list1[a] != list2[a]):
            return False
    return True
'''
#Problem 4:
def find_GCD(x, y):
    if (x==y):
        return x
    if (x > y):
        i = y
        while (i > 0):
            if ((x % i) == 0) and ((y % i) == 0):
                return i
            else:
                i -= 1
    if (y > x):
        j = x
        while (j > 0):
            if ((y % j) == 0) and ((x % j) == 0):
                return j
            else:
                j -= 1
def simplify_fraction(n, m):
    GCD = find_GCD(n, m)
    new_n = n / GCD
    new_n = int(new_n)
    new_n = str(new_n)
    new_m = m / GCD
    new_m = int(new_m)
    new_m = str(new_m)
    output_str = new_n + "/" + new_m
    return output_str
'''
#Problem 5:
'''
'''
#Problem 6:
def euclid(a, b):
    x = min(a, b)
    y = max(a, b)
    if (x != 0):
        return(euclid(x, y%x))
    else:
        return y
'''
