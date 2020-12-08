from pygame import Color, Rect, Surface

class Ball():
    def __init__(self):
        self.radius = 10
        self.size = (self.radius*2, self.radius*2)
        self.colour = Color(63, 0, 31)
        self.surf = Surface(self.size)
        self.rect = self.surf.get_rect()
        self.vel = [0.25, 0.25]
        self.launched = False
        
        import pygame.draw
        pygame.draw.circle(self.surf, self.colour, self.rect.center, self.radius)

        self.surf.set_colorkey(Color(0, 0, 0))

    def update(self, delta_ms):
        if self.launched:
            self.rect.centerx += int(self.vel[0] * delta_ms)
            self.rect.centery += int(self.vel[1] * delta_ms)

    def render(self):
        from engine.game_env import Game
        Game.get_surface().blit(self.surf, self.rect)

    def launch(self):
        self.launched = True
