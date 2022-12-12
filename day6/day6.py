import os
import sys
from collections import defaultdict


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        raw_data = f.readlines()
    return raw_data[0].strip()


# solution for part 1
def part1(data):
    for i in range(len(data)-4):
        packet = data[i:i+4]
        if len(set(packet)) == len(packet):
            return i + 4


# solution for part 2
def part2(data):
    for i in range(len(data)-14):
        packet = data[i:i+14]
        if len(set(packet)) == len(packet):
            return i + 14


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
