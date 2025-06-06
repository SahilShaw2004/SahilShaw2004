import json

# Define the chess piece symbols
symbols = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙",
    " ": " "
}

# Read the game state from game.json
with open("game.json", "r") as f:
    game = json.load(f)

board = game["board"]
turn = game["turn"]

# Build the chessboard grid with row/column labels
rows = ""
for i, row in enumerate(board):
    row_str = f"{8 - i} | " + " | ".join([symbols[sq] for sq in row]) + " |\n"
    rows += row_str

# Create the column header
header = "    A   B   C   D   E   F   G   H\n"
divider = "  +---+---+---+---+---+---+---+---+\n"
formatted_board = header + divider + rows.replace("|", "|") + divider

# Write it to README.md
with open("README.md", "w") as f:
    f.write(f"# ♟️ Sahil’s Community Chess Tournament\n\n")
    f.write(f"**Current Turn:** `{turn.capitalize()}`\n\n")
    f.write("## ♟️ Current Board:\n\n")
    f.write("```text\n")
    f.write(formatted_board)
    f.write("```\n")
    f.write("\nMake your move by editing `game.json` and submitting a PR!")
