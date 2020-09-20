import pygame

# TODO: Add comments
# TODO: optimize setting cells in UI (user should be able to hold mouse and set multiple cells
"""
 Represents a single cell on the game screen
 Inherited from pygame sprite class
"""


class Cell(pygame.sprite.Sprite):
    """
    Creates a cell object

    INPUTS:
    x (int) - x-coordinate of the cell on the screen
    y (int) - y-coordinate of the cell on the screen
    i (int) - first index of the cell that corresponds to the internal grid
    j (int) - second index of the cell that corresponds to the internal grid
    grid (Grid) - Instance of a grid class which keeps track of the status of each cell
    """
    def __init__(self, x,y, i, j, grid):
        super().__init__()
        self.i = i
        self.j = j
        self.grid = grid
        # Create 5 by 5px images to represent the cells
        # live cells are black
        self.live_cell = pygame.Surface((5, 5))
        self.live_cell.fill(pygame.Color(0,0,0))
        # dead cells are white
        self.dead_cell = pygame.Surface((5, 5))
        self.dead_cell.fill(pygame.Color(255, 255, 255))
        # cells will turn light gray when hovered upon
        self.hover_cell = pygame.Surface((5, 5))
        self.hover_cell.fill(pygame.Color(150, 150, 150))
        # cells will turn dark gray when clicked on
        self.pressed_cell = pygame.Surface((5,5))
        self.pressed_cell.fill(pygame.Color(100,100,100))
        # Inherited from pygame sprite
        # Set first image of cell to be a dead cell
        self.image = self.dead_cell
        # Set collision boundaries for the cell
        self.rect = self.image.get_rect(topleft=(x, y))
        # bool to see if the button has been pressed
        self.pressed = False

    """
    Update the image of the cell based off the cell's status from the internal grid (1 means alive, 0 means dead)
    INPUTS
    N/A
    OUTPUTS
    N/A
    """

    def check_status(self):
        if self.grid.get_status(self.i, self.j) == 1:
            self.image = self.live_cell
        else:
            self.image = self.dead_cell

    """
    Event handler for the cell, handles MOUSEBUTTONDOWN, MOUSEBUTTONUP, and MOUSEMOTION events
    INPUTS
    event (pygame.event) - event in pygame
    OUTPUTS
    N/A
    """

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.image = self.pressed_cell
                self.pressed = True
            else:
                self.check_status()
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos) and self.pressed:
                self.grid.set_status(self.i, self.j)
                self.image = self.hover_cell
            self.pressed = False
        elif event.type == pygame.MOUSEMOTION:
            collided = self.rect.collidepoint(event.pos)
            if collided and not self.pressed:
                self.image = self.hover_cell
            elif not collided:
                self.check_status()


