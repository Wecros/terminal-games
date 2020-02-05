CROSS_CHAR = "X"
CIRCLE_CHAR = "O"


def print_start_message():
    print("Welcome to the tic tac toe game.")
    print("Please enter coordinates to place your token.")
    print("======")
    print("X O X")
    print("O X X")
    print("X O X")
    print("======")

def init_game_board():
    game_board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    return game_board

def reset_game_board(game_board):
    game_board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def print_game_board(game_board):
    char_count = 0
    for line in game_board:
        for char in line:
            if char_count % 3 != 0:
                print(" ", end='')
            if char == 0:
                print("-", end='')
            elif char == 1:
                print(CROSS_CHAR, end='')
            elif char == 2:
                print(CIRCLE_CHAR, end='')
            char_count += 1
        print("")

def is_game_finished(game_board):
    full_board = False
    if any(0 in line for line in game_board):
        full_board = False
    else:
        full_board = True

    if full_board:
        print("The board is full! The game's a draw.")
        return True

    return False


def game():
    print_start_message()
    game_board = init_game_board()
    turn = 1

    while (True):
        X_coord = int(input("Please enter the X coordinate (1-3): ")) - 1
        Y_coord = int(input("Please enter the Y coordinate (1-3): ")) - 1
        
        if (turn % 2):
            game_board[Y_coord][X_coord] = 1
        else:
            game_board[Y_coord][X_coord] = 2
        
        print_game_board(game_board)
        turn += 1

        if (is_game_finished(game_board)):
            break
    print("The game is over!")

    
game()