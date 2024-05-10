from enum import Enum

from tiles.Tile import Tile
from tiles.Ground.Grass import Grass

class ElementType(Enum):
    GRASS = 0
    WATER = 1

    def MatrixCreateElement(self,x:int=1,y:int=1) -> Tile:
        match self:
            case ElementType.GRASS:
                cell = Grass(x,y)
                return cell