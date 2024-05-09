import csv
import config
opened_map = []

with open("savedmap.csv","r") as file:
        for row in csv.reader(file):
            opened_map.append(list(map(int,row)))
print(opened_map)

def create_new_map(default_tile=0) -> list[list]:
    new_map = []
    for y in range(config.MatrixSize.y):
        row_list = []
        for x in range(config.MatrixSize.x):
            row_list.append(default_tile)
        new_map.append(row_list)
    with open("savedmap.csv","w") as mapFile:
        writer = csv.writer(mapFile,lineterminator="\n")
        writer.writerows(new_map)
        mapFile.close()

create_new_map()
