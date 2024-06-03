from MatrixObject import MatrixObject
import random

class Animal(MatrixObject):
    def __init__(self, x: int, y: int,resourcemap,groundmap) -> None:
        super().__init__(x, y)
        self.resourceMap = resourcemap 
        self.groundMap = groundmap
        self.movefreqent = 1.0

    def step(self,Matrix):
        if random.random() < self.movefreqent:
            self.move(Matrix)

    def move(self,Matrix):
        travelDir = self.travelCheck()
        Matrix.tileMove((self.x,self.y),travelDir)
    def travelCheck(self)-> tuple[int]:
        #create dict of neighbouring tiles
        tiles = {"N":(0,-1),"E":(1,0),"S":(0,1),"W":(-1,0)}
        #check if neighbouring tiles can be walked on
        walkable = []
        for dir in tiles.values():
            if self.groundMap.tileAtPos(self.x+dir[0],self.y+dir[1]).walkable:
                walkable.append(dir)
        #return a random walkable position
        return random.choice(walkable)




        