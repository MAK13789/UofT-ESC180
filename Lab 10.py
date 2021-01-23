#Problem 1:
def power(x, n):
    if n == 0:
        return 1
    if n > 0:
        return x * power(x, n-1)
print (power(5, 5))
#Problem 2:
def interleave(L1, L2):
    length = len(L1)
    if length == 0:
        return []
    else: 
        return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])

test_1 = [1,2,3,4,5]
test_2 = [1,2,3,4,5]
print (interleave(test_1, test_2))

#Problem 3:
def reverse_rec(L):
    if len(L) == 0:
        return []
    else:
        return [L[len(L) - 1]] + reverse_rec(L[:len(L) - 1])
print (reverse_rec([1,2,3,4,5,6,7,8,9,10]))
#Problem 4:
def print_pattern(L):
    if(len(L)):
        print(L[int(len(L) / 2 - 0.5)])
        del L[int(len(L) / 2 - 0.5)]
        print_pattern(L)
print_pattern([1,2,3,4,5])
#Problem 5 (old version, only parantheses):
'''
def is_balanced(s):   
    if len(s) == 0:
        return True
    #checking for first time run:
    if type(s) == type('string'):    #because later times a list will be input
        if s[0] == ')' or s[len(s) - 1] == '(':
            return False
        new = list(s)
    else:
        #s is a list here
        new = s[:]
        s = ''.join(s)       
    if s[0] == '(':
        if s.find(')') == -1:       
            return False
        else:
            del new[s.find(')')]               
            del new[0]
            return is_balanced(new)
    if s[0] == ')':
        return False
print (is_balanced("(()(())"))
'''
def check(temp_1):        #helper function to check ending conidtion for remove_extra, checks if only parantheses
    if len(temp_1) == 0:
        return True
    if temp_1[0] != '(' and temp_1[0] != ')' and temp_1[0] != '{':
        return False
    else:
        return check(temp_1[1:])
def remove_extra(temp):
    if check(temp) == True:
        return temp
    if temp[0] != '(' and temp[0] != ')':
        return remove_extra(temp[1:])
    else:
        x = temp[0]
        if temp.find('{') == -1:
            temp = temp[1:] + '{'
            temp = temp + x
        else:
            temp = temp[1:] + x
        return remove_extra(temp)
def is_balanced(s):   
    if len(s) == 0:
        return True
    #checking for first time run:
    if type(s) == type('string'):    #because later times a list will be input
        s = remove_extra(s)
        temp_3 = s.find('{')
        if temp_3 != -1:
            s = s[temp_3 + 1:] + s[:temp_3]
        if s[0] == ')' or s[len(s) - 1] == '(':
            return False
        new = list(s)
    else:
        #s is a list here
        new = s[:]
        s = ''.join(s)       
    if s[0] == '(':
        if s.find(')') == -1:       
            return False
        else:
            del new[s.find(')')]               
            del new[0]
            return is_balanced(new)
    if s[0] == ')':
        return False
print (is_balanced("(well (I think), recursion works like that (as far as I know)"))