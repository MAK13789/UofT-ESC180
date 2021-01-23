#Question 1:
def most_productive_elf(toys_produced):
   temp = sorted(toys_produced, key=toys_produced.get)
   return temp[len(temp)-1]
#Question 2a:
def two_smallest(L):
    smallest = min(L)
    L.remove(smallest)
    second_smallest = min(L)
    return [second_smallest, smallest]
#Question 2b:
'''
min has a runtime complexity of O(n), where n is the length of the list
as it loops through each element once, and this is called twice so the 
overall complexity is O(2n) which is just O(n)
'''
#Question 3:
def largest_col_sum(M):
    sums_list = []
    for i in range(len(M[0])):
        col_sum = 0
        for j in range(len(M)):
            col_sum += M[j][i]
        sums_list.append(col_sum)
    return max(sums_list)
M0 = [ [1, 2, 3, 4],  [5, 0, 5, 0], [6, 7, 8, 9]]
#Question 4:
'''
Not applicable
'''
#Question 5:
'''
in the worst case, item is alwawys > 0, and it has n calls so the 
runtime complexity is O(n)

inner loop is O(5), outer is O(n), so overall it is O(5n) which is just
O(n)

for loop with complexity O(k) is executed n times, so the overall complexity
is O(k*n)
'''
#Question 6:
def filter_out_odds(L):
    if len(L) == 0:
        return L
    else:
        if L[0] % 2 !=0:
            return filter_out_odds(L[1:])
        else:
            return [L[0]] + filter_out_odds(L[1:])



#Question 8:
def mult(expr):
    operator_indices = []
    operations = ['+', '-', '*']
    for b in range(len(expr)):
        if expr[b] in operations:
            operator_indices.append(b)
    for k in range(len(expr)):
        x = expr.find('*')
        if x == -1:
            break
        else:
            if operator_indices.index(x) != 0:
                temp_1 = operator_indices[operator_indices.index(x)-1]
            else:
                temp_1 = 0
            if operator_indices.index(x) != len(operator_indices)-1:
                temp_2 = operator_indices[operator_indices.index(x)+1]
            else:
                temp_2 = len(expr)
            if temp_1 != 0:
                num_1 = int(expr[temp_1+1:x])
            else:
                num_1 = int(expr[:x])
            num_2 = int(expr[x+1:temp_2])
            product = num_1 * num_2
            if temp_1 != 0 and temp_2 != 0:
                expr = expr[:temp_1+1] + str(product) + expr[temp_2:]
            elif temp_1 == 0 and temp_2 != 0:
                expr = str(product) + expr[temp_2:]
            elif temp_1 != 0 and temp_2 == 0:
                expr = expr[:temp_1+1] + str(product)
            elif temp_1 == 0 and temp_2 == 0:
                expr = str(product)
    return expr
def subtract(expr):
    operator_indices = []
    operations = ['+', '-', '*']
    for b in range(len(expr)):
        if expr[b] in operations:
            operator_indices.append(b)
    for k in range(len(expr)):
        x = expr.find('-')
        if x == -1:
            break
        else:
            print (expr)
            if operator_indices.index(x) != 0:
                temp_1 = operator_indices[operator_indices.index(x)-1]
            else:
                temp_1 = 0
            if operator_indices.index(x) != len(operator_indices)-1:
                temp_2 = operator_indices[operator_indices.index(x)+1]
            else:
                temp_2 = len(expr)
            if temp_1 != 0:
                num_1 = int(expr[temp_1+1:x])
            else:
                num_1 = int(expr[:x])
            num_2 = int(expr[x+1:temp_2])
            diff = num_1 - num_2
            if temp_1 != 0 and temp_2 != 0:
                expr = expr[:temp_1+1] + str(diff) + expr[temp_2:]
            elif temp_1 == 0 and temp_2 != 0:
                expr = str(diff) + expr[temp_2:]
            elif temp_1 != 0 and temp_2 == 0:
                expr = expr[:temp_1+1] + str(diff)
            elif temp_1 == 0 and temp_2 == 0:
                expr = str(diff)
    return expr




'''
def ev(expr):

    
    expr = mult(expr)
    return subtract(expr)
'''
expr = "14-3*2+3+3*4-20"
new = mult(expr)
print (new)
newer = subtract(new)
print (newer)



