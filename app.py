'''
_1|2_|3_
_4|_5|_6
7 | 8|9


IMPORT
random
datetime
time
os
'''


# from datetime import datetime
# print(datetime.now())


import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    return time_sec

def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_winner(board, player):
    if(board[0] == player and board[1] == player and board[2] == player) or \
        (board[3] == player and board[4] == player and board[5] == player) or \
        (board[6] == player and board[7] == player and board[8] == player) or\
        (board[0] == player and board[3] == player and board[6] == player) or\
        (board[1] == player and board[4] == player and board[7] == player) or\
        (board[2] == player and board[5] == player and board[8] == player) or\
        (board[0] == player and board[4] == player and board[8] == player) or\
        (board[2] == player and board[4] == player and board[6] == player):
            return True
    else:
        False

def GAME():
    board = ['1', '2','3', '4', '5', '6', '7', '8', '9']
    player = 'X'
    print_board(board)

    while True:
        
        print(f"it's {player} 's turn.")
        # while countdown(5) != 0:
        choice = input(f"Choose a cell to place your {player} (1-9):  ") 
        if board[int(choice)-1] != 'X' and board[int(choice)-1] != 'O': 
            board[int(choice)-1] = player 
            print_board(board)
            if check_winner(board, player):
                print(f'\n{player} WINS \n')
                break

            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print("\nThat cell is already taken! Choose another Cel\n")
    
        # if player == 'X':
        #         player = 'O'
        # else:
        #         player = 'X'
        


GAME()
    