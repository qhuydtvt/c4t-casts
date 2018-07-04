import pygame
from game_object import GameObject
from physics.box_collider import BoxCollider

from renderers.animation import Animation


class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.box_collider = BoxCollider(30, 30)
        self.renderer = Animation(["images/enemy/bacteria1.png",
                                   "images/enemy/bacteria2.png",
                                   "images/enemy/bacteria3.png",
                                   "images/enemy/bacteria4.png",
                                   "images/enemy/bacteria5.png",
                                   "images/enemy/bacteria6.png",],
                                  loop=True,
                                  frame_delay=10)

    def update(self):
        GameObject.update(self)
        self.y += 3
