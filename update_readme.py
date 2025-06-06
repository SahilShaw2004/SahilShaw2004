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

# Format board into markdown table string
header = "|   | A | B | C | D | E | F | G | H |\n"
divider = "|---|---|---|---|---|---|---|---|---|\n"
rows = ""
for i, row in enumerate(board):
    row_symbols = [symbols[sq] if sq in symbols else sq for sq in row]
    rows += f"| {8 - i} | " + " | ".join(row_symbols) + " |\n"

formatted_board = header + divider + rows

# Create new chess section content (no code block, just markdown)
new_section = f"""<!-- CHESS_BOARD_START -->
**Current Turn:** `{turn.capitalize()}`

## ♟️ Current Board:

{formatted_board}
<!-- CHESS_BOARD_END -->
"""

# Read README.md content
with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

# Replace content between markers with new_section
pattern = re.compile(r"<!-- CHESS_BOARD_START -->.*?<!-- CHESS_BOARD_END -->", re.DOTALL)
updated_readme = pattern.sub(new_section, readme_content)

# Write updated content back to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_readme)

print("README.md updated successfully.")
