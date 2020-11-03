import sys
import pygame
from pygame.time import Clock
from src.intro_screen import IntroScreen

FPS = 30
class Game():
    def __init__(self):
        self.screen_size = (450, 600)
        self.title = "Week 06"
        self.clock = Clock()
        self.delta = 0
        self.time_since_started = 0

        pygame.init()
        self.time_since_started = pygame.time.get_ticks()

        self.screen_surf = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
        pygame.display.set_caption(self.title)

        self.game_screen = IntroScreen()

        self.is_running = True

    def process_events(self):
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                self.is_running = False
            if evt.type == pygame.VIDEORESIZE:
                self.screen_size = evt.size

    def update(self):
        #The alternative to the second term in the equality comparison
        #is pygame.display.get_surface().get_size()
        if self.screen_size != self.screen_surf.get_size():
            self.screen_surf = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
            self.game_screen.resize(self.screen_size)
        self.game_screen.update()

    def render(self):
        self.game_screen.render()
        pygame.display.flip()

    #swithed cleanup() and run() order, for organization
    def cleanup(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while self.is_running:
            self.process_events()
            self.update()
            self.render()
            self.delta = self.clock.tick(FPS)
            self.time_since_started = pygame.time.get_ticks()
        self.cleanup()
