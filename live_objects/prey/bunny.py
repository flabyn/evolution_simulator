from live_objects.prey.prey import Prey
import pygame as py

class Bunny(Prey):
    def __init__(self, x: int, y: int,resourcemap,groundmap) -> None:
        super().__init__(x, y,resourcemap,groundmap)
        self.image = py.image.load("assets\Bunny.png")