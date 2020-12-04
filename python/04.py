import string


lines = []
with open("day4_input.txt", 'r') as f:
    x = f.read()
    l = x.split('\n\n')
    for a in l:
        lines.append(" ".join(a.split('\n')))

pp_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]


data_dicts = []
for line in lines:
    data_dict = dict()
    for s in line.split(' '):
        if s == "":
            continue
        x = s.split(':')
        data_dict[x[0]] = x[1]
    data_dicts.append(data_dict)


valid_ones = []

    

def valid_passports():
    count = 0
    for d in data_dicts:
        if all(map(lambda x: x in d.keys(), pp_fields)):
            count += 1
            valid_ones.append(d)
    return count



def check_string(s, length, lower, upper):
    if len(s) != length or not all(map(lambda x: x.isdigit(), s)):
        return False
    return int(s) >= lower and int(s) <= upper


def check_height(s):
    if not ("cm" in s or "in" in s):
        return False
    n = "".join(filter(str.isdigit, s))
    if "cm" in s:
        return check_string(n, 3, 150, 193)
    return check_string(n, 2, 59, 76)


def check_color(s):
    if not s.startswith("#"):
        return False
    rest = s[1:]
    chars = ['0']
    return len(rest) == 6 and all(map(lambda x: x in string.hexdigits, rest))




def valid_data():
    count = 0
    for d in valid_ones:
        year = check_string(d["byr"], 4, 1920, 2002)
        issue_year = check_string(d["iyr"], 4, 2010, 2020)
        exp_year = check_string(d["eyr"], 4, 2020, 2030)
        height = check_height(d["hgt"])
        hair_color = check_color(d["hcl"])
        eye_color = d["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        pid = len(d["pid"]) == 9 and all(map(str.isdigit, d["pid"]))
        count += year and issue_year and exp_year and height and hair_color and eye_color and pid
    return count


print(valid_passports())
print(valid_data())