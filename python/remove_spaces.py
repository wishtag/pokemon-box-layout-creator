import os

try:
    with open(os.path.abspath('./text/mons.txt'), 'r') as file:
        lines = file.readlines()

    with open(os.path.abspath('./text/mons.txt'), 'w') as file:
        for line in lines:
            file.write(line.rstrip() + '\n')  # removes trailing spaces
except: #this triggers if its running through a batch file
    with open(os.path.abspath('../text/mons.txt'), 'r') as file:
        lines = file.readlines()

    with open(os.path.abspath('../text/mons.txt'), 'w') as file:
        for line in lines:
            file.write(line.rstrip() + '\n')  # removes trailing spaces