# tictactoe.py

class TicTacToe:
    def __init__(self):
        """Initialize the game board and the current player."""
        self.board = [" " for _ in range(9)]  # 3x3 board represented as a list
        self.current_player = "X"

    def display_board(self):
        """Display the current state of the game board."""
        print("\n")
        for row in range(3):
            print(" | ".join(self.board[row * 3:(row + 1) * 3]))
            if row < 2:
                print("-" * 9)
        print("\n")

    def make_move(self, position):
        """
        Make a move on the board.
        
        :param position: Position (0-8) where the player wants to place their mark.
        :return: True if the move is valid, False otherwise.
        """
        if 0 <= position < 9 and self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        """
        Check for a winner or a draw.
        
        :return: "X", "O", "Draw", or None if the game is still ongoing.
        """
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]

        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] 
                    and self.board[combo[0]] != " "):
                return self.board[combo[0]]

        if " " not in self.board:
            return "Draw"
        return None

    def switch_player(self):
        """Switch the current player."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        """Reset the game board and start with player X."""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
