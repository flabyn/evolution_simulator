import pygame as py
from config import *

class HeadsUpDisplay:
    def __init__(self, SScreen = py.Surface) -> None:
        self.screen = SScreen
    def drawHUD(self,frametime):
        self.screen.fill((0,0,0))
        font = py.font.Font(None, 16)
        text = font.render(f"Fps:{round(1/max(frametime,1/FPS))}", True, (255, 255, 255))
        self.screen.blit(text, (10,10))

        font = py.font.Font(None, 16)
        text = font.render(f"Tps:{round(1/max(frametime,1/SIMRATE))}", True, (255, 255, 255))
        self.screen.blit(text, (10,25))



