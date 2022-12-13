import os
import sys
import copy
import math
from functools import reduce


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        raw_data = [line.strip() for line in f.readlines()]

    monkeys = {}
    monkey_info = []
    for line in raw_data:
        if line != "":
            monkey_info.append(line)
            continue
        # process monkey info here
        no = int(monkey_info[0].split(" ")[1][:-1])
        items = [int(x) for x in monkey_info[1].split(":")[1].strip().split(", ")]
        operation = monkey_info[2].split(": ")[1].split("=")[1].strip()
        test = int(monkey_info[3].split(" ")[3])
        test_true = int(monkey_info[4].split(" ")[5])
        test_false = int(monkey_info[5].split(" ")[5])
        monkeys[no] = {
                "business": 0,
                "items": items,
                "operation": operation,
                "test": test,
                "test_operation": [test_true, test_false]}
        monkey_info = []

    return monkeys


# solution for part 1
def part1(data):
    monkeys = copy.deepcopy(data)
    for _ in range(20):
        for monkey in monkeys:
            operation = monkeys[monkey]["operation"]
            test = monkeys[monkey]["test"]
            test_operation = monkeys[monkey]["test_operation"]
            while monkeys[monkey]["items"]:
                item = monkeys[monkey]["items"].pop(0)
                new_worry = eval(operation.replace("old", str(item)))
                bored_worry = new_worry // 3
                monkeys[test_operation[1 - int(bored_worry % test == 0)]]["items"].append(bored_worry)
                monkeys[monkey]["business"] += 1
    sorted_monkeys = sorted(monkeys, key=lambda k: monkeys[k]["business"])
    return monkeys[sorted_monkeys[-1]]["business"] * monkeys[sorted_monkeys[-2]]["business"]


# solution for part 2
def part2(data):
    monkeys = copy.deepcopy(data)
    prod = reduce(lambda x, y: x * y, [monkeys[k]["test"] for k in monkeys])
    gcd = reduce(math.gcd, [monkeys[k]["test"] for k in monkeys])
    lcm = prod // gcd
    for _ in range(10000):
        for monkey in monkeys:
            operation = monkeys[monkey]["operation"]
            test = monkeys[monkey]["test"]
            test_operation = monkeys[monkey]["test_operation"]
            while monkeys[monkey]["items"]:
                item = monkeys[monkey]["items"].pop(0)
                new_worry = eval(operation.replace("old", str(item))) % lcm
                monkeys[test_operation[1 - int(new_worry % test == 0)]]["items"].append(new_worry)
                monkeys[monkey]["business"] += 1
    sorted_monkeys = sorted(monkeys, key=lambda k: monkeys[k]["business"])
    return monkeys[sorted_monkeys[-1]]["business"] * monkeys[sorted_monkeys[-2]]["business"]


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
