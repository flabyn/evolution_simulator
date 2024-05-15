from tiles.Tile import Tile

class EmptyTile(Tile):
    def __init__(self,x,y) -> None:
        super().__init__(x,y)