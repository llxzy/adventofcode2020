import string

lines = []
with open("day6_input.txt", 'r') as f:
    line_str = f.read()
    lines = line_str.split("\n\n")


def count_answers():
    count = 0
    for ls in lines:
        print(ls)
        s = "".join(ls.split('\n'))
        count += len(set(s))
    return count


def count_yes_answers():
    count = 0
    for ls in lines:
        strs = ls.split('\n')
        sets = set(string.ascii_lowercase)
        for s in strs:
            sets = sets.intersection(set(s))
        count += len(sets)
    return count


print(count_answers())
print(count_yes_answers())
