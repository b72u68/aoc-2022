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
    ## test data
    # width = 4
    # bordermap = {
            # # up, right, down, left
            # 1: [(2, "U"), (6, "R"), (4, "U"), (3, "U")],
            # 2: [(1, "U"), (3, "L"), (5, "D"), (6, "D")],
            # 3: [(1, "L"), (4, "L"), (5, "L"), (2, "R")],
            # 4: [(1, "D"), (6, "U"), (5, "U"), (3, "R")],
            # 5: [(4, "D"), (6, "L"), (2, "D"), (3, "D")],
            # 6: [(4, "R"), (1, "R"), (2, "L"), (5, "R")]
    # }
    width = 50
    bordermap = {
            # up, right, down, left
            1: [(6, "L"), (2, "L"), (3, "U"), (4, "L")],
            2: [(6, "D"), (5, "R"), (3, "R"), (1, "R")],
            3: [(1, "D"), (2, "D"), (5, "U"), (4, "U")],
            4: [(3, "L"), (5, "L"), (6, "U"), (1, "L")],
            5: [(3, "D"), (2, "R"), (6, "R"), (4, "R")],
            6: [(4, "D"), (5, "D"), (2, "U"), (1, "U")]
    }
    board, path = copy.deepcopy(data)
    board_id = 1
    boardmap = {}
    for y in range(0, len(board), width):
        for x in range(0, len(board[y]), width):
            if board[y][x] == " ":
                continue
            boardmap[board_id] = [board[yy][x:x+width] for yy in range(y, y+width)]
            board_id += 1
    # right, down, left, up
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    moveidx = 0
    curcoord = (0, 0)
    curboard_id = 1
    for p in path:
        if p.isnumeric():
            for _ in range(int(p)):
                curboard = boardmap[curboard_id]
                dx, dy = moves[moveidx]
                x, y = curcoord
                nextboard_id = curboard_id
                nmoveidx = moveidx
                nx = x + dx
                ny = y + dy
                if 0 <= ny < len(curboard):
                    if nx >= len(curboard[ny]):
                        nextboard_id, border = bordermap[curboard_id][1]
                        if border == "L":
                            nx, ny = 0, ny
                        elif border == "R":
                            nx, ny = width - 1, width - 1 - ny
                            nmoveidx = 2
                        elif border == "U":
                            nx, ny = width - 1 - ny, 0
                            nmoveidx = 1
                        else:
                            nx, ny = ny, width - 1
                            nmoveidx = 3
                    elif nx < 0:
                        nextboard_id, border = bordermap[curboard_id][3]
                        if border == "L":
                            nx, ny = 0, width - 1 - ny
                            nmoveidx = 0
                        elif border == "R":
                            nx, ny = width - 1, ny
                        elif border == "U":
                            nx, ny = ny, 0
                            nmoveidx = 1
                        else:
                            nx, ny = width - 1 - ny, width - 1
                            nmoveidx = 3
                elif ny < 0:
                    nextboard_id, border = bordermap[curboard_id][0]
                    if border == "L":
                        nx, ny = 0, nx
                        nmoveidx = 0
                    elif border == "R":
                        nx, ny = width - 1, width - 1 - nx
                        nmoveidx = 2
                    elif border == "U":
                        nx, ny = width - 1 - nx, 0
                        nmoveidx = 1
                    else:
                        nx, ny = nx, width - 1
                else:
                    nextboard_id, border = bordermap[curboard_id][2]
                    if border == "L":
                        nx, ny = 0, width - 1 - nx
                        nmoveidx = 0
                    elif border == "R":
                        nx, ny = width - 1, nx
                        nmoveidx = 2
                    elif border == "U":
                        nx, ny = nx, 0
                    else:
                        nx, ny = width - 1 - nx, width - 1
                        nmoveidx = 3
                if boardmap[nextboard_id][ny][nx] == ".":
                    curcoord = (nx, ny)
                    curboard_id = nextboard_id
                    moveidx = nmoveidx
                elif boardmap[nextboard_id][ny][nx] == "#":
                    break
        elif p == "L":
            moveidx = (moveidx - 1) % len(moves)
        else:
            moveidx = (moveidx + 1) % len(moves)
    # answer: 123149
    return (curboard_id, curcoord, moveidx)


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
