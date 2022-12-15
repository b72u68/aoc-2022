import os
import sys


# get data from file
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    data = []
    with open(file_dir, "r") as f:
        for line in f.readlines():
            p1, p2 = line.strip().split(": ")
            x1_raw, y1_raw = p1.split(", ")
            x2_raw, y2_raw = p2.split(", ")
            x1 = int(x1_raw.split()[2].split("=")[1])
            y1 = int(y1_raw.split("=")[1])
            x2 = int(x2_raw.split()[4].split("=")[1])
            y2 = int(y2_raw.split("=")[1])
            dis = distance((x1, y1), (x2, y2))
            data.append(((x1, y1), (x2, y2), dis))
    return data


# solution for part 1
def part1(data):
    target = 2000000
    bpos = set()
    for scoord, nbcoord, maxdis in data:
        xs, ys = scoord
        dy = abs(target - ys)
        if dy > maxdis:
            continue
        for dx in range(maxdis - dy + 1):
            if (xs+dx, target) != nbcoord:
                bpos.add((xs+dx, target))
            if (xs-dx, target) != nbcoord:
                bpos.add((xs-dx, target))
    return len(bpos)


# solution for part 2
def valid(x, y, minpos, maxpos, data):
    if not (minpos <= x <= maxpos and minpos <= y <= maxpos):
        return False
    for (scoord, _, maxdis) in data:
        dis = distance(scoord, (x, y))
        if dis <= maxdis:
            return False
    return True

def part2(data):
    minpos = 0
    maxpos = 4000000
    # check all points that are maxdis + 1 from (xs, ys)
    for scoord, _, maxdis in data:
        xs, ys = scoord
        for dx in range(maxdis+1):
            dy = maxdis + 1 - dx
            for stepx, stepy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                x = xs + dx * stepx
                y = ys + dy * stepy
                if valid(x, y, minpos, maxpos, data):
                    return x * 4000000 + y


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
