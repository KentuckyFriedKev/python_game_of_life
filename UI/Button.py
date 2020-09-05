# TODO: Add comments
"""
Class for a button in pygame

Credit to skrx on Stack Overflow for the basis of this class: https://stackoverflow.com/questions/47639826/pygame-button-single-click
"""

import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, action = None, text="", text_color=(0,0,0)):
        super().__init__()
        font = pygame.font.Font('freesansbold.ttf', 24)

        self.button_normal = pygame.Surface((width, height))
        self.button_normal.fill(pygame.Color(255,255,255))
        self.button_hover = pygame.Surface((width, height))
        self.button_hover.fill(pygame.Color(150,150,150))
        self.button_down = pygame.Surface((width, height))
        self.button_down.fill(pygame.Color(100,100,100))
        # Inherited from pygame sprite
        self.image = self.button_normal
        self.rect = self.image.get_rect(topleft=(x, y))

        button_center = self.image.get_rect().center
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=button_center)
        for button in (self.button_normal, self.button_hover, self.button_down):
            button.blit(text_surface, text_rect)
        self.action = action
        self.pressed = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.image = self.button_down
                self.pressed = True
            else:
                self.image = self.button_normal
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos) and self.pressed:
                self.action()
                self.image = self.button_hover
            self.pressed = False
        elif event.type == pygame.MOUSEMOTION:
            collided = self.rect.collidepoint(event.pos)
            if collided and not self.pressed:
                self.image = self.button_hover
            elif not collided:
                self.image = self.button_normal





