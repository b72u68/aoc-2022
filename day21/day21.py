import os
import sys
import copy


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    data = {}
    with open(file_dir, "r") as f:
        for line in f.readlines():
            name, operation = line.strip().split(": ")
            res = None
            need = []
            if not operation.isnumeric():
                n1, op, n2 = operation.split()
                need.extend([n1, n2, op] if op != "/" else [n1, n2, "//"])
            else:
                res = int(operation)
            data[name] = (res, need)
    return data


# solution for part 1
def dfs(data):
    def dfs_rec(monkey):
        nonlocal data
        n, operation = data[monkey]
        if n is not None:
            return n
        n1, n2, op = operation
        try:
            if op == "+":
                n = dfs_rec(n1) + dfs_rec(n2)
            elif op == "-":
                n = dfs_rec(n1) - dfs_rec(n2)
            elif op == "*":
                n = dfs_rec(n1) * dfs_rec(n2)
            elif op == "//":
                n = dfs_rec(n1) // dfs_rec(n2)
            data[monkey] = (n, operation)
            return n
        except:
            return None
    return dfs_rec("root")


def part1(data):
    return dfs(copy.deepcopy(data))


# solution for part 2
def solve(equation, humn=0):
    ls, rs = equation.split("=")
    rs_val = int(eval(rs))
    while True:
        ls_val = eval(ls)
        print(humn, ls_val, rs_val)
        if ls_val == rs_val:
            return humn
        humn += 1

def build_equation(data):
    dfs(data)
    equation = f'{data["root"][1][0]}{data["root"][1][2]}{data["root"][1][1]}'
    def build_rec(monkey):
        nonlocal equation
        n, operation = data[monkey]
        if n is not None:
            equation = equation.replace(monkey, str(n))
            return
        if monkey == "humn":
            return
        n1, n2, op = operation
        equation = equation.replace(monkey, f'({n1}{op}{n2})')
        build_rec(n1)
        build_rec(n2)
    build_rec("root")
    return equation


def part2(data):
    n, operation = data["root"]
    data["root"] = (n, [operation[0], operation[1], "="])
    data["humn"] = (None, [])
    equation = build_equation(data)
    return solve(equation, humn=3441198822500)


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
