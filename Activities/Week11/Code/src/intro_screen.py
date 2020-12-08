from pygame import Color, Rect, Surface

from src.paddle import Paddle
from src.ball import Ball
from src.brick import Brick

class IntroScreen():
    def __init__(self, size_ = (0, 0)):
        self.size = size_
        self.bg = Color(69, 139, 116)

        self.ball = Ball()
        self.paddle = Paddle()

        brick_size = (50, 25)
        brick_colour = Color(63, 0, 127)
        self.bricks = []

        for x in range(6, self.size[0] - brick_size[0], brick_size[0]+5):
            for y in range(25, 250, brick_size[1]+3):
                self.bricks.append(Brick((x, y), brick_size, brick_colour))
        
    def update(self, delta_ms):
        self.ball.update(delta_ms)
        self.paddle.update(delta_ms)

        if not self.ball.launched:
            self.ball.rect.centerx = self.paddle.rect.centerx
            self.ball.rect.bottom = self.paddle.rect.top
            self.launch_ball()

        for br in self.bricks:
            br.update(delta_ms)

        self.brick_bounce()
        self.bound_ball()
        self.bind_paddle()

        self.paddle_bounce()

        

    def render(self):
        from engine.game_env import Game
        Game.get_surface().fill(self.bg)

        for br in self.bricks:
            br.render()

        self.ball.render()
        self.paddle.render()
        
    def resize(self, new_size):
        self.size = new_size

    def bound_ball(self):
        if self.ball.rect.left < 0:
            self.ball.rect.left = 0
            self.ball.vel[0] *= -1
        if self.ball.rect.right > self.size[0]:
            self.ball.rect.right = self.size[0]
            self.ball.vel[0] *= -1
        if self.ball.rect.top < 0:
            self.ball.rect.top = 0
            self.ball.vel[1] *= -1
        if self.ball.rect.bottom > self.size[1]:
            self.ball.rect.bottom = self.size[1]
            self.ball.vel[1] *= -1

    def bind_paddle(self):
        if self.paddle.rect.left < 0:
            self.paddle.rect.left = 0
        if self.paddle.rect.right > self.size[0]:
            self.paddle.rect.right = self.size[0]

    def paddle_bounce(self):
        tolerance = 0.2929
        
        overlap = self.paddle.rect.clip(self.ball.rect)

        if overlap:
            if overlap.width < overlap.height:
                if self.ball.rect.centerx < overlap.centerx:
                    self.ball.rect.right = overlap.left - 1
                else:
                    self.ball.rect.left = overlap.right + 1
                self.ball.vel[0] *= -1

                if overlap.height < self.ball.rect.height * tolerance:
                    if self.ball.rect.centery < overlap.centery:
                        self.ball.rect.bottom = overlap.top - 1
                        self.ball.vel[1] *= -1

            elif overlap.width > overlap.height:
                self.ball.rect.bottom = overlap.top - 1
                self.ball.vel[1] *= -1

                if overlap.width < self.ball.rect.width * tolerance:
                    if self.ball.rect.centerx < overlap.centerx:
                        self.ball.rect.right = overlap.left - 1
                    else:
                        self.ball.rect.left = overlap.right + 1
            else:
                if self.ball.rect.centerx < overlap.centerx:
                    self.ball.rect.right = overlap.left - 1
                else:
                    self.ball.rect.left = overlap.right + 1
                if self.ball.rect.centery < overlap.centery:
                    self.ball.rect.bottom = overlap.top - 1
                else:
                    self.ball.rect.top = self.paddle.rect.bottom + 1
                self.ball.vel[0] *= -1
                self.ball.vel[1] *= -1    

    def brick_bounce(self):
        for brick in self.bricks:
            if brick.active:
                test_x = self.ball.rect.centerx
                test_y = self.ball.rect.centery

                if self.ball.rect.centerx < brick.rect.left:
                    test_x = brick.rect.left
                elif self.ball.rect.centerx > brick.rect.right:
                    test_x = brick.rect.right

                if self.ball.rect.centery < brick.rect.top:
                    test_y = brick.rect.top
                elif self.ball.rect.centery > brick.rect.bottom:
                    test_y = brick.rect.bottom

                dist_x = self.ball.rect.centerx - test_x
                dist_y = self.ball.rect.centery - test_y

                dist_x *= dist_x
                dist_y *= dist_y

                distance = (dist_x + dist_y)**0.5

                if distance <= self.ball.radius:
                    brick.active = False
                    overlap = self.ball.rect.clip(brick.rect)

                    if overlap.width < overlap.height:
                        self.ball.vel[0] *= -1
                    elif overlap.width > overlap.height:
                        self.ball.vel[1] *= -1
                    else:
                        self.ball.vel[0] *= -1
                        self.ball.vel[1] *= -1

    def launch_ball(self):
        from pygame.locals import K_SPACE
        from engine.game_env import Game
        if Game.get_key(K_SPACE):
            self.ball.launch()
