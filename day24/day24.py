import os
import sys
import copy


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    board = {}
    height = len(lines) - 2
    width = len(lines[0]) - 2
    for i in range(len(lines)):
        for j, c in enumerate(lines[i].strip()):
            if c == ">":
                board[(i-1, j-1)] = [(0, 1)]
            elif c == "<":
                board[(i-1, j-1)] = [(0, -1)]
            elif c == "^":
                board[(i-1, j-1)] = [(-1, 0)]
            elif c == "v":
                board[(i-1, j-1)] = [(1, 0)]
    return board, width, height


def cycle(board, width, height):
    new_board = {}
    for (i, j), dirs in board.items():
        for di, dj in dirs:
            ni, nj = (i + di) % height, (j + dj) % width
            if (ni, nj) not in new_board:
                new_board[(ni, nj)] = []
            new_board[(ni, nj)].append((di, dj))
    return new_board


def get_neighbors(coord, board, width, height):
    neighbors = []
    dirs = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    start, end = (-1, 0), (height, width-1)
    i, j = coord
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if (ni, nj) in board:
            continue
        if (ni, nj) in (start, end) \
                or (0 <= ni < height and 0 <= nj < width):
            neighbors.append((ni, nj))
    return neighbors


def bfs(start, end, board, width, height):
    moves = 0
    q = [(start.pop(0))]
    while True:
        board = cycle(board, width, height)
        moves += 1
        next_q = set()
        while q:
            coord = q.pop(0)
            if coord == end[0]:
                end.pop(0)
                if start:
                    next_q = {start.pop(0)}
                    break
                else:
                    return moves - 1
            next_q.update(get_neighbors(coord, board, width, height))
        q = list(next_q)


# solution for part 1
def part1(data):
    board, width, height = copy.deepcopy(data)
    start, end = (-1, 0), (height, width-1)
    return bfs([start], [end], board, width, height)


# solution for part 2
def part2(data):
    board, width, height = copy.deepcopy(data)
    start, end = (-1, 0), (height, width-1)
    return bfs([start, end, start], [end, start, end], board, width, height)


if __name__ == "__main__":

    filename = "data.txt"

    if len(sys.argv) >= 2:
        filename = sys.argv[1]

    data = get_data(filename)
    print(part1(data))
    print(part2(data))
