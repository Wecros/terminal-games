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
    for line in game_board:
        print(line)

def game():
    print_start_message()
    game_board = init_game_board()

    while (True):
        X_coord = int(input("Please enter the X coordinate (1-3): ")) - 1
        Y_coord = int(input("Please enter the Y coordinate (1-3): ")) - 1
        
        game_board[Y_coord][X_coord] = 1

        print_game_board(game_board)
        


game()