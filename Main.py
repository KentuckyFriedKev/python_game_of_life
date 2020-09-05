import pygame
import time
from Button import Button
from Cell import Cell
from Internal_Grid import Grid

pygame.init()

# Set window width and height
display_width = 702
display_height = 754
# Set number of cells to use in game
cell_x = 100
cell_y = 100
grid = Grid(cell_x,cell_y)
# Set some properties on for the window
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Conway\'s Game of Life')
clock = pygame.time.Clock()
# Create a lock so the user can't change cells when the game is updating
lock = False

# Declare some colors as RGB values tuples
black = (0,0,0)
white = (255, 255, 255)
light_gray = (200, 200, 200)
dark_gray = (150, 150, 150)


def update_cells():
    grid.update()


def game_loop():
    game_exit = False
    controls = pygame.sprite.Group()
    cells = pygame.sprite.Group()
    step_button = Button(100, 702, 100, 50, update_cells, "Step 1")
    x = 2
    for i in range(cell_x):
        y = 2
        for j in range(cell_y):
            new_cell = Cell(x,y,i,j,grid)
            cells.add(new_cell)
            y += 7
        x += 7

    controls.add(step_button)

    while not game_exit:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            for button in controls:
                button.handle_event(event)
            for cell in cells:
                cell.handle_event(event)
        game_display.fill(light_gray)
        controls.draw(game_display)
        cells.draw(game_display)
        pygame.display.update()
        clock.tick(60)


game_loop()
quit()

