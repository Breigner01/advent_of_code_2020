with open("input.txt", "r") as f:
    text = f.read()

content = text.split("\n")
passports = ["" for _ in range(len(content))]
j = 0

for i in range(len(content)):
    passports[j] += content[i] + ' '
    if content[i] == "":
        j += 1
i = 0
while passports[i] != "":
    i += 1
passports[i:] = []

valid = 0
required_fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

for passport in passports:
    if all(field in passport for field in required_fields):
        valid += 1
print(valid)