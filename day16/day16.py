import os
import sys
import re


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    nodemap = {}
    pressuremap = {}
    with open(file_dir, "r") as f:
        for line in f.readlines():
            data = re.findall(r"[A-Z][A-Z]|\d+", line.strip())
            nodemap[data[0]] = {}
            for node in data[2:]:
                nodemap[data[0]][node] = 1
            pressuremap[data[0]] = int(data[1])
    for node in nodemap:
        for nnode in nodemap:
            if node != nnode and node in nodemap[nnode]:
                current_distance = nodemap[nnode][node]
                for neighbor in nodemap[node]:
                    if neighbor == nnode:
                        continue
                    if neighbor not in nodemap[nnode]:
                        nodemap[nnode][neighbor] = current_distance + nodemap[node][neighbor]
                    else:
                        nodemap[nnode][neighbor] = min(nodemap[nnode][neighbor],
                                                       current_distance + nodemap[node][neighbor])
                if not pressuremap[node]:
                    del nodemap[nnode][node]
    return nodemap, pressuremap


# solution for part 1
def gen_paths(nodemap, pressuremap, start, maxtime):
    paths = []
    def gen(v, pressure=0, time=maxtime, path=[]):
        nonlocal paths
        if time <= 0:
            return
        pressure += pressuremap[v] * time
        if path not in paths:
            paths.append((pressure, path + [v]))
        for nv in nodemap[v]:
            if nv not in path:
                gen(nv, pressure, time - nodemap[v][nv] - 1, path + [v])
    gen(start)
    return paths

def part1(data):
    nodemap, pressuremap = data
    return max(gen_paths(nodemap, pressuremap, "AA", 30))

# solution for part 2
def part2(data):
    nodemap, pressuremap = data
    paths = gen_paths(nodemap, pressuremap, "AA", 26)
    sorted_paths = sorted(paths, reverse=True)
    maxpressure = 0
    for i in range(len(sorted_paths)):
        pri, pi = sorted_paths[i]
        for j in range(i + 1, len(sorted_paths)):
            prj, pj = sorted_paths[j]
            if set(pi).intersection(set(pj)) == set(["AA"]):
                maxpressure = max(maxpressure, pri + prj)
    return maxpressure


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
