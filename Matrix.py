import pygame as py
from config import *
from tiles.TileType import TileType

Tiles = {0:py.image.load("assets\grass.png"),1:py.image.load("assets\water.png")}

class Map_Matrix:
    def __init__(self,mapdata,screen) -> None:
        self.map = self.generateClassMatrix(mapdata)
        print(self.map)
        self.screen:py.Surface = screen
    def generateClassMatrix(self,mapdata):
        classMatrix = []
        for row_pos,row in enumerate(mapdata):
            rowmap = []
            for tile_pos,tile in enumerate(row):
                TILE = TileType(tile)
                rowmap.append(TILE.MatrixCreateElement(tile_pos,row_pos))
            classMatrix.append(rowmap)
        print("here")
        return classMatrix
    def drawTiles(self):
        for rowPos,rowValue in enumerate(self.map):
            for elePos,eleValue in enumerate(rowValue):
                x_position = elePos*TileSize.x
                y_position = rowPos*TileSize.y
                self.screen.blit(Tiles[eleValue], (x_position,y_position))
    def drawClassTiles(self):
        for row in self.map:
            for tile in row:
                self.screen.blit(tile.image, (tile.x*TileSize.x,tile.y*TileSize.y))