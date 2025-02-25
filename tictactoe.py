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

    while True:
        # Player move
        playdecision = input("Where would you like to place your piece? ") + " "
        
        for row in board:
            if playdecision in row:
                row[row.index(playdecision)] = "X "
                break

        print_board(board)

        # Computer move
        print("Computer is choosing...")
        time.sleep(1)
        comp_rand(board)
        print_board(board)


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
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        
        if board[row][col] not in ["X ", "O "]:
            board[row][col] = "O "
            break

    
game_main()