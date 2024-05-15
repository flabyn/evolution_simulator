from tiles.Resource.Resource import Resource
import pygame as py
from config import *
import random

class Fruit(Resource):
    def __init__(self,x,y) -> None:
        super().__init__(x,y)
        self.growthState = 0
        self.maxGrowthState = 2
        self.growthChance = 0.005

        self.image = [py.image.load("assets/fruit1.png"),py.image.load("assets/fruit2.png"),py.image.load("assets/fruit3.png")]
    def drawSelf(self, screen):
        screen.blit(self.image[self.growthState], (self.x*TileSize.x,self.y*TileSize.y))
    def step(self):
        if random.random() < self.growthChance and self.growthState != self.maxGrowthState:
            self.growthState += 1