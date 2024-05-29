import csv

map_location = {"ground":"map\groundmap.csv","resource":"map/resourcemap.csv","animal":"map/animal.csv"}

def map_interpreter(type):
    opened_map = []
    with open(map_location[type],"r") as file:
        for row in csv.reader(file):
            opened_map.append(list(map(int,row)))
    return opened_map
 
    
