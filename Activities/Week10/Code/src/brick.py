from pygame import Color, Rect, Surface

class Brick():
    surf = None
    def __init__(self, anchor = (0, 0), extent = (0, 0), colour_ = Color(255, 255, 255)):
        self.rect = Rect(anchor, extent)
        self.colour = colour_
        self.active = True
        Brick.surf = Surface(extent)

    def update(self, delta_ms):
        pass

    def render(self):
        if self.active:
            from engine.game_env import Game
            Brick.surf.fill(self.colour)
            Game.get_surface().blit(Brick.surf, self.rect)
