from threading import Thread
import time
board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]
user = True #True-->user is 'x'  False-->user is 'o'
count=1 

def print_board(boardd):
    for i in range(3):
        for j in range(3):
            print(boardd[i][j] + " ", end="")
        print()
    #time.sleep(1)
    #print()

print("Welcome to Tic Tac Toe game!\nThis is your board:")
print_board(board)

def quit(user_input):
    if user_input.lower() == 'q':
        print("Thanks for playing")
        return True
    else:
        return False

def check_input(user_input):
    # to check if its a number
    if not isnum(user_input):
        return False
    else:
        if not int(user_input) in range(1, 10):
            print("Invalid digit entered,Please enter a digit between 1 to 9")
            return False

        else:
            #print_board(board)
            return True

def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else:
        return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]

    if board[row][col] != '_':
        print('This position is already taken')
        return True

    else:
        return False

def coordinates(array_input):
    row = int(array_input / 3)
    col = int(array_input % 3)

    return row, col

def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    sign = active_user
    if not istaken(coords, board):
        board[row][col] = sign
        print_board(board)

def current_user(user):
    if user :
        return 'x'
    else:
        return 'o'

def iswin(user, board):
    if check_row(user, board): return True
    elif check_col(user, board): return True
    elif check_diagonal(user, board): return True
    else: return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False

def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col :
            return True
    return False

def check_diagonal(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False


while count<=9:
    print()
    user_input = input("Please enter a position between 1 to 9 or enter 'q' to quit:")
    if quit(user_input):
        break
    if not check_input(user_input):
        continue

    array_input = int(user_input) - 1
    coords = coordinates(array_input)
    #board[0][0] = 'x'

    if istaken(coords, board):
        print('Plz try again')
        continue

    active_user = current_user(user)
    add_to_board(coords, board, active_user)

    if iswin(active_user, board):
        print(f"{active_user.upper()} won! Congratulations :)\n")
        break

    if count == 9:
        print("Match tied!\nWell played, both of you!\n")

    count += 1
    user = not user

