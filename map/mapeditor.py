#used for editing the map no run time processes

import csv
opened_map = []

MatrixSize = [25,25]

maptype = "resource"
map_location = {"ground":"map\groundmap.csv","resource":"map/resourcemap.csv"}

with open(map_location[maptype],"r") as file:
        for row in csv.reader(file):
            opened_map.append(list(map(int,row)))
print(opened_map)

def create_new_map(default_tile=0) -> list[list]:
    new_map = []
    for y in range(MatrixSize[1]):
        row_list = []
        for x in range(MatrixSize[0]):
            row_list.append(default_tile)
        new_map.append(row_list)
    with open(map_location[maptype],"w") as mapFile:
        writer = csv.writer(mapFile,lineterminator="\n")
        writer.writerows(new_map)
        mapFile.close()

create_new_map()
