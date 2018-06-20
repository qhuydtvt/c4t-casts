from game_object import GameObject
import pygame


class BoxCollider(GameObject):
    def __init__(self, width, height):
        GameObject.__init__(self, 0, 0)
        self.width = width
        self.height = height

    def render(self, canvas):
        RED = (255, 0, 0)
        rect = (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(canvas, RED, rect, 1)