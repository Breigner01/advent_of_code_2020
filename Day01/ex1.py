import sys

with open("input.txt", "r") as f:
    text = f.read()

nb_list = list(map(int, text.split("\n")))

for i in range(len(nb_list)):
    for j in range(len(nb_list)):
        if i == j:
            continue
        if nb_list[i] + nb_list[j] == 2020:
            print(nb_list[i] * nb_list[j])
            sys.exit(0)