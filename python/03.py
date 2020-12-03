lines = []
with open("day3_input.txt", 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def count_trees(right, down):
    current_pos = 0
    length = len(lines[0])
    tree_count = 0
    for i in range(0, len(lines) - 1, down):
        new_pos = (current_pos + right) % length
        if lines[i+down][new_pos] == '#':
            tree_count += 1
        current_pos = new_pos
    return tree_count


def count_all_slopes():
    directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1
    for r, d in directions:
        total *= count_trees(r, d)
        print(count_trees(r, d))
        print(total)
    return total

print(count_trees(3, 1))
print(count_all_slopes())