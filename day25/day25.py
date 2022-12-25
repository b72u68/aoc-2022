import os
import sys
import math


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir, "r") as f:
        return [line.strip() for line in f.readlines()]


MAP_SNAFU = {
        "2": 2,
        "1": 1,
        "0": 0,
        "-": -1,
        "=": -2
}

MAP_DECIMAL = {
        -2: "=",
        -1: "-",
        0: "0",
        1: "1",
        2: "2",
        3: "1=",
        4: "1-",
        5: "10",
        6: "11",
        7: "12",
        8: "2=",
        9: "2-",
        10: "20",
        15: "1=0",
        20: "1-0",
        2022: "1=11-2",
        12345: "1-0---0",
        314159265: "1121-1110-1=0"
}

# solution for part 1
def to_decimal(snafu):
    result = 0
    for i, c in enumerate(snafu):
        result += 5**(len(snafu) - 1 - i) * MAP_SNAFU[c]
    return result

def to_snafu(decimal):
    base = math.log(abs(decimal), 5)
    result = None
    def convert(decimal, base, snafu=""):
        nonlocal result
        if decimal in MAP_DECIMAL:
            result = snafu + MAP_DECIMAL[decimal]
            return
        if base == 0:
            return
        b = decimal / (5**(base-1))
        if b > 0:
            b = int(b) if b - int(b) < 0.5 else int(b)+1
        else:
            b = int(b) if abs(b) - int(abs(b)) < 0.5 else int(b)-1
        convert(decimal - 5**(base-1)*b, base-1, snafu+MAP_DECIMAL[b])
    convert(decimal, int(base)+1)
    return result

def part1(data):
    result = 0
    for n in data:
        result += to_decimal(n)
    return to_snafu(result)


# solution for part 2
def part2(data):
    return


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
