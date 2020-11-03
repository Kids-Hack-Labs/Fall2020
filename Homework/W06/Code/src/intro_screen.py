'''
    Code copied directly from the class folder, adapted for the
    homework
'''
import pygame
from pygame import Color, Rect, Surface

class IntroScreen():
    def __init__(self):
        self.size = pygame.display.get_surface().get_size()
        self.bg = Color(69, 139, 116)

        #Homework-specific code
        self.surf_size = (50, 50)
        self.surf = Surface(self.surf_size, pygame.SRCALPHA)
        #We're hard-coding the colour because it will be used only once
        self.surf.fill(Color(0, 0, 0, 0))
        self.rect = self.surf.get_rect()
        #creating arbitrary colour
        t = Color(186, 116, 139)
        pygame.draw.circle(self.surf, t, self.rect.center, int(self.surf_size[0]/2))
        self.rect.center = (int(self.size[0]/2), int(self.size[1]/2))

    def update(self):
        pass

    def render(self):
        temp_surf = pygame.display.get_surface()
        temp_surf.fill(self.bg)
        temp_surf.blit(self.surf, self.rect)

    def resize(self, new_size):
        self.size = new_size

        #CHALLENGE CODE
        self.surf_size = (int(new_size[0]/9), int(new_size[0]/9))
        self.surf = Surface(self.surf_size, pygame.SRCALPHA)
        #We're hard-coding the colour because it will be used only once
        self.surf.fill(Color(0, 0, 0, 0))
        self.rect = self.surf.get_rect()
        #creating arbitrary colour
        t = Color(186, 116, 139)
        pygame.draw.circle(self.surf, t, self.rect.center, int(self.surf_size[0]/2))
        self.rect.center = (int(self.size[0]/2), int(self.size[1]/2))
        
