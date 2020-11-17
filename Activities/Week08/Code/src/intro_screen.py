from pygame import Color, Rect, Surface

from src.paddle import Paddle
from src.ball import Ball

class IntroScreen():
    def __init__(self, size_ = (0, 0)):
        self.size = size_
        self.bg = Color(69, 139, 116)

        self.ball = Ball()
        self.paddle = Paddle()
        
    def update(self, delta_ms):
        self.ball.update(delta_ms)
        self.paddle.update(delta_ms)

    def render(self):
        from engine.game_env import Game
        Game.get_surface().fill(self.bg)

        self.ball.render()
        self.paddle.render()
        
    def resize(self, new_size):
        self.size = new_size
