import csv

def map_interpreter():
    opened_map = []
    with open("savedmap.csv","r") as file:
        for row in csv.reader(file):
            opened_map.append(list(map(int,row)))
    print(opened_map)

map_interpreter()
#
#def map_creator():
    
