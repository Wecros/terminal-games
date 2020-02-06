def print_start_message():
    print("Welcome to the tic tac toe game.")
    print("Please enter coordinates to place your token.")
    print("================================")


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
        for cell in line:
            if char_count % 3 != 0:
                print(" ", end='')
            if cell == 0:
                print("-", end='')
            elif cell == 1:
                print("X", end='')
            elif cell == 2:
                print("O", end='')
            char_count += 1
        print("")


def is_game_finished(game_board):
    full_board = False
    x_win = False
    y_win = False

    if any(0 in line for line in game_board):
        full_board = False
    else:
        full_board = True

    for y in range(3):
        for x in range(3):
            if ((game_board[y%3][x%3] == 1 and game_board[y%3][(x+1)%3] == 1 and game_board[y%3][(x+2)%3] == 1) or
                (game_board[y%3][x%3] == 1 and game_board[(y+1)%3][x%3] == 1 and game_board[(y+2)%3][x%3] == 1) or
                (game_board[y%3][x%3] == 1 and game_board[(y+1)%3][(x+1)%3] == 1 and game_board[(y+2)%3][(x+2)%3] == 1) or
                (game_board[(y)%3][(x+2)%3] == 1 and game_board[(y+1)%3][(x+1)%3] == 1 and game_board[y%3][x%3] == 1)):
                x_win = True
                break
            elif ((game_board[y%3][x%3] == 2 and game_board[y%3][(x+1)%3] == 2 and game_board[y%3][(x+2)%3] == 2) or
                (game_board[y%3][x%3] == 2 and game_board[(y+1)%3][x%3] == 2 and game_board[(y+2)%3][x%3] == 2) or
                (game_board[y%3][x%3] == 2 and game_board[(y+1)%3][(x+1)%3] == 2 and game_board[(y+2)%3][(x+2)%3] == 2) or
                (game_board[(y+2)%3][(x+2)%3] == 2 and game_board[(y+1)%3][(x+1)%3] == 2 and game_board[y%3][x%3] == 2)):
                y_win = True
                break
        if x_win or y_win:
            break

    if (x_win):
        print("Player with crosses won.")
    elif (y_win):
        print("Player with circles won.")
    elif full_board:
        print("The board is full! The game's a draw.")

    if (x_win or y_win or full_board):
        return True
    return False


def is_input_right(input):
    if input == "1" or input == "2" or input == "3":
        return True
    return False


def loop(game_board, turn):
    while (True):
        X_coord = input("Please enter the X coordinate (1-3): ")
        Y_coord = input("Please enter the Y coordinate (1-3): ")

        if (not is_input_right(X_coord) or not is_input_right(Y_coord)):
            print("Wrong input!")
            continue
        
        X_coord = int(X_coord) - 1
        Y_coord = int(Y_coord) - 1

        if (game_board[Y_coord][X_coord] != 0):
            print("Wrong input!")
            continue
            

        if (turn % 2):
            game_board[Y_coord][X_coord] = 1
        else:
            game_board[Y_coord][X_coord] = 2
        
        print_game_board(game_board)
        turn += 1

        if (is_game_finished(game_board)):
            break


def game():
    print_start_message()
    game_board = init_game_board()
    turn = 1

    loop(game_board, turn)

    print("The game is over!")
    choice = input("Do you want to play again [y/N]? ")
    if (choice.lower() == 'y'):
        game_board = init_game_board()
        loop(game_board, turn)
    else:
        pass
    
    
game()