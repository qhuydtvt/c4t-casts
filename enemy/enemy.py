import pygame
from game_object import GameObject
from physics.box_collider import BoxCollider

from renderers.image_renderer import ImageRenderer


class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.box_collider = BoxCollider(30, 30)
        self.renderer = ImageRenderer("images/enemy/bacteria1.png")

    def update(self):
        GameObject.update(self)
        self.y += 3
