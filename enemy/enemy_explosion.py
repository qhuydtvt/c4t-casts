from game_object import GameObject
from renderers.image_renderer import ImageRenderer


class EnemyExplosion(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("images/enemy/bacteria_dead5.png")