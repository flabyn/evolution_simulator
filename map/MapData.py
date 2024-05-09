import csv

def map_interpreter():
    opened_map = []
    with open("map\savedmap.csv","r") as file:
        for row in csv.reader(file):
            opened_map.append(list(map(int,row)))
    return opened_map
 
    
