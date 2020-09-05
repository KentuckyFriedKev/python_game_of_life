import pygame
import time
from Button import Button
from Cell import Cell
from Internal_Grid import Grid

pygame.init()

class Game:
    def __init__(self):
        # Set window width and height
        self.display_width = 702
        self.display_height = 754
        # Set number of cells to use in game
        self.cell_x = 100
        self.cell_y = 100
        # Initialize a grid to keep track of the statuses of all cells
        self.grid = Grid(self.cell_x, self.cell_y)
        # Set some properties on for the window
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Conway\'s Game of Life')
        self.clock = pygame.time.Clock()
        # Create a bool to determine whenever to loop the update grid function
        self.loop = False
        # Create a variable to terminate the game
        self.game_exit = False
        self.controls = pygame.sprite.Group()
        self.cells = pygame.sprite.Group()
        self.stop = pygame.sprite.Group()
        self.step_button = Button(100, 702, 100, 50, self.update_cells, "Step 1")
        self.loop_button = Button(500, 702, 100, 50, self.set_loop, "Loop")
        self.stop_button = Button(500, 702, 100, 50, self.set_loop, "Stop")
        self.clear_button = Button(300, 702, 100, 50, self.clear_grid, "Clear")
        x = 2
        for i in range(self.cell_x):
            y = 2
            for j in range(self.cell_y):
                new_cell = Cell(x, y, i, j, self.grid)
                self.cells.add(new_cell)
                y += 7
            x += 7

        self.controls.add(self.step_button)
        self.controls.add(self.loop_button)
        self.controls.add(self.clear_button)
        self.stop.add(self.stop_button)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if not self.loop:
                for button in self.controls:
                    button.handle_event(event)
                for cell in self.cells:
                    cell.handle_event(event)
            else:
                self.stop_button.handle_event(event)

    def draw(self):
        self.game_display.fill((200,200,200))
        if not self.loop:
            self.controls.draw(self.game_display)
        else:
            self.stop.draw(self.game_display)
        self.cells.draw(self.game_display)
        pygame.display.update()

    def run(self):
        while not self.game_exit:
            if self.loop:
                self.update_cells()
            self.event_loop()
            self.draw()
            self.clock.tick(60)

    def quit(self):
        self.game_exit = True

    def update_cells(self):
        self.grid.update()
        for cell in self.cells:
            cell.check_status()

    def set_loop(self):
        self.loop = not self.loop

    def clear_grid(self):
        self.grid.clear()
        for cell in self.cells:
            cell.check_status()


if __name__ == '__main__':
    pygame.init()
    Game().run()
    pygame.quit()

