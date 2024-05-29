from config import *
import time
from Matrix import Map_Matrix
import map.MapData as MapData
import pygame as py
from HUD import HeadsUpDisplay

py.init()
Screen = py.display.set_mode((ScreenSize.width,ScreenSize.height+HUDScreen.height))
GameScreen = py.Surface((ScreenSize.width,ScreenSize.height))
HUDScreen = py.Surface((ScreenSize.width,HUDScreen.height))

def main():
    mapdata = MapData.map_interpreter("ground")
    GroundMatrix = Map_Matrix(mapdata=mapdata,screen=GameScreen) #bottom layer matrix
    mapdata = MapData.map_interpreter("resource")
    ResourceMatrix = Map_Matrix(mapdata=mapdata,screen=GameScreen)
    mapdata = MapData.map_interpreter("animal")
    AnimalMatrix = Map_Matrix(mapdata=mapdata,screen=GameScreen)
    HUD = HeadsUpDisplay(HUDScreen)

    FPSTimer = 0
    SIMTimer = 0
    while True:
        start = time.time() #start timer

        if SIMTimer <= 0:
            ResourceMatrix.stepClassTiles()
            AnimalMatrix.stepClassTiles()
            SIMTimer = 1/SIMRATE


        if FPSTimer <= 0:
            GameScreen.fill((0,0,0))
            GroundMatrix.drawClassTiles()
            ResourceMatrix.drawClassTiles()
            AnimalMatrix.drawClassTiles()
            FPSTimer = 1/FPS




        time.sleep(0.001)
        end = time.time() #end timer
        total_time = (end-start)

        HUD.drawHUD(total_time)

        Screen.blit(GameScreen, (0,0))
        Screen.blit(HUDScreen, (0,ScreenSize.height))
        #decrease timers by loop time (run time)
        FPSTimer-=total_time
        SIMTimer-=total_time

        py.display.flip() #update display


if __name__ == "__main__":
    main()