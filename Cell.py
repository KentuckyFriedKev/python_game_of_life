import pygame


class Cell(pygame.sprite.Sprite):
    def __init__(self, x,y, i, j, grid):
        super().__init__()
        self.i = i
        self.j = j
        self.grid = grid
        self.live_cell = pygame.Surface((5, 5))
        self.live_cell.fill(pygame.Color(0,0,0))
        self.dead_cell = pygame.Surface((5, 5))
        self.dead_cell.fill(pygame.Color(255, 255, 255))
        self.hover_cell = pygame.Surface((5, 5))
        self.hover_cell.fill(pygame.Color(150, 150, 150))
        self.pressed_cell = pygame.Surface((5,5))
        self.pressed_cell.fill(pygame.Color(100,100,100))
        # Inherited from pygame sprite
        self.image = self.dead_cell
        self.rect = self.image.get_rect(topleft=(x, y))

        self.pressed = False

    def check_status(self):
        if self.grid.get_status(self.i, self.j) == 1:
            self.image = self.live_cell
        else:
            self.image = self.dead_cell

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


