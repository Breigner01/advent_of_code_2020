import sys

with open("input.txt", "r") as f:
    text = f.read()

nb_list = list(map(int, text.split("\n")))

for i in range(len(nb_list)):
    for j in range(len(nb_list)):
        for k in range(len(nb_list)):
            if i == j or j == k or i == k:
                continue
            if nb_list[i] + nb_list[j] + nb_list[k] == 2020:
                print(nb_list[i] * nb_list[j] * nb_list[k])
                sys.exit(0)
