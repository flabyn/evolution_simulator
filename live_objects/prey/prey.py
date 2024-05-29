from live_objects.animal import Animal

class Prey(Animal):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
    
