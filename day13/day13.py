import os
import sys
from functools import cmp_to_key


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        raw_data = [line.strip() for line in f.readlines()]
    return [(eval(raw_data[i]), eval(raw_data[i+1])) for i in range(0, len(raw_data), 3)]


# solution for part 1
def compare(l1, l2, nested=0):
    # print(f"{' '*nested*2}Compare {l1} vs {l2}")
    i1 = i2 = 0
    while i1 < len(l1) and i2 < len(l2):
        # print(f"{' '*nested*2}Compare {l1[i1]} vs {l2[i2]}")
        if isinstance(l1[i1], int) and isinstance(l2[i2], int):
            if l1[i1] > l2[i2]:
                return 0
            elif l1[i1] < l2[i2]:
                return 1
        elif isinstance(l1[i1], int) and isinstance(l2[i2], list):
            # print(f"{' '*(nested+1)*2}Mixed types; convert left to {[l1[i1]]} and retry comparison")
            result = compare([l1[i1]], l2[i2], nested+1)
            if result == 0 or result == 1:
                return result
        elif isinstance(l1[i1], list) and isinstance(l2[i2], int):
            # print(f"{' '*(nested+1)*2}Mixed types; convert right to {[l2[i2]]} and retry comparison")
            result = compare(l1[i1], [l2[i2]], nested+1)
            if result == 0 or result == 1:
                return result
        else:
            result = compare(l1[i1], l2[i2], nested+1)
            if result == 0 or result == 1:
                return result
        i1 += 1
        i2 += 1
    if i1 < len(l1) and i2 >= len(l2):
        return 0
    elif i1 == len(l1) and i2 == len(l2):
        return 2
    return 1

def part1(data):
    count = 0
    for i in range(len(data)):
        l1, l2 = data[i]
        result = compare(l1, l2)
        if result:
            count += i + 1
    return count


# solution for part 2
def sort(packets):
    # bubblesort because I'm stupid
    while True:
        swapped = False
        for i in range(len(packets)-1):
            if not compare(packets[i], packets[i+1]):
                packets[i], packets[i+1] = packets[i+1], packets[i]
                swapped = True
        if not swapped:
            break
    return packets

def part2(data):
    packets = []
    for i in range(len(data)):
        packets.extend(data[i])
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = sort(packets)
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


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
