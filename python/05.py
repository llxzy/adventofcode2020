lines = []
with open("day5_input.txt", 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def search_row(s):
    l, r = 0, 127
    for i in range(0, 7):
        m = (l + r + 1)//2
        if s[i] == 'F':
            r = m - 1
        else:
            l = m
    return l


def search_col(s):
    l, r = 0, 7
    for i in range(7, 10):
        m = (l+r+1)//2
        if s[i] == 'L':
            r = m - 1
        else:
            l = m
    return l


def calc_seats():
    seats = set()
    for line in lines:
        seats.add(search_row(line) * 8 + search_col(line))
    
    s_id = 0
    for i in range(max(seats)):
        if i + 1 in seats and i - 1 in seats and i not in seats:
            s_id = i

    return max(seats), s_id

print(calc_seats())