import pygame as py
from config import *

class HeadsUpDisplay:
    def __init__(self,screen:py.Surface) -> None:
        self.screen = screen
    def drawHUD(self,total_time):
        font = py.font.Font(None, 16)
        text = font.render(f"Fps:{round(1/max(total_time,1/FPS))}", True, (255, 255, 255))
        self.screen.blit(text, (10,10))
