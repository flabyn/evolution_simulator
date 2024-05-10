import pygame as py
import config
Tiles = {0:py.image.load("assets\grass.png"),1:py.image.load("assets\water.png")}

class Map_Matrix:
    def __init__(self,mapdata,screen) -> None:
        self.map = self.generateClassMatrix(mapdata)
        self.screen:py.Surface = screen
    def generateClassMatrix(self,mapdata):
        classMatrix = []
        for row in mapdata:
            pass
    def drawTiles(self):
        for rowPos,rowValue in enumerate(self.map):
            for elePos,eleValue in enumerate(rowValue):
                x_position = elePos*config.TileSize.x
                y_position = rowPos*config.TileSize.y
                self.screen.blit(Tiles[eleValue], (x_position,y_position))
