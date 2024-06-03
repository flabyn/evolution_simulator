import pygame as py
from config import *
from tiles.TileType import TileType

class Map_Matrix:
    def __init__(self,mapdata,screen,map1=None,map2=None) -> None:
        self.othermaps = [map1,map2]
        self.map = self.generateClassMatrix(mapdata)
        self.screen:py.Surface = screen
    def generateClassMatrix(self,mapdata) -> list[list]:
        classMatrix = []
        for row_pos,row in enumerate(mapdata):
            rowmap = []
            for tile_pos,tile in enumerate(row):
                TILE = TileType(tile)
                rowmap.append(TILE.MatrixCreateElement(tile_pos,row_pos,resourcemap=self.othermaps[0],groundmap=self.othermaps[1]))
            classMatrix.append(rowmap)
        return classMatrix
    def tileAtPos(self,x,y):
        return self.map[y][x]
    def drawClassTiles(self):
        for row in self.map:
            for tile in row:
                tile.drawSelf(self.screen)
                #self.screen.blit(tile.image, (tile.x*TileSize.x,tile.y*TileSize.y))
    def stepClassTiles(self):
        for row in self.map:
            for tile in row:
                tile.step(self)
    def swapTiles(self,pos1,pos2):
        tile1 = self.map[pos1[1]][pos1[0]]
        tile2 = self.map[pos2[1]][pos2[0]]

        self.map[pos1[1]][pos1[0]].x = pos2[0]
        self.map[pos1[1]][pos1[0]].y = pos2[1]
        self.map[pos2[1]][pos2[0]].x = pos1[0]
        self.map[pos2[1]][pos2[0]].y = pos1[1]

        self.map[pos2[1]][pos2[0]] = tile1
        self.map[pos1[1]][pos1[0]] = tile2
    def tileMove(self,pos1,direction):
        self.swapTiles(pos1,[pos1[0]+direction[0],pos1[1]+direction[1]])
