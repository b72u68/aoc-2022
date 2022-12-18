import os
import sys
import copy


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
         return f.readlines()[0].strip()


rockshapes = [
        [(1, 0), (2, 0), (3, 0), (4, 0)],           # -
        [(3, 2), (2, 1), (3, 1), (4, 1), (3, 0)],   # +
        [(2, 2), (2, 1), (2, 0), (3, 0), (4, 0)],   # L
        [(4, 0), (4, 1), (4, 2), (4, 3)],           # |
        [(3, 0), (4, 0), (3, 1), (4, 1)]            # square
    ]


# solution for part 1
def pprint(rocks):
    maxheight = max(rocks, key=lambda c: c[1])[1]
    map = [["." for _ in range(7)] for _ in range(maxheight+1)]
    for x, y in rocks:
        if y == -1:
            continue
        map[y][x] = "#"
    print("\n".join(["".join(row) for row in map]))

def down_coords(shape):
    return [(x, y - 1) for x, y in shape]

def right_coords(shape):
    return [(x - 1, y) for x, y in shape]

def left_coords(shape):
    return [(x + 1, y) for x, y in shape]

def simulation(jetstream, numrocks):
    rocks = set([(x, -1) for x in range(7)])
    count = 0
    wi = 0
    maxwidth = 6
    while count < numrocks:
        # relocate rocks
        maxheight = max(rocks, key=lambda c: c[1])[1]
        cur = [(x, y + maxheight + 4) for x, y in rockshapes[count % len(rockshapes)]]
        while True:
            x_min, x_max = min(cur)[0], max(cur)[0]
            # wind
            if jetstream[wi] == ">":
                right = right_coords(cur)
                if x_min > 0 and not set(right).intersection(rocks):
                    cur = right
            else:
                left = left_coords(cur)
                if x_max < maxwidth and not set(left).intersection(rocks):
                    cur = left
            wi = (wi + 1) % len(jetstream)
            # fall
            down = down_coords(cur)
            if set(down).intersection(rocks):
                for coord in cur:
                    rocks.add(coord)
                break
            cur = down
        count += 1
    return max(rocks, key=lambda c: c[1])[1] + 1


def part1(data):
    return simulation(data, 2022)


# solution for part 2
def part2(data):
    # return simulation(data, 1000000000000)
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
