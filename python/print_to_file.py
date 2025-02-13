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

f = open("formatted.txt", "w")
f.write("")
f.close()

im_too_lazy_to_name_variables = math.ceil(float(len(names)/30))
lets_make_another_variable = 0

f = open("formatted.txt", "a", encoding='utf-8')
for something in range(im_too_lazy_to_name_variables):

    idk = (max_length+2)*6+7
    box_name = f"Box {something+1}"
    f.write("┌")
    for whatever in range(idk):
        f.write("─")
    f.write(f"┐\n│{box_name.center(idk)}│\n├")
    for whatever in range(idk):
        f.write("─")
    f.write("┤\n")

    for i in range(30):
        if i == 5 or i == 11 or i == 17 or i == 23:
            try:
                f.write(f"{names[lets_make_another_variable+i]}│\n│ ")
            except:
                f.write(f"{empty}│\n│ ")
        elif i == 29:
            try:
                f.write(f"{names[lets_make_another_variable+i]}│\n")
            except:
                f.write(f"{empty}│\n")
        elif i == 0:
            try:
                f.write(f"│ {names[lets_make_another_variable+i]}")
            except:
                f.write(f"│ {empty}")
        else:
            try:
                f.write(names[lets_make_another_variable+i])
            except:
                f.write(empty)
    lets_make_another_variable = lets_make_another_variable + 30
    f.write("└")
    for whatever in range(idk):
        f.write("─")
    f.write("┘\n")