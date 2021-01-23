import random
def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
board = make_empty_board()
import random
#Problem 1a:
def get_coord(square_num):
    coord = []
    row =  (square_num - 1) // 3
    coord.append(row)
    column = (square_num - 1) % 3
    coord.append(column)
    return coord
#Problem 1b:
def put_in_board(board, mark, square_num):
    temp = get_coord(square_num)
    board[temp[0]][temp[1]] = mark
#Problem 1c:
'''
count = 0
finish = False
while finish == False:
    if count % 2 == 0:
        input_num = int(input("Give the number of the square where you wanna place X"))
        put_in_board(board, "X", input_num)
        print_board_and_legend(board)
    if count % 2 == 1:
        input_num = int(input("Give the number of the square where you wanna place O"))
        put_in_board(board, "O", input_num)
        print_board_and_legend(board)
    count += 1
    is_finish = input("Should the game be finished?")
    if is_finish == "Yes":
        finish = True
'''
#Problem 2a:
def get_free_squares(board):
    free_squares_list = []
    for i in range(0, len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] == " ":
                temp_list = []
                temp_list.append(i)
                temp_list.append(j)
                free_squares_list.append(temp_list)
    return free_squares_list
#Problem 2b:
def make_random_move(board, mark):
    temp_1 = get_free_squares(board)
    rand_index = random.randint(0, len(temp_1)-1)
    rand_coord = temp_1[rand_index]
    board[rand_coord[0]][rand_coord[1]] = mark
#Problem 2c:
'''
finish = False
count = 0
while finish == False:
    if count % 2 == 0:
        make_random_move(board, "X")
        print_board_and_legend(board)
    if count % 2 == 1:
        input_num = int(input("Give the number of the square where you wanna place O"))
        put_in_board(board, "O", input_num)
        print_board_and_legend(board)
    count += 1
    is_finish = input("Should the game be finished?")
    if is_finish == "Yes":
        finish = True
'''
#Problem 3a:
def is_row_all_marks(board, row_i, mark):
    temp_1 = [mark for j in range(3)]
    if board[row_i] == temp_1:
        return True
    else:
        return False
#Problem 3b:
def is_col_all_marks(board, col_i, mark):
    for k in range(len(board)):
        if board[k][col_i] != mark:
            return False
    return True
#helper function hard coded to see if one of the 2 diagonals is all the same mark:
def is_diag_all_marks(board, mark):
    if (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or (board[2][0] == mark and board[1][1] == mark and board[0][2] == mark):
        return True
    else:
        return False
#Problem 3c:
def is_win(board, mark):
    for a in range(3):
        if is_row_all_marks(board, a, mark) == True:
            return True
    for b in range(3):
        if is_col_all_marks(board, b, mark) == True:
            return True
    if is_diag_all_marks(board, mark) == True:
        return True
    return False
#Problem 3d:
'''
finish = False
count = 0
while finish == False:
    if count % 2 == 0:
        make_random_move(board, "X")
        print_board_and_legend(board)
    if count % 2 == 1:
        input_num = int(input("Give the number of the square where you wanna place O"))
        put_in_board(board, "O", input_num)
    count += 1
    if is_win(board, "X") == True:
        print ("The computer has won!")
        finish = True
    if is_win(board, "O") == True:
        print ("You've won!")
        finish = True
'''
#Problem 4a:
def win_move(board):
    new_board = [] 
    for a in range(len(board)): # deep copy
        row = []           
        for b in range(len(board[0])):
            row.append(board[a][b])
        new_board.append(row)
    temp_2 = get_free_squares(board)
    for c in range(len(temp_2)):
        new_board[temp_2[c][0]][temp_2[c][1]] = "X"
        if is_win(new_board, "X") == True:
            return temp_2[c]  #will return the coordinates of the position
#only returns a winning move if there is one, otherwise returns nothing
#Problem 4b (implementing 4a):
finish = False
count = 0
while finish == False:
    if count % 2 == 0:
        if win_move(board) != None:
            coordinate = win_move(board)
            board[coordinate[0]][coordinate[1]] = "X"
        else:
            make_random_move(board, "X")
        print_board_and_legend(board)
    if count % 2 == 1:
        input_num = int(input("Give the number of the square where you wanna place O"))
        put_in_board(board, "O", input_num)
    count += 1
    if is_win(board, "X") == True:
        print ("The computer has won!")
        finish = True
    if is_win(board, "O") == True:
        print ("You've won!")
        finish = True