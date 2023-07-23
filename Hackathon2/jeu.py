import pygame
import sqlite3
import random
import time

# Configuration du jeu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CARD_WIDTH = 100
CARD_HEIGHT = 100
FPS = 60
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

# Initialise la base de données et crée la table pour les scores
conn = sqlite3.connect('memory_game.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS scores (player_name TEXT, time_taken INTEGER)''')
conn.commit()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jeu de mémoire')

def generate_cards():
    cards = []
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'cyan']
    for color in colors:
        cards.append(pygame.image.load(f'{color}_card.png').convert())
        cards.append(pygame.image.load(f'{color}_card.png').convert())
    random.shuffle(cards)
    return cards

def draw_card(card, x, y):
    screen.blit(card, (x, y))

def main():
    running = True
    clock = pygame.time.Clock()
    cards = generate_cards()
    num_columns = 4
    num_rows = len(cards) // num_columns

    # grille pour garder trace des cartes retournées
    grid = [[False for _ in range(num_columns)] for _ in range(num_rows)]
    flips = []

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and len(flips) < 2:
                x, y = pygame.mouse.get_pos()
                row = y // CARD_HEIGHT
                col = x // CARD_WIDTH
                if not grid[row][col]:
                    flips.append((row, col))
                    grid[row][col] = True

        if len(flips) == 2:
            r1, c1 = flips[0]
            r2, c2 = flips[1]
            if cards[r1 * num_columns + c1] != cards[r2 * num_columns + c2]:
                time.sleep(1)
                grid[r1][c1] = False
                grid[r2][c2] = False
            flips.clear()

        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c]:
                    draw_card(cards[r * num_columns + c], c * CARD_WIDTH, r * CARD_HEIGHT)
                else:
                    pygame.draw.rect(screen, GRAY, (c * CARD_WIDTH, r * CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT))

        pygame.display.flip()
        if all(all(row) for row in grid):
            # Toutes les cartes ont été retournées, le jeu est terminé
            player_name = input("Bravo! Vous avez terminé le jeu. Entrez votre nom pour enregistrer votre score: ")
            time_taken = pygame.time.get_ticks() // 1000
            cursor.execute("INSERT INTO scores VALUES (?, ?)", (player_name, time_taken))
            conn.commit()
            running = False

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
