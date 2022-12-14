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
        x = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    walls.add(x + y * 1j)
                    abyss = max(abyss, y + 1)
    return (walls, abyss)


# solution for part 1
def pprint(map):
    print("\n".join(["".join(line) for line in map]))

def part1(data):
    walls, abyss = copy.deepcopy(data)
    t = 0
    while True:
        s = 500
        while True:
            if s.imag >= abyss:
                return t
            if s + 1j not in walls:
                s += 1j
                continue
            if s + 1j - 1 not in walls:
                s += 1j - 1
                continue
            if s + 1j + 1 not in walls:
                s += 1j + 1
                continue
            walls.add(s)
            t += 1
            break


# solution for part 2
def part2(data):
    walls, abyss = copy.deepcopy(data)
    t = 0
    while 500 not in walls:
        s = 500
        while True:
            if s.imag >= abyss:
                break
            if s + 1j not in walls:
                s += 1j
                continue
            if s + 1j - 1 not in walls:
                s += 1j - 1
                continue
            if s + 1j + 1 not in walls:
                s += 1j + 1
                continue
            break
        walls.add(s)
        t += 1
    return t


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
