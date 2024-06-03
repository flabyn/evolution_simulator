from live_objects.animal import Animal

class Prey(Animal):
    def __init__(self, x: int, y: int,resourcemap,groundmap) -> None:
        super().__init__(x, y,resourcemap,groundmap)
    
