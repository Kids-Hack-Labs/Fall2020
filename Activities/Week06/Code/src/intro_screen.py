import pygame
from pygame import Color, Rect, Surface

class IntroScreen():
    def __init__(self):
        self.size = pygame.display.get_surface().get_size()
        self.bg = Color(69, 139, 116)

    def update(self):
        pass

    def render(self):
        pygame.display.get_surface().fill(self.bg)

    def resize(self, new_size):
        self.size = new_size
