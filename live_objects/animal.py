from MatrixObject import MatrixObject

class Animal(MatrixObject):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def move(self):
        pass