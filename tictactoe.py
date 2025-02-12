import time
chart = [["    |      |  "], ["____|______|____"], ["    |      |  "], ["    |      |  "], ["____|______|____"], ["    |      |  "], ["    |      |  "]]

def board_create():
    for row in chart:
        print(row[0])

def start():
    print("""
          WELCOME TO TIC TAC TOE""")
    time.sleep(1)
    print("          Select Game Mode:")
    print("          1. PLAYER VS PLAYER")
    print("          2. PLAYER VS COMPUTER")
    
    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            print("You selected PLAYER VS PLAYER mode.")
            return "PVP"
        elif choice == "2":
            print("You selected PLAYER VS COMPUTER mode.")
            return "PVC"
        else:
            print("Invalid choice. Please enter 1 or 2.")

def game_loop(mode):
    if mode == "PVP":
        print("Starting PLAYER VS PLAYER mode...")
        pvp()
    elif mode == "PVC":
        print("Starting PLAYER VS COMPUTER mode...")
        pvc()

def pvp():
    print("gyattgyattgyattgyattgyattgyatt")

def pvc():
    print("rizzrizzrizzrizzrizzrizzrizzrizz")

def game_main():
    mode = start()
    game_loop(mode)
    time.sleep(1)
    board_create()

game_main()
