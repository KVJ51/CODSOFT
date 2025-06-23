import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_moves_left(board):
    return any(cell == " " for row in board for cell in row)

def evaluate(board):
    # Check rows
    for row in board:
        if row.count("X") == 3:
            return -10
        elif row.count("O") == 3:
            return 10
    # Check columns
    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return -10
        elif all(board[row][col] == "O" for row in range(3)):
            return 10
    # Check diagonals
    if all(board[i][i] == "X" for i in range(3)):
        return -10
    elif all(board[i][i] == "O" for i in range(3)):
        return 10
    if all(board[i][2 - i] == "X" for i in range(3)):
        return -10
    elif all(board[i][2 - i] == "O" for i in range(3)):
        return 10
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!\nYou are X, AI is O")
    print_board(board)

    while True:
        # Player move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != " ":
            print("Invalid move, try again.")
            continue
        board[row][col] = "X"
        print_board(board)
        if evaluate(board) == -10:
            print("You win!")
            break
        if not is_moves_left(board):
            print("It's a tie!")
            break

        # AI move
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = "O"
        print("AI's move:")
        print_board(board)
        if evaluate(board) == 10:
            print("AI wins!")
            break
        if not is_moves_left(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
