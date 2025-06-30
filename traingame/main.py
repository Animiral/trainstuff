import pygame
import math
import random
from . import model

# Constants
CELL_SIZE = 50  # Size of each cell in the grid (you can change this as needed)
class Game:
    def __init__(self):
        pygame.init()
        self.window_width = model.MAP_SIZE[0] * CELL_SIZE
        self.window_height = model.MAP_SIZE[1] * CELL_SIZE
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Railway Game")
        self.model = model.Model()
        self.model.randomize(n_players = 1)
        self.edit_connection = model.Connection.EAST_WEST

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = self.get_cell_from_position(event.pos)
                    if event.button == 1:
                        self.on_click(row, col)
                    elif event.button == 3:
                        self.on_right_click(row, col)
            self.draw_grid()
            pygame.display.flip()

    def get_cell_from_position(self, pos):
        x, y = pos
        return y // CELL_SIZE, x // CELL_SIZE

    def on_click(self, row, col):
        # Cycle through contents when a tile is clicked
        grid = self.model.map.grid
        tile = grid[row][col]
        if isinstance(tile, model.City):
           # grid[row][col] = model.TrackTile()
           pass
        else:
            if self.edit_connection in tile.track:
                tile.track.remove(self.edit_connection)
            else:
                tile.track.add(self.edit_connection)

    def on_right_click(self, row, col):
        # Cycle through connection types when right-clicking
        connections = list(model.Connection)
        current_index = connections.index(self.edit_connection)
        next_index = (current_index + 1) % len(connections)
        self.edit_connection = connections[next_index]

    def draw_grid(self):
        self.screen.fill((255, 255, 255))  # White background
        grid = self.model.map.grid
        for i in range(model.MAP_SIZE[1]):
            for j in range(model.MAP_SIZE[0]):
                tile = grid[i][j]
                is_city = isinstance(tile, model.City)
                if is_city:
                    self.draw_city(tile, i, j)
                else:
                    self.draw_tracktile(tile, i, j)

    def draw_city(self, tile, i, j):
        color = (169, 169, 169)
        pygame.draw.rect(self.screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        city_name = tile.name
        font_size = 20 if len(city_name) <= 6 else 15
        font = pygame.font.Font(None, font_size)
        text = font.render(city_name, True, (255, 255, 255))
        text_rect = text.get_rect(center=((j * CELL_SIZE) + CELL_SIZE/2, (i * CELL_SIZE) + CELL_SIZE/2))
        self.screen.blit(text, text_rect)

    def draw_tracktile(self, tile, i, j):
        color = (0, 128, 0)
        pygame.draw.rect(self.screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        # Draw connections as thick black lines
        top, bottom, left, right = i * CELL_SIZE, (i+1) * CELL_SIZE, j * CELL_SIZE, (j+1) * CELL_SIZE
        center_x = j * CELL_SIZE + CELL_SIZE // 2
        center_y = i * CELL_SIZE + CELL_SIZE // 2
        color = (0, 0, 0)
        line_width = 5
        for connection in tile.track:
            if connection == model.Connection.NORTH_SOUTH:
                pygame.draw.line(self.screen, color, (center_x, top), (center_x, bottom), line_width)
            elif connection == model.Connection.EAST_WEST:
                pygame.draw.line(self.screen, color, (left, center_y), (right, center_y), line_width)
            elif connection == model.Connection.NORTH_EAST:
                pygame.draw.arc(self.screen, color, (center_x, center_y - CELL_SIZE, CELL_SIZE, CELL_SIZE),
                                math.pi, math.pi*3/2, line_width)
            elif connection == model.Connection.NORTH_WEST:
                pygame.draw.arc(self.screen, color, (center_x - CELL_SIZE, center_y - CELL_SIZE, CELL_SIZE, CELL_SIZE),
                                math.pi*3/2, 0, line_width)
            elif connection == model.Connection.SOUTH_EAST:
                pygame.draw.arc(self.screen, color, (center_x, center_y, CELL_SIZE, CELL_SIZE),
                                math.pi/2, math.pi, line_width)
            elif connection == model.Connection.SOUTH_WEST:
                pygame.draw.arc(self.screen, color, (center_x - CELL_SIZE, center_y, CELL_SIZE, CELL_SIZE),
                                0, math.pi/2, line_width)

if __name__ == "__main__":
    game = Game()
    game.run()
