from tiles.Ground.Ground import Ground
import pygame as py

class Grass(Ground):
    def __init__(self,x,y) -> None:
        super().__init__(x,y)
        self.image = py.image.load("assets\grass.png")
        self.walkable = True