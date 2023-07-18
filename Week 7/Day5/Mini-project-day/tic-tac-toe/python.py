board = [" "] * 9
current_player = "X"


def display_board():
    """Display the Tic Tac Toe board."""
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")


def player_input(player):
    """Get the position from the player and update the board."""
    position = int(input("Player " + player + ", enter your move (1-9): ")) - 1

    if position < 0 or position >= 9 or board[position] != " ":
        print("Invalid move! Try again.")
        player_input(player)
    else:
        board[position] = player


def check_win():
    """Check if there is a winner or a tie."""
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return True

    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return True

    if board[0] == board[4] == board[8] != " " or board[2] == board[4] == board[6] != " ":
        return True

    if " " not in board:
        return "Tie"

    return False


def play():
    """The main function that calls other functions to play the game."""
    display_board()

    while True:
        player_input(current_player)
        display_board()

        if check_win() == True:
            print("Player", current_player, "wins!")
            break
        elif check_win() == "Tie":
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


play()