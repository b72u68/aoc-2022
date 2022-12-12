import os
import sys
import copy
from collections import defaultdict


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        raw_data = f.readlines()

    # process data here
    stacks = defaultdict(list)
    moves = []
    i = 0

    while i < len(raw_data):
        line = raw_data[i]
        curstack = 1
        ptr = 0
        while ptr < len(line) and ptr + 3 < len(line):
            if line[ptr+1] == " ":
                pass
            elif line[ptr+1].isnumeric():
                pass
            else:
                stacks[curstack] = [line[ptr+1]] + stacks[curstack]
            ptr += 4
            curstack += 1
        if line.strip() == "":
            i += 1
            break
        i += 1

    while i < len(raw_data):
        line = raw_data[i]
        sline = line.split(" ")
        moves.append((int(sline[1]), int(sline[3]), int(sline[5])))
        i += 1

    return (stacks, moves)


# solution for part 1
def part1(data):
    stacks, moves = copy.deepcopy(data)
    for n, s1, s2 in moves:
        for _ in range(n):
            stacks[s2].append(stacks[s1].pop())
    return "".join([stacks[k][-1] for k in sorted(stacks.keys())])


# solution for part 2
def part2(data):
    stacks, moves = copy.deepcopy(data)
    for n, s1, s2 in moves:
        block = stacks[s1][-n:]
        stacks[s1] = stacks[s1][:-n]
        stacks[s2] = stacks[s2] + block
    return "".join([stacks[k][-1] for k in sorted(stacks.keys())])


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
