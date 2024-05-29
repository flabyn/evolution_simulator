from live_objects.prey.prey import Prey
import pygame as py

class Bunny(Prey):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.image = py.image.load("assets\Bunny.png")