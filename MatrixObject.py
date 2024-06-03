import pygame as py
from config import *
class MatrixObject:
    def __init__(self,x:int,y:int) -> None:
        self.x = x
        self.y = y
        self.image = None
    def drawSelf(self,screen):
        if self.image:
            screen.blit(self.image, (self.x*TileSize.x,self.y*TileSize.y))
    def step(self,Matrix):
        pass
