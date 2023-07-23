import tkinter as tk
import random
import time
import sqlite3

# Configuration du jeu
CARD_WIDTH = 100
CARD_HEIGHT = 100
NUM_CARDS = 16
COLORS = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'cyan']
DB_FILE = 'memory_game.db'

# Initialise la base de données et crée la table pour les scores
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS scores (player_name TEXT, time_taken INTEGER)''')
conn.commit()

def generate_cards():
    cards = []
    for color in COLORS:
        cards.append(color)
        cards.append(color)
    random.shuffle(cards)
    return cards

def on_card_click(row, col):
    global flips, cards, card_buttons, grid, start_time

    if len(flips) < 2 and not grid[row][col]:
        card_buttons[row][col].config(bg=cards[row * NUM_ROWS + col])
        flips.append((row, col))
        grid[row][col] = True

        if len(flips) == 2:
            r1, c1 = flips[0]
            r2, c2 = flips[1]
            if cards[r1 * NUM_ROWS + c1] != cards[r2 * NUM_ROWS + c2]:
                time.sleep(1)
                card_buttons[r1][c1].config(bg='gray')
                card_buttons[r2][c2].config(bg='gray')
                grid[r1][c1] = False
                grid[r2][c2] = False
            flips.clear()

        if all(all(row) for row in grid):
            # Toutes les cartes ont été retournées, le jeu est terminé
            player_name = input("Bravo! Vous avez terminé le jeu. Entrez votre nom pour enregistrer votre score: ")
            time_taken = int(time.time() - start_time)
            cursor.execute("INSERT INTO scores VALUES (?, ?)", (player_name, time_taken))
            conn.commit()

def create_card_buttons():
    buttons = [[None for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            buttons[row][col] = tk.Button(root, width=10, height=5, bg='gray', command=lambda r=row, c=col: on_card_click(r, c))
            buttons[row][col].grid(row=row, column=col)
    return buttons

def main():
    global root, cards, card_buttons, grid, flips, NUM_ROWS, NUM_COLS, start_time

    root = tk.Tk()
    root.title('Jeu de mémoire')

    cards = generate_cards()
    NUM_ROWS = NUM_CARDS // 4
    NUM_COLS = 4

    grid = [[False for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
    card_buttons = create_card_buttons()
    flips = []

    start_time = time.time()

    root.mainloop()

if __name__ == "__main__":
    main()
