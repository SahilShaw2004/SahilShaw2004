import json
import re

# Chess symbols dictionary
symbols = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙",
    " ": " "
}

# Load game.json
with open("game.json", "r") as f:
    game = json.load(f)

board = game["board"]
turn = game["turn"]

# Format board into a string
header = "    A   B   C   D   E   F   G   H\n"
divider = "  +---+---+---+---+---+---+---+---+\n"
rows = ""
for i, row in enumerate(board):
    rows += f"{8 - i} | " + " | ".join([symbols[sq] for sq in row]) + " |\n"
formatted_board = header + divider + rows + divider

# Create new chess section content
new_section = f"""<!-- CHESS_BOARD_START -->
**Current Turn:** `{turn.capitalize()}`

## ♟️ Current Board:

```text
{formatted_board}
