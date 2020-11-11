from pygame import Color, Rect, Surface

class IntroScreen():
    def __init__(self, size_ = (0, 0)):
        self.size = size_
        self.bg = Color(69, 139, 116)

    def update(self):
        pass

    def render(self):
        from engine.game_env import Game
        Game.get_surface().fill(self.bg)

    def resize(self, new_size):
        self.size = new_size
