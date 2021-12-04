# Day 3 - Part 1

def get_vals(lines):
    gamma = ""
    epsilion = ""

    for index in range(len(lines[0])):
        bit0 = 0
        bit1 = 0
        for line in lines:
            if line[index] == "0":
                bit0 += 1
            elif line[index] == "1":
                bit1 += 1
        if bit0 > bit1:
            gamma += "0"
            epsilion += "1"
        else:
            gamma += "1"
            epsilion += "0"

    return  (gamma , epsilion)


if __name__ == "__main__":
    lines = [x.strip() for x in open('input-d3.txt', 'r').readlines()]
    gamma , epsilion = get_vals(lines)
    print(f"GAMMA - BINARY: {int(gamma)}")
    print(f"GAMMA DECIMAL: {int(gamma,2)}")
    print(f"EPSILION - BINARY: {int(epsilion)}")
    print(f"EPSILION DECIMAL: {int(epsilion,2)}")
    print(f"POWER CONSUMPTION: {(int(gamma,2)) * (int(epsilion,2)) }")
