from config import *
import time
from Matrix import Map_Matrix
import map.MapData as MapData
import pygame as py
from HUD import HeadsUpDisplay

py.init()
Screen = py.display.set_mode((ScreenSize.width,ScreenSize.height))

def main():
    mapdata = MapData.map_interpreter()
    MapMatrix = Map_Matrix(mapdata=mapdata,screen=Screen)
    HUD = HeadsUpDisplay(Screen)
    while True:
        start = time.time() #start frame timer
        Screen.fill((0,0,0))
        MapMatrix.drawTiles()

        end = time.time() #end frame timer
        total_time = (end-start)
        HUD.drawHUD(total_time)
        time.sleep(max(0,(1/FPS)-total_time))

        py.display.flip() #update display









if __name__ == "__main__":
    main()