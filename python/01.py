lines = []
filename = "input.txt"
with open(filename, 'r') as read_f:
        lines = [int(line.strip()) for line in read_f.readlines()]
target = 2020


def two_sum_to_2020():
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            if lines[i] + lines[j] == target:
                return lines[i] * lines[j]


# can be done with better complexity
def three_sum_to_2020():
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            for k in range(j+ 1, len(lines)):
                if lines[i] + lines[j] + lines[k] == target:
                    return lines[i] * lines[j] * lines[k]


print(two_sum_to_2020())
print(three_sum_to_2020())