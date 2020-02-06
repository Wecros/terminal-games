def print_start_message():
    print("Welcome to the tic-tac-toe game.")
    print("Please enter coordinates to place your token.")
    print("=============================================")


def init_game_board():
    game_board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    return game_board


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


def is_win(board, v):
    for y in range(3):
        for x in range(3):
            if ((board[y%3][x%3] == v and board[y%3][(x+1)%3] == v and board[y%3][(x+2)%3] == v) or
                (board[y%3][x%3] == v and board[(y+1)%3][x%3] == v and board[(y+2)%3][x%3] == v) or
                (board[y%3][x%3] == v and board[(y+1)%3][(x+1)%3] == v and board[(y+2)%3][(x+2)%3] == v
                    and y == 0 and x == 0) or
                (board[y%3][x%3] == v and board[(y+1)%3][(x-1)%3] == v and board[(y+2)%3][(x-2)%3] == v
                    and y == 0 and x == 2)):
                return True
    return False


def is_game_finished(game_board):
    full_board = False
    x_win = False
    y_win = False

    if any(0 in line for line in game_board):
        full_board = False
    if (is_win(game_board, 1)):
        x_win = True
    elif (is_win(game_board, 2)):
        y_win = True

    if (x_win):
        print("Player with crosses won!")
    elif (y_win):
        print("Player with circles won!")
    elif full_board:
        print("The board is full! It's a draw.")

    if (x_win or y_win or full_board):
        return True
    return False


def is_input_right(input):
    if input == "1" or input == "2" or input == "3":
        return True
    return False


def loop(game_board):
    turn = 1
    while (True):
        X_input = input("Please enter the X coordinate (1-3): ")
        Y_input = input("Please enter the Y coordinate (1-3): ")
        if (not is_input_right(X_input) or not is_input_right(Y_input)):
            print("Wrong input!")
            continue
        
        X_coord = int(X_input) - 1
        Y_coord = int(Y_input) - 1

        if (game_board[Y_coord][X_coord] != 0):
            print("Invalid position!")
            continue

        if (turn % 2):
            game_board[Y_coord][X_coord] = 1
        else:
            game_board[Y_coord][X_coord] = 2
        
        print_game_board(game_board)
        turn += 1

        if (is_game_finished(game_board)):
            break

    choice_made = False
    while (not choice_made):
        choice = input("Do you want to play again [y/N]: ")
        if (choice.lower() == 'y'):
            game_board = init_game_board()
            loop(game_board)
            choice_made = True
        elif (choice.lower() == 'n'):
            choice_made = True


def game():
    print_start_message()
    game_board = init_game_board()
    print_game_board(game_board)
    loop(game_board)


game()
