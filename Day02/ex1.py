with open("input.txt", "r") as f:
    text = f.read()

text = text.split("\n")
content = []
nb_pwd = 0

for i in range(len(text)):
    content += [text[i].split(" ")]
    content[i][0] = content[i][0].split("-")
    content[i][0][0] = int(content[i][0][0])
    content[i][0][1] = int(content[i][0][1])
    content[i][1] = content[i][1].replace(":", "")
    nb = content[i][2].count(content[i][1])
    if nb >= content[i][0][0] and nb <= content[i][0][1]:
        nb_pwd += 1

print(nb_pwd)