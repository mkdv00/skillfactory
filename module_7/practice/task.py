with open("m7-map-1.txt", encoding='utf-8') as map_file_1:
    map_file_lines_1 = map_file_1.readlines()

with open("m7-map-2.txt", encoding='utf-8') as map_file_2:
    map_file_lines_2 = map_file_2.readlines()


map_1 = []
map_2 = []

for elem in map_file_lines_1:
    if elem.find("ID") != -1:
        map_1.append(elem)

for elem in map_file_lines_2:
    if elem.find("ID") != -1:
        map_2.append(elem)
