import time
import random

def board_create():
    chart = [
    ["1 ","2 ","3 "],
    ["4 ","5 ","6 "],
    ["7 ","8 ","9 "]
]
    print(*chart[0])
    print(*chart[1])
    print(*chart[2])
    return chart

def print_board(board):
    for row in board:
        print(*row)

def start():
    print("""
          WELCOME TO TIC TAC TOE""")
    time.sleep(1)

def game_loop(board):
    print("You are X and the enemy is O")
    playdecision = int(input("Where would you like to place your piece:  "))
    playdecision = str(playdecision)+" "
    for i in range(len(board)):
        try:
            col = board[i].index(playdecision)
            row = i
        except ValueError:
            pass
    
    board[row][col] = "X "

def game_main():
    start()
    time.sleep(1)
    board = board_create()
    game_loop(board)
    print(*board[0])
    print(*board[1])
    print(*board[2])
    comp_rand(board)
    print("Computer is choosing")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print(*board[0])
    print(*board[1])
    print(*board[2])
    return board

def comp_rand(board):
    comp_choice1 = random.randint(0,2)
    if board[comp_choice1] == "X" or "O":
        comp_choice1 = random.randint(0,2)

    for j in range(len(board)):
        try:
            col = board[j].index(comp_choice1)
            row = j
            board[row][col] = "O "
        except ValueError:
            pass
    
game_main()