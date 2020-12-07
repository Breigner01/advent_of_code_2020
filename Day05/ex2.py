import math

with open("input.txt" ,"r") as f:
    text = f.read()

seats = text.split('\n')

airplane_seats = [i for i in range(1024)]
found_seats = [False for _ in range(1024)]
seat_value = 0

for seat in seats:
    lower_row = 0
    upper_row = 127
    lower_col = 0
    upper_col = 7
    for i in range(7):
        if seat[i] == 'F':
            upper_row = math.floor((upper_row + lower_row) / 2)
        elif seat[i] == 'B':
            lower_row = math.ceil((upper_row + lower_row) / 2)
    for i in range(7, 10):
        if seat[i] == 'L':
            upper_col = math.floor((upper_col + lower_col) / 2)
        elif seat[i] == 'R':
            lower_col = math.ceil((upper_col + lower_col) / 2)
    seat_value = upper_row * 8 + upper_col
    found_seats[seat_value] = True
    airplane_seats.remove(seat_value)

for i in airplane_seats:
    if i != 0 and i != 1024 and not found_seats[i] and found_seats[i - 1] and found_seats[i + 1]:
        print(i)
