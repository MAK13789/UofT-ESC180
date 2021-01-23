#Question 1a:
def is_sorted(L):
    if len(L) == 0 or len(L) == 1 or len(L) == 2:
        return True
    else:
        if L[len(L)-1] >= L[0]:
            if sorted(L) == L:
                return True
        else:
            temp = reversed(L)
            if sorted(temp) == temp:
                return True
        return False
#Question 1b:
'''
O(nlogn)
'''
#Question 2:
def euc_distance(u, v):
    inner_sum = 0
    for i in list(u.keys()):
        if i in list(v.keys()):
            diff = u[i] = v[i]
            inner_sum += diff ** 2
        else:
            diff = u[i]
    return inner_sum ** 0.5
u = {1:4, 2:5, 4:10}
v = {1:5, 2:4, 3:10, 4:20}
print (euc_distance(u, v))
#Question 3:
def movies_by_release_date(movies):
    release_dates = {}
    for movie in list(movies.keys()):
        if movies[movie][0] == "a":
            release_dates[movie] = 0 
        else:
            release_dates[movie] = int(movies[movie][:4])
    temp = list(reversed(sorted(release_dates, key = release_dates.get)))
    return temp
#Question 4:
def merge(L1, L2):
    if len(L2) == 0:
        return L1
    if L2[len(L2)-1] <= L1[0]:
        return L2 + L1
    if L2[0] >= L1[len(L1)-1]:
        return L1 + L2
    if L2[0] <= L1[0]:
        return merge([L2[0]] + L1, L2[1:])
    elif L2[0] > L1[0]:
        temp_1 = L1[0]
        del L1[0]
        return [temp_1] + merge(L1, L2)
print (merge([4, 8, 10], [2, 5]))
#Question 5:
'''
Not appplicable
'''
#Question 6:
'''
O(n) in the worst case, where L[i] > 0 for all i

inner for loop is O(1) and outer for loops is O(n), so overall it is O(n)

in the worst case it i and j decrease by 1 each time, so O(n^2) overall
'''
#Question 7:
'''
for each row, the worst case is O(n^2), making the overall O(m*n^2) 
'''
#Question 9:
def is_any_empty(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return True
    return False
def x_can_win(board):
    if x_won(board) == True:
        return True
    else:
        if is_any_empty(board) == False:
            return False
        else:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        new_board = board[:]
                        new_board[i][j] = "X"
                        if x_won(new_board) == True:
                            return True
                        else:
                            if is_any_empty(board) == False:
                                return False
                            else:
                                for a in range(3):
                                    for b in range(3):
                                        if board[a][b] == " ":
                                            newer_board = new_board[:]
                                            newer_board[a][b] = "O"
                                            if is_any_empty(board) == False:
                                                return False
                                            else:
                                                for c in range(3):
                                                    for d in range(3):
                                                        if newer_board[c][d] == " "
                                                            newest_board = newer_board[:]
                                                            newest_board[c][d] = "X"
                                                            if x_won(newest_board) == True:
                                                                return True
                                                            else:
                                                                if is_any_empty(board) == False:
                                                                    return False
                                                                else:
                                                                    for e in range(3):
                                                                        for f in range(3):
                                                                            if newest_board[e][f] == " "
                                                                            

                    
