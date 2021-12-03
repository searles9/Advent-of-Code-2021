def get_input(file):
    with open(file, "r") as file:
        lines = file.readlines()
        return [int(measurement.strip()) for measurement in lines]

def check_increases(inputs):
    increases = 0 
    for count, i in enumerate(inputs, start=0):
        if count == 0: depth = i
        if i > depth: increases += 1
        depth = i
    return increases

if __name__ == "__main__":
    inputs = get_input("input.txt")
    print(check_increases(inputs))
    