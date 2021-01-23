#Problem 1a:
def wish_happy_holiday(holiday_name):
    output = "Happy " + holiday_name + "!"
    return output
print(wish_happy_holiday("midterm"))

#Problem 1b:
def print_first_half(L):
    temp = int(len(L) / 2)
    return print((L[:temp]))
print_first_half(["pumpkins", "candy", "costumes", "autumn"])


#Problem 1c:
def h():
    global trick
    trick = "trick"
    return "treat"
trick = "midterm"
treat ="exam"
treat = h()
print (trick + " or " + treat)


#Problem 1d:
#N/A


#Problem 2a:
def count_engineers(costumes):
    count = 0
    for i in range(len(costumes)):
        if (costumes[i] == "engineer"):
            count += 1
    return print(count)
count_engineers(["engineer", "doctor", "firefighter", "engineer", "pirate", "artsie"])


#Problem 2b:
for i in range(2, 272483):
    if (272483 % i == 0):
        print (i)
        break


#Problem 2c:
def switch_columns(M, i, j):
    for k in range(len(M)):
        temp_1 = M[k][i]
        temp_2 = M[k][j]
        M[k][j] = temp_1
        M[k][i] = temp_2


M = [[5, 6, 7],
[0, -3, 5]]
switch_columns(M, 0, 1)
print(M)





#Problem 3a:
#N/A


#Problem 4:
def is_symmetric(L):
    return (L == list(reversed(L)))




#Problem 5:
def is_almost_symmetric(L):
    for i in range(len(L)):
        for j in range(len(L)):
            temp_1 = L[i]
            temp_2 = L[j]
            new_list = L[:]
            new_list[j] = temp_1
            new_list[i] = temp_2
            if is_symmetric(new_list) == True:
                return True
    return False
L = [1, 2, 1, 2]
print (is_almost_symmetric(L))


