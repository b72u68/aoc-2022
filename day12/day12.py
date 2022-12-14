import os
import sys
import copy
from queue import PriorityQueue


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        raw_data = [line.strip() for line in f.readlines()]

    # process data here
    start = None
    end = None
    map = [[0 for _ in range(len(raw_data[0]))] for _ in range(len(raw_data))]
    for i in range(len(raw_data)):
        for j in range(len(raw_data[i])):
            if raw_data[i][j] == "S":
                map[i][j] = 0
                start = (i, j)
            elif raw_data[i][j] == "E":
                map[i][j] = 25
                end = (i, j)
            else:
                map[i][j] = ord(raw_data[i][j]) - ord("a")
    return (map, start, end)


# solution for part 1
def part1(data):
    map, start, end = copy.deepcopy(data)
    return


# solution for part 2
def part2(data):
    return


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
