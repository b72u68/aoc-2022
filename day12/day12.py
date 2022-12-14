import os
import sys
import copy
from collections import deque


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        raw_data = [line.strip() for line in f.readlines()]

    # process data here
    start = None
    end = None
    map = [[0 for _ in range(len(raw_data[0]))] for _ in range(len(raw_data))]
    for i in range(len(raw_data)):
        for j in range(len(raw_data[i])):
            if raw_data[i][j] == "S":
                map[i][j] = 0
                start = (i, j)
            elif raw_data[i][j] == "E":
                map[i][j] = 25
                end = (i, j)
            else:
                map[i][j] = ord(raw_data[i][j]) - ord("a")
    return (map, start, end)


def bfs(map, start, end):
    rows, cols = len(map), len(map[0])
    q = deque([[start]])
    visited = set([start])
    while q:
        path = q.popleft()
        i, j = path[-1]
        if (i, j) == end:
            return path
        for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
                if map[ni][nj] <= map[i][j] + 1:
                    q.append(path + [(ni, nj)])
                    visited.add((ni, nj))


# solution for part 1
def part1(data):
    map, start, end = copy.deepcopy(data)
    path = bfs(map, start, end)
    return len(path) - 1 if path else None


# solution for part 2
def part2(data):
    map, _, end = copy.deepcopy(data)
    minpath = float('inf')
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                path = bfs(map, (i, j), end)
                if path:
                    minpath = min(minpath, len(path)-1)
    return minpath


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
