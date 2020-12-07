import re

with open("input.txt", "r") as f:
    text = f.read()

content = text.split("\n")
passports = ["" for _ in range(len(content))]
j = 0

for i in range(len(content)):
    passports[j] += content[i] + ' '
    if content[i] == "":
        passports[j] = passports[j].split(' ')
        for k in range(len(passports[j])):
            passports[j][k] = passports[j][k].split(':')
        j += 1
i = 0
while passports[i] != "":
    i += 1
passports[i:] = []

valid = 0
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
required_values = [[1920, 2002], [2010, 2020], [2020, 2030], {"cm": [150, 193], "in": [59, 76]}, r"#[0-9a-f]{6}",
                   ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], r"^[0-9]{9}$"]
found_field = [False for _ in range(len(required_fields))]

for passport in passports:
    for field in passport:
        for i, key in enumerate(required_fields):
            if field[0] == key:
                if key in ["byr", "iyr", "eyr"]:
                    try:
                        value = int(field[1])
                        if value >= required_values[i][0] and value <= required_values[i][1]:
                            found_field[i] = True
                    except TypeError:
                        pass
                elif key == "hgt":
                    try:
                        value = int(field[1][:-2])
                        unit = field[1][-2:]
                        if value >= required_values[i][unit][0] and value <= required_values[i][unit][1]:
                            found_field[i] = True
                    except (TypeError, KeyError, ValueError):
                        pass
                elif key in ["hcl", "pid"]:
                    if re.match(required_values[i], field[1]) is not None:
                        found_field[i] = True
                elif key == "ecl":
                    if field[1] in required_values[i]:
                        found_field[i] = True
    if all(found_field):
        valid += 1
    found_field = [False for _ in range(len(required_fields))]

print(valid)
