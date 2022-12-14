import os
import sys
import copy


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        raw_data = [line.strip() for line in f.readlines()]

    # process data here
    abyss = 0
    walls = set()
    for line in raw_data:
        x = [list(map(int, p.split(","))) for p in line.split(" -> ")]
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    walls.add((x, y))
                    abyss = max(abyss, y + 1)
    return (walls, abyss)


# solution for part 1
def part1(data):
    walls, abyss = copy.deepcopy(data)
    count = 0
    while True:
        x = 500
        y = 0
        while True:
            if y >= abyss:
                return count
            if (x, y + 1) not in walls:
                y += 1
                continue
            if (x-1, y+1) not in walls:
                x -= 1
                y += 1
                continue
            if (x+1, y+1) not in walls:
                x += 1
                y += 1
                continue
            walls.add((x, y))
            count += 1
            break


# solution for part 2
def part2(data):
    walls, abyss = copy.deepcopy(data)
    count = 0
    while (500, 0) not in walls:
        x = 500
        y = 0
        while True:
            if y >= abyss:
                break
            if (x, y + 1) not in walls:
                y += 1
                continue
            if (x-1, y+1) not in walls:
                x -= 1
                y += 1
                continue
            if (x+1, y+1) not in walls:
                x += 1
                y += 1
                continue
            break
        walls.add((x, y))
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
