from enum import Enum

from tiles.Tile import Tile
from tiles.Ground.Grass import Grass
from tiles.Ground.Water import Water

class TileType(Enum):
    OTHER = -1
    GRASS = 0
    WATER = 1

    def MatrixCreateElement(self,x:int=1,y:int=1) -> Tile:
        match self:
            case TileType.GRASS:
                cell = Grass(x,y)
                return cell
            case TileType.WATER:
                cell = Water(x,y)
                return cell