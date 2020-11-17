import sys
import pygame
from pygame.time import Clock
from src.intro_screen import IntroScreen

FPS = 30
class Game():
    screen_surf = None
    level = None
    keys = ()
    mouse_buttons = ()
    mouse_prev = ()
    mouse_pos = ()
    def __init__(self):
        self.screen_size = (450, 600)
        self.title = "Week 06"
        self.clock = Clock()
        self.delta = 0
        self.time_since_started = 0

        pygame.init()
        self.time_since_started = pygame.time.get_ticks()

        Game.screen_surf = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
        pygame.display.set_caption(self.title)

        Game.set_level(IntroScreen(self.screen_size))

        Game.keys = pygame.key.get_pressed()
        Game.mouse_buttons = pygame.mouse.get_pressed()
        Game.mouse_prev = Game.mouse_pos = pygame.mouse.get_pos()

        self.is_running = True

    def process_events(self):
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                self.is_running = False
            if evt.type == pygame.VIDEORESIZE:
                self.screen_size = evt.size
            if evt.type == pygame.KEYDOWN or\
               evt.type == pygame.KEYUP:
                Game.keys = pygame.key.get_pressed()
            if evt.type == pygame.MOUSEBUTTONDOWN or\
               evt.type == pygame.MOUSEBUTTONUP:
                Game.mouse_buttons = pygame.mouse.get_pressed()
                Game.mouse_prev = Game.mouse_pos
                Game.mouse_pos = pygame.mouse.get_pos()
            if evt.type == pygame.MOUSEMOTION:
                Game.mouse_prev = Game.mouse_pos
                Game.mouse_pos = pygame.mouse.get_pos()
                
    def update(self, delta_ms):
        #The alternative to the second term in the equality comparison
        #is pygame.display.get_surface().get_size()
        if self.screen_size != Game.screen_surf.get_size():
            Game.screen_surf = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
            Game.level.resize(self.screen_size)
        Game.level.update(delta_ms)

    def render(self):
        Game.level.render()
        pygame.display.flip()

    #swithed cleanup() and run() order, for organization
    def cleanup(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while self.is_running:
            self.process_events()
            self.update(self.delta)
            self.render()
            self.delta = self.clock.tick(FPS)
            self.time_since_started = pygame.time.get_ticks()
        self.cleanup()

    @staticmethod
    def get_surface():
        return Game.screen_surf

    @staticmethod
    def set_level(new_level):
        Game.level = new_level

    @staticmethod
    def get_keys():
        return Game.keys

    @staticmethod
    def get_key(key):
        return Game.keys[key]

    @staticmethod
    def get_mouse_buttons():
        return Game.mouse_buttons

    @staticmethod
    def get_mouse_prev():
        return Game.mouse_prev

    @staticmethod
    def get_mouse_pos():
        return Game.mouse_pos
