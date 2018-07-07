import pygame
from player.player_bullet import PlayerBullet
import game_object
from game_object import GameObject
from frame_counter import FrameCounter
from player.player_animator import PlayerAnimator


class Player(GameObject):
    # 1. Create constructor (properties)
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.input_manager = input_manager
        self.shoot_lock = False
        self.counter = FrameCounter(30)
        self.renderer = PlayerAnimator()
        self.dx = 0
        self.dy = 0

    # 2. Describe action / method / behavior
    def update(self):
        GameObject.update(self)
        self.move()
        self.update_animator()
        self.shoot()

    def update_animator(self):
        self.renderer.update(self.dx, self.dy)

    def move(self):
        self.dx = 0
        self.dy = 0

        if self.input_manager.right_pressed:
            self.dx += 3
        if self.input_manager.left_pressed:
            self.dx -= 3
        if self.input_manager.down_pressed:
            self.dy += 3
        if self.input_manager.up_pressed:
            self.dy -= 3

        self.x += self.dx
        self.y += self.dy

    def shoot(self):
        if self.input_manager.x_pressed and not self.shoot_lock:
            game_object.recycle(PlayerBullet, self.x, self.y - 40)
            self.shoot_lock = True

        if self.shoot_lock:
            self.counter.run()
            if self.counter.expired:
                self.shoot_lock = False
                self.counter.reset()
