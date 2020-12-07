with open("input.txt", "r") as f:
    text = f.read()

answers = text.split('\n')

letters = "abcdefghijklmnopqrstuvwxyz"
done = [0 for _ in range(len(letters))]

people = 0
res = 0

group = ''

for answer in answers:
    people += 1
    group += answer
    if answer == '':
        for i in range(len(letters)):
            if group.count(letters[i]) == people - 1:
                done[i] = 1
        res += sum(done)
        done = [0 for _ in range(len(letters))]
        group = ''
        people = 0

print(res)
