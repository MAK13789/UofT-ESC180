#Question 1a:
def insert(L, e):
    if len(L) == 0:
        return [e]
    if e <= L[0]:
        return [e] + L
    if e >= L[len(L) - 1]:
        return L + [e]
    else:
        for i in range(len(L)):
            if e <= L[i]:
                new_list = L[:i]
                new_list.append(e)
                new_list = new_list + L[i:]
                return new_list
#Question 1b:
'''
in the worst case scenario, a for loop is run for n iterations where n is the length of the list, and hence it is O(n)
'''
#Question 2:
def select_gifts(good_ratings, want_ratings):
    combined_dict = {}
    for j in list(good_ratings.keys()):
        combined_dict[j] = good_ratings[j]
    for k in list(want_ratings.keys()):
        if k not in list(combined_dict.keys()):
            combined_dict[k] = want_ratings[k]
        else:
            combined_dict[k] = combined_dict[k] + want_ratings[k]
    max_rating = max(list(combined_dict.values()))
    max_ratings = []
    for a in list(combined_dict.keys()):
        if combined_dict[a] == max_rating:
            max_ratings.append(a)
    max_ratings.sort()
    return max_ratings
#Question 3:
def transpose(M):
    output = []
    for b in range(len(M[0])):
        column = []
        for c in range(len(M)):
            column.append(M[c][b])
        output.append(column)
    return output
#Question 4:
def max_rec(L):
    if len(L) == 1:
        return L[0]
    else:
        if L[0] < L[1]:
            return max_rec(L[1:])
        elif L[0] >= L[1]:
            return max_rec([L[0]] + L[2:])
#Question 5:
def is_fib(L):
    if len(L) == 3:
        if L[0] == 1 and L[1] == 1 and L[2] == 2:
            return True
        else:
            return False
    elif len(L) == 2:
        if L[0] == 1 and L[1] == 1:
            return True
        else:
            return False
    elif len(L) == 1:
        if L[0] == 1:
            return True
        else:
            return False
    elif len(L) == 0:
        return True
    else:
        if (L[len(L)-1] == L[len(L)-3] + L[len(L)-2]):
            return is_fib(L[:len(L)-3])
        else:
            return False
#Question 6:
'''
Not applicable
'''
#Question 7:
'''
total calls: 1+1+2+2+3+3+4+4+...+(n//2)+(n//2)  ---> O(n^2)

while loop with j runs in O(n) in the first iteration of i, but doesn't
get executed in later iterations. while loop with i runs in O(n^3/n) = 
O(n^2) time and hence the overall complexity is O(n^2)

O(log_2(n))   WRONG!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

O(10k) time so just constant time AKA O(1)
'''
#Question 8a:
'''
Not applicable
'''
#Question 8b:
'''
O(n^2)
'''
#Question 9:
def sorted_timestamps(timestamps):
    times = {}
    for x in timestamps:
        if x[0] not in list(times.keys()):
            times[x[0]] = x[1]
        else:
            temp = []
            temp.append(times[x[0]])
            if x[1] >= temp[0]:
                temp.append(x[1])
            else:
                temp = [x[1]] + temp
            times[x[0]] = temp
    sorted_hours = sorted(list(times.keys()))
    final = []
    for y in sorted_hours:
        if type(times[y]) == type(1):
            final.append((y, times[y]))
        else:
            for z in times[y]:
                final.append((y, z)) 
    return final
#Question 10:
def max_clique(friends):
    cliques = []
    for h in list(friends.keys()):
        for q in friends[h]:
            for f in friends[q]:
                clique = []
                if f in friends[h]:
                    clique.append(h)
                    clique.append(q)
                    clique.append(f) 
                    cliques.append(clique)
    lengths = []
    for u in cliques:
        lengths.append(len(u))
    return cliques[lengths.index(max(lengths))]