import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    f = open(file_dir)

    # process data here
    data = f.readlines()
    f.close()

    return [line.strip() for line in data]


# solution for part 1
def part1(data):
    result = 0
    for sack in data:
        p1, p2 = sack[:len(sack)//2], sack[len(sack)//2:]
        inter = list(set(p1).intersection(set(p2)))[0]
        if inter.isupper():
            result += (ord(inter) - ord("A") + 1) + 26
        else:
            result += ord(inter) - ord("a") + 1
    return result


# solution for part 2
def part2(data):
    groups = [data[i:i+3] for i in range(0, len(data), 3)]
    result = 0
    for group in groups:
        inter = list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0]
        if inter.isupper():
            result += (ord(inter) - ord("A") + 1) + 26
        else:
            result += ord(inter) - ord("a") + 1
    return result


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
