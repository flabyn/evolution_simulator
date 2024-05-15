from enum import Enum

from tiles.Tile import Tile
from tiles.EmptyTile import EmptyTile
from tiles.Ground.Grass import Grass
from tiles.Ground.Water import Water
from tiles.Resource.Fruit import Fruit
class TileType(Enum):
    EMPTY = 0
    GRASS = 1
    WATER = 2
    FRUIT = 3

    def MatrixCreateElement(self,x:int=1,y:int=1) -> Tile:
        match self:
            case TileType.EMPTY:
                cell = EmptyTile(x,y)
                return cell
            case TileType.GRASS:
                cell = Grass(x,y)
                return cell
            case TileType.WATER:
                cell = Water(x,y)
                return cell
            
            case TileType.FRUIT:
                cell = Fruit(x,y)
                return cell
            