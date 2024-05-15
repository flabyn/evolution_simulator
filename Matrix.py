import pygame as py
from config import *
from tiles.TileType import TileType

class Map_Matrix:
    def __init__(self,mapdata,screen) -> None:
        self.map = self.generateClassMatrix(mapdata)
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
    def drawClassTiles(self):
        for row in self.map:
            for tile in row:
                tile.drawSelf(self.screen)
                #self.screen.blit(tile.image, (tile.x*TileSize.x,tile.y*TileSize.y))
    def stepClassTiles(self):
        for row in self.map:
            for tile in row:
                tile.step()