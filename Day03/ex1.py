with open("input.txt", "r") as f:
    text = f.read()

my_map = text.split("\n")
for i in range(len(my_map)):
    my_map[i] = list(my_map[i])

max_x = len(my_map[0])
max_y = len(my_map)

x = 0
y = 0

encoutered_trees = 0

while y < max_y:
    if my_map[y][x] == "#":
        my_map[y][x] = "X"
        encoutered_trees += 1
    else:
        my_map[y][x] = "O"
    x += 3
    y += 1
    if x >= max_x:
        x -= max_x

for i in range(len(my_map)):
    my_map[i] = ''.join(my_map[i])
print('\n'.join(my_map))
print(encoutered_trees)