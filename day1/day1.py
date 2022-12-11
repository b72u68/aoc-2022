import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    # process data here
    raw_data = f.readlines()

    return [x.strip() for x in raw_data]


# solution for part 1
def part1(data):
    calories = []
    currsum = 0
    for i in range(len(data)):
        if data[i] == "":
            calories.append(currsum)
            currsum = 0
        else:
            currsum += int(data[i])
    return max(calories)


# solution for part 2
def part2(data):
    calories = []
    currsum = 0
    for i in range(len(data)):
        if data[i] == "":
            calories.append(currsum)
            currsum = 0
        else:
            currsum += int(data[i])
    return sum(sorted(calories)[-3:])


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
