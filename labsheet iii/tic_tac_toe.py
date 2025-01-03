class TicTacToe:
    def __init__(self):
        # Initialize the 3x3 board and players
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.turns = 0  # Track the number of turns

    def print_board(self):
        # Print the current state of the board
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def check_winner(self, player):
        # Check rows and columns for a win
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        # Check diagonals for a win
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def play(self):
        while self.turns < 9:
            self.print_board()
            current_player = self.players[self.turns % 2]
            print(f"Player {current_player}'s turn.")
            try:
                # Get the player's move
                row, col = map(int, input("Enter row and column (0-2): ").split())
                if self.board[row][col] != " ":
                    print("Cell already taken! Try again.")
                    continue
                # Mark the cell with the player's symbol
                self.board[row][col] = current_player
                self.turns += 1
                # Check if the current player has won
                if self.check_winner(current_player):
                    self.print_board()
                    print(f"Player {current_player} wins!")
                    return
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid row and column numbers (0-2).")
        # If no winner, declare a draw
        self.print_board()
        print("It's a draw!")

# Example usage
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
