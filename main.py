# Tic Tac Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('---------')
    for i in range(3):
        row = '| '.join(board[i * 3:(i * 3) + 3])
        print('| ' + row + ' |')
        print('---------')

# Function to check for a win
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        print("Player", current_player, "turn.")

        move = input("Enter your move (1-9): ")

        if move.isdigit():
            move = int(move) - 1

            if 0 <= move < 9 and board[move] == ' ':
                board[move] = current_player

                if check_win(current_player):
                    print_board()
                    print("Player", current_player, "wins!")
                    game_over = True
                elif ' ' not in board:
                    print_board()
                    print("It's a tie!")
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move. Try again.")
        else:
            print("Invalid input. Try again.")

# Start the game
play_game()
