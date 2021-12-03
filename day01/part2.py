# Day 1 - Part 2
# Find increases based on a sliding scale

import part1

def get_sliding_increases(inputs):
    increases = 0
    for count, i in enumerate(inputs):
        if count + 4 > len(inputs): break 
        # slice the items i:next 3
        first_window = inputs[count:count + 3]
        # slice the items i+1:next 3
        second_window = inputs[count + 1:count + 4]
        if sum(first_window) < sum(second_window): increases += 1
    return increases


if __name__ == "__main__":
    inputs = part1.get_input("input.txt")
    print(get_sliding_increases(inputs)) # 1421