import pygame
import random

# Constants
GRID_SIZE = 10
NUM_CITIES = 6
TILES = ['grass', 'city']
CELL_SIZE = 50  # Size of each cell in the grid (you can change this as needed)
WINDOW_WIDTH = GRID_SIZE * CELL_SIZE
WINDOW_HEIGHT = GRID_SIZE * CELL_SIZE

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Grid Game")
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.initialize_grid()

    def initialize_grid(self):
        # Randomly initialize the grid with 'grass' or 'city'
        city_positions = random.sample(range(GRID_SIZE * GRID_SIZE), NUM_CITIES)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if i * GRID_SIZE + j in city_positions:
                    self.grid[i][j] = 'city'
                else:
                    self.grid[i][j] = 'grass'

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
                    row, col = self.get_cell_from_position(event.pos)
                    self.on_click(row, col)

            self.draw_grid()
            pygame.display.flip()

    def get_cell_from_position(self, pos):
        x, y = pos
        return y // CELL_SIZE, x // CELL_SIZE

    def on_click(self, row, col):
        # Cycle through contents when a tile is clicked
        current_tile = self.grid[row][col]
        next_tile = TILES[(TILES.index(current_tile) + 1) % len(TILES)]
        self.grid[row][col] = next_tile

    def draw_grid(self):
        self.screen.fill((255, 255, 255))  # White background
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                color = (0, 128, 0) if self.grid[i][j] == 'grass' else (169, 169, 169)  # Green for grass, grey for city
                pygame.draw.rect(self.screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

if __name__ == "__main__":
    game = Game()
    game.run()
