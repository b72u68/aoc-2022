import os
import sys
import copy
from collections import defaultdict


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        board = [list(line.strip()) for line in f.readlines()]
    elves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "#":
                elves.append((i, j))
    return elves

# solution for part 1
def pprint(elves):
    minwidth, maxwidth = min(elves, key=lambda e: e[1])[1], max(elves, key=lambda e: e[1])[1]
    minheight, maxheight = min(elves, key=lambda e: e[0])[0], max(elves, key=lambda e: e[0])[0]
    board = [["." for _ in range(minwidth, maxwidth+1)] for _ in range(minheight, maxheight+1)]
    for ei, ej in elves:
        board[ei-minheight][ej-minwidth] = "#"
    print("\n".join(["".join(row) for row in board]))
    print()

def north(elves, ei, ej):
    if (ei-1, ej) not in elves and (ei-1, ej+1) not in elves \
            and (ei-1, ej-1) not in elves:
        return (ei-1, ej)
    return None

def south(elves, ei, ej):
    if (ei+1, ej) not in elves and (ei+1, ej+1) not in elves \
            and (ei+1, ej-1) not in elves:
        return (ei+1, ej)
    return None

def west(elves, ei, ej):
    if (ei, ej-1) not in elves and (ei+1, ej-1) not in elves \
            and (ei-1, ej-1) not in elves:
        return (ei, ej-1)
    return None

def east(elves, ei, ej):
    if (ei, ej+1) not in elves and (ei+1, ej+1) not in elves \
            and (ei-1, ej+1) not in elves:
        return (ei, ej+1)
    return None

def part1(data):
    elves = copy.deepcopy(data)
    checks = [north, south, west, east]
    minwidth, maxwidth = len(elves[0]), 0
    minheight, maxheight = len(elves), 0
    for _ in range(10):
        moves = defaultdict(list)
        for i, (ei, ej) in enumerate(elves):
            if (ei, ej+1) not in elves and (ei, ej-1) not in elves \
                    and (ei+1, ej) not in elves and (ei+1, ej-1) not in elves \
                    and (ei+1, ej+1) not in elves and (ei-1, ej) not in elves \
                    and (ei-1, ej-1) not in elves and (ei-1, ej+1) not in elves:
                moves[(ei, ej)].append(i)
                continue
            for check in checks:
                next_move = check(elves, ei, ej)
                if next_move:
                    moves[next_move].append(i)
                    break
        for (ei, ej), v in moves.items():
            if len(v) > 1:
                continue
            for idx in v:
                elves[idx] = (ei, ej)
            minwidth, maxwidth = min(minwidth, ej), max(maxwidth, ej)
            minheight, maxheight = min(minheight, ei), max(maxheight, ei)
        checks.append(checks.pop(0))
    return (maxwidth - minwidth + 1) * (maxheight - minheight + 1) - len(elves)


# solution for part 2
def part2(data):
    elves = copy.deepcopy(data)
    checks = [north, south, west, east]
    r = 1
    while True:
        no_change = True
        moves = defaultdict(list)
        for i, (ei, ej) in enumerate(elves):
            if (ei, ej+1) not in elves and (ei, ej-1) not in elves \
                    and (ei+1, ej) not in elves and (ei+1, ej-1) not in elves \
                    and (ei+1, ej+1) not in elves and (ei-1, ej) not in elves \
                    and (ei-1, ej-1) not in elves and (ei-1, ej+1) not in elves:
                moves[(ei, ej)].append(i)
                continue
            for check in checks:
                next_move = check(elves, ei, ej)
                if next_move:
                    moves[next_move].append(i)
                    break
        for (ei, ej), v in moves.items():
            if len(v) > 1:
                continue
            for idx in v:
                if (ei, ej) != elves[idx]:
                    no_change = False
                elves[idx] = (ei, ej)
        checks.append(checks.pop(0))
        if no_change:
            return r
        r += 1


if __name__ == "__main__":

    filename = "data.txt"

    if len(sys.argv) >= 2:
        filename = sys.argv[1]

    try:
        data = get_data(filename)
        # print(part1(data))
        print(part2(data))

    except Exception as e:
        print(e)
