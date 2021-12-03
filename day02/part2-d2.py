# Day 2 - Part 2

def get_position(file):
    depth = 0
    horizontal = 0
    aim = 0
    with open(file) as file:
        for line in file:
            line = line.strip()
            line = line.split(" ")
            if line[0].startswith("forward"):
                horizontal += int(line[1])
                if line[1] != 0: depth += aim * int(line[1])
            if line[0].startswith("down"): # positive
                aim += int(line[1])
            if line[0].startswith("up"): # negative
                aim -= int(line[1])
    return depth * horizontal




if __name__ == "__main__":
    print(get_position("input-d2.txt")) # 105273490