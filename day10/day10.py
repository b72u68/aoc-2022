import os
import sys


# get data from file
def get_data(filename):
    file_dir = os.path.join(os.getcwd(), filename)
    with open(file_dir) as f:
        data = [line.strip() for line in f.readlines()]
    return data


# solution for part 1
def part1(data):
    X = 1
    cycle = 0
    strengths = 0
    target_cycle = 20
    for signal in data:
        prevX = X
        if signal == "noop":
            cycle += 1
        else:
            cycle += 2
            X += int(signal.split(" ")[1])
        if target_cycle <= 220:
            if cycle >= target_cycle:
                strengths += prevX * target_cycle
                target_cycle += 40
    return strengths


# solution for part 2
def part2(data):
    sprite_position = ["."] * 40
    sprite_position[0] = sprite_position[1] = sprite_position[2] = "#"
    crt = []
    X = 1
    cycle = 0
    for signal in data:
        if signal == "noop":
            crt.append(sprite_position[cycle % 40])
            cycle += 1
        else:
            for _ in range(2):
                crt.append(sprite_position[cycle % 40])
                cycle += 1
            X += int(signal.split(" ")[1])
            sprite_position = ["."] * 40
            for dX in range(-1, 2):
                if X + dX < len(sprite_position):
                    sprite_position[X+dX] = "#"
    return "".join(["".join(crt[i:i+40]) + "\n" for i in range(0, len(crt), 40)])

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
