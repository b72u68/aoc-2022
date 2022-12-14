import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        return [line.strip().split() for line in f.readlines()]


# solution for part 1
def part1(data):
    tp = [[0,0]]
    kl = [[0,0] for _ in range(9)]
    H = [0,0]
    t = kl[0]
    dd = {'U':[1,1], 'D':[1,-1], 'R':[0,1], 'L':[0,-1]}
    for line in data:
        n = int(line[1])
        e = dd[line[0]]
        for i in range(n):
            H[e[0]] += e[1]
            p = list(H)
            for i in kl:
                xd = p[0] - i[0]
                yd = p[1] - i[1]
                if not (abs(xd) <=1 and abs(yd) <= 1):
                    if xd != 0: i[0] += int(abs(xd)/xd)
                    if yd != 0: i[1] += int(abs(yd)/yd)
                p = list(i)
                break
            if list(t) not in tp: tp.append(list(t))
    return len(tp)


# solution for part 2
def part2(data):
    tp = [[0,0]]
    kl = [[0,0] for _ in range(9)]
    H = [0,0]
    t = kl[8]
    dd = {'U':[1,1], 'D':[1,-1], 'R':[0,1], 'L':[0,-1]}
    for line in data:
        n = int(line[1])
        e = dd[line[0]]
        for i in range(n):
            H[e[0]] += e[1]
            p = list(H)
            for i in kl:
                xd = p[0] - i[0]
                yd = p[1] - i[1]
                if not (abs(xd) <=1 and abs(yd) <= 1):
                    if xd != 0: i[0] += int(abs(xd)/xd)
                    if yd != 0: i[1] += int(abs(yd)/yd)
                p = list(i)
            if list(t) not in tp: tp.append(list(t))
    return len(tp)


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
