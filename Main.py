import pygame
import time
from Button import Button
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

# Create some text to display, used by display_text
# INPUTS
# text (string)- text contained by the object
# font (pygame.font.Font)- font used by the text
# OUTPUT
# textSurface - the text object to be displayed on the screen
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# Display some text
# INPUTS
# text (string) - text to be displayed
# x - (int) - x coordinate of the center of the text
# y - (int) - y coordinate of the center of the text
# font_size (int) - font size (in px) of the text
def display_text(text, x, y, font_size):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    textSurface, textRect = text_objects(text, font)
    textRect.center = (x,y)
    game_display.blit(textSurface, textRect)


# Declare some colors as RGB values tuples
black = (0,0,0)
white = (255, 255, 255)
light_gray = (200, 200, 200)
dark_gray = (150, 150, 150)

# Display a cell
# INPUTS
# x - (int) - x coordinate of the top left corner of the cell
# y - (int) - y coordinate of the top left corner of the cell
# b - (int) - length of the base of the cell
# h - (int) - length of the height of the cell
# ic - (tuple - (int, int, int)) - RGB value of the colo the button appears in when the mouse is not over the cell
# ac - (tuple - (int, int, int)) - RGB value of the color the button appears in when the mouse is over the cell
# action - (function) - function to execute when the button is clicked
def cell(x, y, i, j, b, h, dead, alive, hover):
    if not lock:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + b > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(game_display, hover, (x, y, b, h))
            if click[0] == 1:
                grid.set_status(i, j)
        else:
            if grid.grid[i][j] == 0:
                pygame.draw.rect(game_display, dead, (x, y, b, h))
            else:
                pygame.draw.rect(game_display, alive, (x, y, b, h))


def update_cells():
    grid.update()

def draw_cells():
    grid_x = -1
    for i in range(2, display_width, 7):
        grid_x += 1
        grid_y = 0
        for j in range(2, display_height - 52, 7):
            cell(i, j, grid_x, grid_y, 5, 5, white, black, dark_gray)
            grid_y += 1


def game_loop():
    game_exit = False
    controls = pygame.sprite.Group()
    step_button = Button(100, 702, 100, 50, update_cells, "Step 1")
    controls.add(step_button)

    while not game_exit:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            for button in controls:
                button.handle_event(event)
        game_display.fill(light_gray)
        controls.draw(game_display)
        draw_cells()
        pygame.display.update()
        clock.tick(60)


game_loop()
quit()

