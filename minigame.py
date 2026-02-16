import numpy as np

def create_bord():
    """initializes the 3*3 game board using a numpy array."""
   
    return np.zeros((3, 3), dtype=int)
def display_board(board):
    """prints the current state of the boart."""
    print("\n--- current board ---")
    
    symbols = {0: ' ', 1: 'X', 2: 'O'}
   
    for row in board:
        print(" | ".join(symbols[cell]for cell in row))
        print("-" * 9)
    print("--------------------\n")
def check_win(board, player):
    """checks if the given player (1 or 2) has won."""
    
    for row in board:
        if np.all(row == player):
            return True
    
    for col in board.T:
        if np.all(col == player):
            return True
    
    if np.all(np.diag(board) == player):
        return True
    
    if np.all(np.diag(np.fliplr(board))==player):
        return True
    return False
def check_draw(board):
    """checks if the board is full (a draw)."""
   
    return np.all(board != 0)
def is_valid_move(board, row, col):
    """checks if the chosen coordinates are
within bounds and the cell is empty."""
    if not(0 <= row < 3 and 0 <= col < 3):
        print("Invalidd coordinates. row and column must be 0, 1, or 2.")
        return False
    if board[row, col] != 0:
        print("That cell is already taken. try again.")
        return False
    return True

def play_game():
    """manages the flow of the Tic-Tac-Toe game."""
    board = create_bord()
    current_player = 1
    print("welcome to Tic-Tac-Toe !")
    print("player 1 is 'X',player 2 is 'O'.")

    while True:
        player_symbol = 'X' if current_player == 1 else 'O'
        display_board(board)
        print(f"player {current_player}({player_symbol})'s turn.")
        try:
           
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. please enter a number.")
            continue
        
        if is_valid_move(board, row, col):
            
            board[row, col] = current_player
           
            if check_win(board, current_player):
                display_board(board)
                print(f"player {current_player} ({player_symbol}) WINS! Congratulations!")
                break
            
            elif check_draw(board):
                display_board(board)
                print("It's a DRAW!")
                break
            
            current_player = 3 - current_player
if __name__ == "__main__":
    play_game()