from game_object import GameObject
from renderers.animation import Animation


class EnemyExplosion(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = Animation(["images/enemy/bacteria_dead1.png",
                                   "images/enemy/bacteria_dead2.png",
                                   "images/enemy/bacteria_dead3.png",
                                   "images/enemy/bacteria_dead4.png",
                                   "images/enemy/bacteria_dead5.png"])