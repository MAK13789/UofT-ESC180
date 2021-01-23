'''
#Problem 1a:
def halloween_reaction(thing):
    if thing in ["ghost", "monster", "midterm"]:
        return "NOO!"
    else:
        return "YAY!"
print (halloween_reaction("ghost"))
print (halloween_reaction("candy"))


#Problem 1b:
def print_mid_part(L):
    temp = len(L) - 1
    del L[temp]
    del L[0]
    print (L)
print_mid_part(["pumpkins", "candy", "costumes", "autumn", "zombies"])


#Problem 1c:
def h(L):
    L[0] = "fall"
    L[1] = "colours"
L = ["tricks", "treats"]
h(L)
print (L)


#Problem 1d:
#not applicable


#Problem 2a:
def odds_sum(L):
    count = 0
    for i in range(len(L)):
        if (L[i] % 2 == 1):
            count += L[i]
    return count
print (odds_sum([1,3,4,5]))


#Problem 2b:
i = 5
while (i < 500):
    print (i)
    i += 3



#Problem 3a:
def kids_who_like_candy(faves, kids):
    output = []
    for i in range(len(faves)):
        if faves[i] == "candy":
            output.append(kids[i])
    return output
print (kids_who_like_candy(["candy", "costumes", "weather", "candy"],  ["Bob", "Dorothy", "Mike", "Alice"]))



#Problem 3b:
def cube_root(n):
    for i in range(n):
        if (i * i * i) == n:
            return i
print (cube_root(13824))



count = 0
#Problem 4:
def halloween_surpise():
    global count
    if (count == 0):
        count += 1
        return 3
    if (count == 1):
        count += 1
        return 2
    if (count == 2):
        count += 1
        return 1
    if (count == 3):
        return "SURPRISE!"
print (halloween_surpise())
print (halloween_surpise())
print (halloween_surpise())
print (halloween_surpise())



#Problem 5:
#skip


#problem 6:
def has_single_peak(L):
    peak = 0
    for i in range(len(L)):
        if L[i] >= max(L):
            peak += 1
    if (peak == 1):
       return True
print (has_single_peak([1, 2, 2, 3, 4, 5, 0, -1]))
'''


#Problem 7:
def max_arrivals_2hrs(arrivals):
    count_list = []
    for i in range(len(arrivals) - 1): #should be 2 maybe
        j = i + 1
        temp = arrivals[i:j]
        while (temp[len(temp) - 1] - temp[0]) < 120:
            j += 1
        count_list.append((j - 1) - i)
    return max(count_list)
print (max_arrivals_2hrs([0, 30, 40, 150, 160, 170, 370]))
            

