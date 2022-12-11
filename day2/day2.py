import argparse
import os


parser = argparse.ArgumentParser("aoc")
parser.add_argument('-t', '--test', help='run program using test data', action='store_true')
args = parser.parse_args()


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    # process data here
    raw_data = f.readlines()
    f.close()

    return [x.strip().split(" ") for x in raw_data]


# solution for part 1
def part1(data):
    points = 0
    shapes = [1, 2, 3]
    outcomes = [3, 6, 0]
    for p1, p2 in data:
        p1_move = ord(p1) - ord("A")
        p2_move = ord(p2) - ord("X")
        points += shapes[p2_move] + outcomes[(p2_move - p1_move + 3) % 3]
    return points


# solution for part 2
def part2(data):
    points = 0
    shapes = [1, 2, 3]
    outcomes = [0, 3, 6]
    for p1, p2 in data:
        p1_move = ord(p1) - ord("A")
        p2_move = ord(p2) - ord("X")
        points += outcomes[p2_move] + shapes[(p1_move + p2_move - 1) % 3]
    return points


if __name__ == "__main__":

    if args.test:
        filename = "test.txt"
    else:
        filename = "data.txt"

    try:
        data = get_data(filename)
        print(part1(data))
        print(part2(data))

    except Exception as e:
        print(e)
