import os
import sys
from collections import deque


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    data = set()
    with open(file_dir, "r") as f:
        for line in f.readlines():
            x, y, z = line.strip().split(",")
            data.add((int(x), int(y), int(z)))
    return data


# solution for part 1
def part1(data):
    result = 0
    for x, y, z in data:
        result += 6
        if (x + 1, y, z) in data:
            result -= 1
        if (x - 1, y, z) in data:
            result -= 1
        if (x, y + 1, z) in data:
            result -= 1
        if (x, y - 1, z) in data:
            result -= 1
        if (x, y, z + 1) in data:
            result -= 1
        if (x, y, z - 1) in data:
            result -= 1
    return result


# solution for part 2
def exposed(x, y, z, data, maxside):
    q = deque([(x, y, z)])
    visited = set()
    while q:
        x, y, z = q.popleft()
        if (x, y, z) in data:
            continue
        if (x, y, z) in visited:
            continue
        if x > maxside or y > maxside or z > maxside:
            return True
        visited.add((x, y, z))
        q.append((x + 1, y, z))
        q.append((x - 1, y, z))
        q.append((x, y + 1, z))
        q.append((x, y - 1, z))
        q.append((x, y, z + 1))
        q.append((x, y, z - 1))
    return False

def part2(data):
    maxside = max(max(data)[0], max(data, key=lambda c: c[1])[1], max(data, key=lambda c: c[2])[2])
    result = 0
    for (x, y, z) in data:
        if exposed(x + 1, y, z, data, maxside):
            result += 1
        if exposed(x - 1, y, z, data, maxside):
            result += 1
        if exposed(x, y + 1, z, data, maxside):
            result += 1
        if exposed(x, y - 1, z, data, maxside):
            result += 1
        if exposed(x, y, z + 1, data, maxside):
            result += 1
        if exposed(x, y, z - 1, data, maxside):
            result += 1
    return result


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
