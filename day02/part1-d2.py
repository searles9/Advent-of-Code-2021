# Day 2 - Part 1

def get_position(file):
    depth = 0
    horizontal = 0
    with open(file) as file:
        for line in file:
            line = line.strip()
            line = line.split(" ")
            if line[0].startswith("forward"):
                horizontal += int(line[1])
            if line[0].startswith("down"):
                depth += int(line[1])
            if line[0].startswith("up"):
                depth -= int(line[1])
    return depth * horizontal




if __name__ == "__main__":
    print(get_position("input-d2.txt")) # 2322630