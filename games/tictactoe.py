# --------Global Variables---------

# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#game still going
game_still_going = True

#who won or tie
winner = None

current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a REAL position from 1-9: ")

    #from str to int to index position on board
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there! Choose again simpleton!")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_win()
    check_if_tie()


def check_for_win():
    #set up global variable within definition
    global winner
    #check rows
    row_win = check_rows()

    #check columns
    col_win = check_columns()

    #check diagonals
    diag_win = check_diag()

    if row_win:
        winner = row_win
    elif col_win:
        winner = col_win
    elif diag_win:
        winner = diag_win
    else:
        winner = None
    return


def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
        #return winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_going = False
        #return winner X or O
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diag():
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    if diag_1 or diag_2:
        game_still_going = False

    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def play_game():
    #display initial board
    display_board()
    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        switch_player()

    #game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!!")
    elif winner == None:
        print("Tie.")


def switch_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()
