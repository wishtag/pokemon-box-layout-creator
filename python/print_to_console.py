import math

max_length = 19
names = []
im_too_lazy_to_name_variables = float(len(names)/30)
just_a_space = " "
empty = f"[{just_a_space.center(max_length)}] "

with open('mons.txt', 'r') as file:
    for line in file:
        name = f"[{line.strip().center(max_length)}] "
        names.append(name)

im_too_lazy_to_name_variables = math.ceil(float(len(names)/30))
lets_make_another_variable = 0
for something in range(im_too_lazy_to_name_variables):
    idk = (max_length+2)*6+7
    box_name = f"Box {something+1}"
    print("┌", end="")
    for whatever in range(idk):
        print("─", end="")
    print(f"┐\n│{box_name.center(idk)}│\n├", end="")
    for whatever in range(idk):
        print("─", end="")
    print("┤")

    for i in range(30):
        if i == 5 or i == 11 or i == 17 or i == 23:
            try:
                print(f"{names[lets_make_another_variable+i]}│\n│ ", end="")
            except:
                print(f"{empty}│\n│ ", end="")
        elif i == 29:
            try:
                print(f"{names[lets_make_another_variable+i]}│")
            except:
                print(f"{empty}│")
        elif i == 0:
            try:
                print(f"│ {names[lets_make_another_variable+i]}", end="")
            except:
                print(f"│ {empty}", end="")
        else:
            try:
                print(names[lets_make_another_variable+i], end="")
            except:
                print(empty, end="")
    lets_make_another_variable = lets_make_another_variable + 30
    print("└", end="")
    for whatever in range(idk):
        print("─", end="")
    print("┘")