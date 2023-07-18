import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GameOfLife:
    def __init__(self, size, initial_state):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.grid_next = np.zeros((size, size), dtype=int)
        self.init_grid(initial_state)

    def init_grid(self, initial_state):
        for i, row in enumerate(initial_state):
            for j, cell in enumerate(row):
                self.grid[i+1, j+1] = cell

    def get_neighbors(self, i, j):
        neighbors = [
            (i-1, j-1), (i-1, j), (i-1, j+1),
            (i, j-1), (i, j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1)
        ]
        return neighbors

    def count_live_neighbors(self, i, j):
        neighbors = self.get_neighbors(i, j)
        count = 0
        for neighbor in neighbors:
            count += self.grid[neighbor[0], neighbor[1]]
        return count

    def update_grid(self):
        for i in range(1, self.size-1):
            for j in range(1, self.size-1):
                live_neighbors = self.count_live_neighbors(i, j)
                if self.grid[i, j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        self.grid_next[i, j] = 0
                else:
                    if live_neighbors == 3:
                        self.grid_next[i, j] = 1
        self.grid = np.copy(self.grid_next)

    def play_game(self, num_generations):
        fig = plt.figure()
        ims = []
        for _ in range(num_generations):
            im = plt.imshow(self.grid, cmap='binary', interpolation='nearest')
            ims.append([im])
            self.update_grid()
        ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True)
        plt.show()


# Example usage:
size = 30
initial_state = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

game = GameOfLife(size, initial_state)
game.play_game(num_generations=50)
