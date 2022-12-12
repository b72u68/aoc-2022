import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        raw_data = [line.strip() for line in f.readlines()]

    # process data here
    data = []
    for line in raw_data:
        r1, r2 = line.split(",")
        data.append(([int(x) for x in r1.split("-")], [int(x) for x in r2.split("-")]))
    return data


# solution for part 1
def part1(data):
    count = 0
    for r1, r2 in data:
        if r2[0] <= r1[0] <= r1[1] <= r2[1] or r1[0] <= r2[0] <= r2[1] <= r1[1]:
            count += 1
    return count


# solution for part 2
def part2(data):
    count = 0
    for r1, r2 in data:
        if r2[0] <= r1[1] and r1[0] <= r2[1]:
            count += 1
    return count


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
