import os
import sys
from collections import defaultdict


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        raw_data = f.readlines()
    return [line.replace("$", "").strip().split(" ") for line in raw_data]


def folder_sizes(output):
    folders = {}
    path = ['/']
    current_path = ''.join(path)
    folders.setdefault(current_path, 0)

    for line in output:
        if line[0] == "ls":
            continue
        elif line[0] == "dir":
            folders.setdefault(current_path + line[1] + '/', 0)
        elif line[0].isdigit():
            folders[current_path] += int(line[0])
        elif line[0] == "cd":
            if line[1] == "..":
                # Account for subfolder size
                subfolder_size = folders.get(current_path)
                path.pop()
                current_path = ''.join(path)
                folders[current_path] += subfolder_size
            elif line[1] == '/':
                path = [line[1]]
                current_path = ''.join(path)
            else:
                path.append(line[1] + '/')
                current_path = ''.join(path)

    # Add folder size for any remaining folders in stack
    for n in range(len(path) - 1):
        subfolder_size = folders.get(current_path)
        path.pop()
        current_path = ''.join(path)
        folders[current_path] += subfolder_size

    return folders


# solution for part 1
def part1(data):
    dirs = folder_sizes(data[1:])
    return sum(v for v in dirs.values() if v <= 100000)


# solution for part 2
def part2(data):
    dirs = folder_sizes(data[1:])
    total = 70000000
    space_needed = 30000000
    space_used = dirs.get('/')
    unused_space = total - space_used
    return min(v for v in dirs.values() if v > (space_needed - unused_space))


if __name__ == "__main__":

    filename = "data.txt"

    if len(sys.argv) >= 2:
        filename = sys.argv[1]

    try:
        data = get_data(filename)
        print(part1(data))
        print(part2(data))

    except Exception as e:
        print(e)
