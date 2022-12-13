import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        raw_data = f.readlines()
    return [[int(x) for x in list(line.strip())] for line in raw_data]


# solution for part 1
def visible_left(data, i, j):
    for jj in range(j):
        if data[i][jj] >= data[i][j]:
            return False
    return True

def visible_right(data, i, j):
    for jj in range(j+1, len(data[0])):
        if data[i][jj] >= data[i][j]:
            return False
    return True

def visible_up(data, i, j):
    for ii in range(i):
        if data[ii][j] >= data[i][j]:
            return False
    return True

def visible_down(data, i, j):
    for ii in range(i+1, len(data)):
        if data[ii][j] >= data[i][j]:
            return False
    return True

def part1(data):
    rows, cols = len(data), len(data[0])
    count = rows * 2 + cols * 2 - 4
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if visible_left(data, i, j) or visible_right(data, i, j) \
                    or visible_up(data, i, j) or visible_down(data, i, j):
                        count += 1
    return count


# solution for part 2
def scenic_left(data, i, j):
    score = 0
    for jj in range(j-1, -1, -1):
        if data[i][jj] >= data[i][j]:
            score += 1
            break
        score += 1
    return score

def scenic_right(data, i, j):
    score = 0
    for jj in range(j+1, len(data[0])):
        if data[i][jj] >= data[i][j]:
            score += 1
            break
        score += 1
    return score

def scenic_up(data, i, j):
    score = 0
    for ii in range(i-1, -1, -1):
        if data[ii][j] >= data[i][j]:
            score += 1
            break
        score += 1
    return score

def scenic_down(data, i, j):
    score = 0
    for ii in range(i+1, len(data)):
        if data[ii][j] >= data[i][j]:
            score += 1
            break
        score += 1
    return score

def part2(data):
    rows, cols = len(data), len(data[0])
    score = float("-inf")
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            curscore = scenic_left(data, i, j) * scenic_right(data, i, j) \
                    * scenic_up(data,i ,j) * scenic_down(data, i, j)
            score = max(curscore, score)
    return score


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
