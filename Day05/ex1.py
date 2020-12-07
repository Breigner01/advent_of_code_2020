import math

with open("input.txt" ,"r") as f:
    text = f.read()

seats = text.split('\n')

highest_seat_value = 0
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
    if seat_value > highest_seat_value:
        highest_seat_value = seat_value

print(highest_seat_value)
