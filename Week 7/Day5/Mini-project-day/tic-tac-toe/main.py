def display_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def player_input(player):
    position = input(f"Player {player}, enter your position (1-9): ")
    while not position.isdigit() or int(position) < 1 or int(position) > 9:
        position = input("Invalid input. Enter a number between 1 and 9: ")
    return int(position) - 1

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3)):
            return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        display_board(board)
        current_player = players[turn % 2]
        position = player_input(current_player)

        row, col = divmod(position, 3)

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_board_full(board):
                display_board(board)
                print("It's a tie!")
                break

            turn += 1
        else:
            print("Position already occupied. Try again.")

if __name__ == "__main__":
    play()
