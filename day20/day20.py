import os
import sys
import copy


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        return [int(line.strip()) for line in f.readlines()]


def decrypt(msg, key, repeat=1):
    msg = [(i, n * key) for i, n in enumerate(msg)]
    for _ in range(repeat):
        for i in range(len(msg)):
            for j in range(len(msg)):
                if msg[j][0] == i:
                    curr = msg.pop(j)
                    new_idx = (j + curr[1]) % len(msg)
                    msg.insert(new_idx, (i, curr[1]))
                    break
    for i, (_, n) in enumerate(msg):
        if n == 0:
            return msg[(i + 1000) % len(msg)][1] + msg[(i + 2000) % len(msg)][1] \
                    + msg[(i + 3000) % len(msg)][1]

# solution for part 1
def part1(data):
    return decrypt(copy.deepcopy(data), 1, 1)


# solution for part 2
def part2(data):
    return decrypt(copy.deepcopy(data), 811589153 , 10)


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
