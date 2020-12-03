with open("input.txt", "r") as f:
    text = f.read()

my_map = text.split("\n")
for i in range(len(my_map)):
    my_map[i] = list(my_map[i])

max_x = len(my_map[0])
max_y = len(my_map)

steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

encoutered_trees = [0, 0, 0, 0, 0]

for i in range(len(steps)):
    x = 0
    y = 0
    while y < max_y:
        if my_map[y][x] == "#":
            my_map[y][x] = "X"
            encoutered_trees[i] += 1
        else:
            my_map[y][x] = "O"
        x += steps[i][0]
        y += steps[i][1]
        if x >= max_x:
            x -= max_x

    for j in range(len(my_map)):
        my_map[j] = ''.join(my_map[j])
    print('\n'.join(my_map))
    print(encoutered_trees)
    my_map = text.split("\n")
    for j in range(len(my_map)):
        my_map[j] = list(my_map[j])

    print(encoutered_trees[0] * encoutered_trees[1] * encoutered_trees[2] * encoutered_trees[3] * encoutered_trees[4])
