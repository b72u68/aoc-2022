import os
import sys
import copy
import re


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    board = []
    path = ""
    maxrow = 0
    with open(file_dir, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.strip() == "":
                path = re.findall(r"\d+|R|L", lines[i+1].strip())
                break
            row = list(line.strip("\n"))
            maxrow = max(maxrow, len(row))
            board.append(list(line.strip("\n")))
    for i, row in enumerate(board):
        board[i] = board[i] + [' ' for _ in range(maxrow - len(row))]
    return board, path


# solution for part 1
def pprint(board):
    print("\n".join(["".join(row) for row in board]))

def part1(data):
    board, path = copy.deepcopy(data)
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    moveidx = 0
    curcoord = (0, 0)
    for y in range(len(board)):
        found = False
        for x in range(len(board[y])):
            if board[y][x] == ".":
                curcoord = (x, y)
                found = True
                break
        if found:
            break
    for p in path:
        if p.isnumeric():
            dx, dy = moves[moveidx]
            for _ in range(int(p)):
                x, y = curcoord
                nx = (x + dx) % len(board[y])
                ny = (y + dy) % len(board)
                while board[ny][nx] == " " and dx:
                    nx = (nx + dx) % len(board[y])
                while board[ny][nx] == " " and dy:
                    ny = (ny + dy) % len(board)
                if board[ny][nx] == ".":
                    curcoord = (nx, ny)
                elif board[ny][nx] == "#":
                    break
        elif p == "L":
            moveidx = (moveidx - 1) % len(moves)
        else:
            moveidx = (moveidx + 1) % len(moves)
    return 1000 * (curcoord[1] + 1) + 4 * (curcoord[0] + 1) + moveidx


# solution for part 2
def part2(data):
    board, path = copy.deepcopy(data)
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
