import random
import time
import sqlite3

# Configuration du jeu
CARD_VALUES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
NUM_CARDS = 16
DB_FILE = 'memory_game.db'

# Initialise la base de données et crée la table pour les scores
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS scores (player_name TEXT, time_taken INTEGER)''')
conn.commit()

class Card:
    def __init__(self, value):
        self.value = value
        self.is_revealed = False

    def __str__(self):
        return self.value if self.is_revealed else '*'

class MemoryGame:
    def __init__(self, num_pairs):
        self.cards = [Card(val) for val in CARD_VALUES[:num_pairs] * 2]
        random.shuffle(self.cards)
        self.num_pairs = num_pairs
        self.board_size = int(num_pairs ** 0.5)
        self.board = [[self.cards[i * self.board_size + j] for j in range(self.board_size)] for i in range(self.board_size)]
        self.flips = []

    def print_board(self):
        for row in self.board:
            print(' '.join(str(card) for card in row))

    def is_game_over(self):
        return all(all(card.is_revealed for card in row) for row in self.board)

    def flip_card(self, x, y):
        if not self.board[x][y].is_revealed and len(self.flips) < 2:
            self.board[x][y].is_revealed = True
            self.flips.append((x, y))

    def check_flips(self):
        if len(self.flips) == 2:
            (x1, y1), (x2, y2) = self.flips
            card1, card2 = self.board[x1][y1], self.board[x2][y2]
            if card1.value == card2.value:
                card1.is_revealed = card2.is_revealed = True
            else:
                time.sleep(1)
                card1.is_revealed = card2.is_revealed = False
            self.flips.clear()

    def save_score(self, player_name, time_taken):
        cursor.execute("INSERT INTO scores VALUES (?, ?)", (player_name, time_taken))
        conn.commit()

def main():
    num_pairs = NUM_CARDS // 2
    game = MemoryGame(num_pairs)
    
    print("Bienvenue dans le Jeu de Mémoire !")
    print("Trouvez toutes les paires de cartes correspondantes.")

    start_time = time.time()

    while not game.is_game_over():
        game.print_board()

        try:
            x, y = map(int, input("Entrez les coordonnées de la carte à retourner (x, y): ").split(','))
            if 1 <= x <= game.board_size and 1 <= y <= game.board_size:
                game.flip_card(x - 1, y - 1)
                game.check_flips()
            else:
                print("Coordonnées invalides, veuillez réessayer.")
        except ValueError:
            print("Entrée invalide, veuillez entrer les coordonnées sous la forme x,y.")
    
    total_time = int(time.time() - start_time)
    player_name = input("Bravo! Vous avez terminé le jeu. Entrez votre nom pour enregistrer votre score: ")
    game.save_score(player_name, total_time)
    print("Score enregistré avec succès. Merci d'avoir joué !")

if __name__ == "__main__":
    main()
