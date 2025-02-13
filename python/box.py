import math
import os
import json

with open(os.path.abspath('./settings.json'), 'r') as file:
    settings = json.loads(file.read())

max_length = 19
names = []
pokemon_index = 0
empty = " "
empty = f"[{empty.center(max_length)}] "

with open(os.path.abspath('./text/mons.txt'), 'r') as file:
    for line in file:
        name = f"[{line.strip().center(max_length)}] "
        names.append(name)
            
f = open(os.path.abspath('./text/box.txt'), 'w')
f.write("")
f.close()

total_boxes = math.ceil(float(len(names)/30))

f = open(os.path.abspath('./text/box.txt'), 'a', encoding='utf-8')
for current_box in range(1,total_boxes+1):

    # max_length is how many characters a pokemons name can be
    # the "+2" is to represent the two brackets, [], at the start and end of a pokemons name
    # the "*6" is to represent how many pokemon can be in one row
    # the "+7" is the additional spaces in between the start and end of each pokemons name
    line_length = (max_length+2)*6+7
    box_name = f"Box {current_box}"
    f.write("┌")
    for i in range(line_length):
        f.write("─")
    f.write(f"┐\n│{box_name.center(line_length)}│\n├")
    for i in range(line_length):
        f.write("─")
    f.write("┤\n")

    for i in range(30):
        if i == 5 or i == 11 or i == 17 or i == 23:
            try:
                f.write(f"{names[pokemon_index+i]}│\n│ ")
            except:
                f.write(f"{empty}│\n│ ")
        elif i == 29:
            try:
                f.write(f"{names[pokemon_index+i]}│\n")
            except:
                f.write(f"{empty}│\n")
        elif i == 0:
            try:
                f.write(f"│ {names[pokemon_index+i]}")
            except:
                f.write(f"│ {empty}")
        else:
            try:
                f.write(names[pokemon_index+i])
            except:
                f.write(empty)
    pokemon_index = pokemon_index + 30
    f.write("└")
    for i in range(line_length):
        f.write("─")
    f.write("┘\n")

if settings["open_when_done"]:
    os.startfile(os.path.abspath('./text/box.txt'))