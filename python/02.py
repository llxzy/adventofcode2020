"""
loads items from input file and splits them into a tuple of values
"""
lines = []
with open("day2_input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

inputs = []
for line in lines:
    fs = line.split(':')
    limits = fs[0].split(' ')
    vals = limits[0].split('-')
    inputs.append((int(vals[0]), int(vals[1]), limits[1], fs[1]))


def valid_passwords_one():
    valid_count = 0
    for entry in inputs:
        x, y, c, string = entry
        z = len(list(filter(lambda x: x == c, string)))
        valid_count += z >= x and z <= y
    return valid_count


def valid_passwords_two():
    valid_count = 0
    for entry in inputs:
        x, y, c, string = entry
        string = string.strip()
        valid_count += (string[x-1] == c)^(string[y-1] == c)
    return valid_count


print(valid_passwords_one())
print(valid_passwords_two())
