import numpy as np

ROWS = 6
COLUMNS = 7
EMPTY_SLOT = ' '

def create_board():
    return np.full((ROWS, COLUMNS), EMPTY_SLOT, dtype=str)

def print_board(board):
    print(np.flip(board, 0))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROWS-1][col] == EMPTY_SLOT

def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == EMPTY_SLOT:
            return r

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(COLUMNS):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMNS-3):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMNS-3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

def main():
    board = create_board()
    print_board(board)
    turn = 0
    game_over = False

    while not game_over:
        # Player 1 input
        if turn % 2 == 0:
            col = int(input("Player 1, choose a column (0-6): "))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 'X')

                if winning_move(board, 'X'):
                    print("Player 1 wins!")
                    game_over = True

        # Player 2 input
        else:
            col = int(input("Player 2, choose a column (0-6): "))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 'O')

                if winning_move(board, 'O'):
                    print("Player 2 wins!")
                    game_over = True

        print_board(board)
        turn += 1

        if turn == ROWS * COLUMNS:
            print("It's a tie!")
            game_over = True

if __name__ == "__main__":
    main()
