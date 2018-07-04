import pygame
from game_object import GameObject
from physics.box_collider import BoxCollider

from game_object import collide_with, add as add_game_object
from enemy.enemy import Enemy
from renderers.image_renderer import ImageRenderer
from enemy.enemy_explosion import EnemyExplosion


class PlayerBullet(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.box_collider = BoxCollider(12, 48)
        self.renderer = ImageRenderer('images/player/player_bullet1.png')

    def update(self):
        GameObject.update(self)

        collide_list = collide_with(self.box_collider, Enemy)
        for game_object in collide_list:
            explosion = EnemyExplosion(game_object.x, game_object.y)
            add_game_object(explosion)
            game_object.deactivate()
            self.deactivate()

        self.move()
        self.deactivate_if_needed()

    def move(self):
        self.y -= 5

    def deactivate_if_needed(self):
        if self.y <= 0:
            self.deactivate()
