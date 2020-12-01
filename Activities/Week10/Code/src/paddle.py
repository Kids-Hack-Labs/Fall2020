from pygame.locals import *
from pygame import Color, Rect, Surface

class Paddle():
    def __init__(self):
        self.rect = Rect(0, 0, 75, 25)
        self.colour = Color(0, 0, 127)
        self.surf = Surface(self.rect.size)
        self.surf.fill(self.colour)
        self.x_vel = 0.5
        
        self.rect.top = 550

    def update(self, delta_ms):
        from engine.game_env import Game
        left  = Game.get_key(K_a) or Game.get_key(K_LEFT)
        right = Game.get_key(K_d) or Game.get_key(K_RIGHT)

        if left:
            self.rect.centerx -= int(self.x_vel * delta_ms)
        if right:
            self.rect.centerx += int(self.x_vel * delta_ms)

    def render(self):
        from engine.game_env import Game
        Game.get_surface().blit(self.surf, self.rect)
