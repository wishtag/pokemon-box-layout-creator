import os

def find_duplicate_lines(file_path):
    seen_lines = []
    duplicate_lines = []
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip() # Remove any leading/trailing whitespace

            if line in seen_lines:
                duplicate_lines.append(line)
            else:
                seen_lines.append(line)
    
    if duplicate_lines:
        print("Duplicate lines found:")
        for dup in duplicate_lines:
            print(dup)
    else:
        print("No duplicate lines found.")

file_path = os.path.abspath('./text/mons.txt')
find_duplicate_lines(file_path)