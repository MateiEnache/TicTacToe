import time
import random

def board_create():
    chart = [
        ["1 ", "2 ", "3 "],
        ["4 ", "5 ", "6 "],
        ["7 ", "8 ", "9 "],
    ]
    print_board(chart)
    return chart

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def start():
    print("WELCOME TO TIC-TAC-TOE")
    time.sleep(1)

def game_loop(board):
    print("You are X and the enemy is O")
    
    while True:
        playdecision = input("Where would you like to place your piece? ") + " "
        
        move_made = False
        for row in board:
            if playdecision in row:
                row[row.index(playdecision)] = "X "
                move_made = True
                break
        
        if not move_made:
            print("Invalid move, try again.")
            continue
        
        print_board(board)
        
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            return
        
        if check_draw(board):
            print("It's a draw!")
            return

        print("Computer is choosing...")
        time.sleep(1)
        comp_rand(board)
        print_board(board)
        
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            return
        
        if check_draw(board):
            print("It's a draw!")
            return

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] in ["X ", "O "]:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] in ["X ", "O "]:
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ["X ", "O "]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ["X ", "O "]:
        return board[0][2]
    
    return None

def check_draw(board):
    for row in board:
        for cell in row:
            if cell not in ["X ", "O "]:
                return False
    return True

def comp_rand(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        
        if board[row][col] not in ["X ", "O "]:
            board[row][col] = "O "
            break

def game_main():
    while True:
        start()
        time.sleep(1)
        board = board_create()
        game_loop(board)
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

game_main()
