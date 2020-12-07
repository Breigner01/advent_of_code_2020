with open("input.txt", "r") as f:
    text = f.read()

text = text.split("\n")
content = []
nb_pwd = 0

for i in range(len(text)):
    content += [text[i].split(" ")]
    content[i][0] = content[i][0].split("-")
    content[i][0][0] = int(content[i][0][0]) - 1
    content[i][0][1] = int(content[i][0][1]) - 1
    content[i][1] = content[i][1].replace(":", "")
    if (len(content[i][2]) > content[i][0][0] and content[i][2][content[i][0][0]] == content[i][1] and
    ((len(content[i][2]) > content[i][0][1] and content[i][2][content[i][0][1]] and
    content[i][2][content[i][0][1]] != content[i][1]) or len(content[i][2]) <= content[i][0][1])) or (
    len(content[i][2]) > content[i][0][1] and content[i][2][content[i][0][1]] == content[i][1] and
    content[i][2][content[i][0][0]] != content[i][1]):
        nb_pwd += 1

print(nb_pwd)
