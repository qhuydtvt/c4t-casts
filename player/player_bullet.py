import pygame
from game_object import GameObject
from physics.box_collider import BoxCollider


class PlayerBullet(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load('images/player/player_bullet1.png')
        self.box_collider = BoxCollider(12, 48)

    def update(self):
        GameObject.update(self)

        self.move()
        self.deactivate_if_needed()

    def move(self):
        self.y -= 5

    def deactivate_if_needed(self):
        if self.y <= 0:
            self.deactivate()
