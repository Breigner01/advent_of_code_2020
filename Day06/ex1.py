with open("input.txt", "r") as f:
    text = f.read()

answers = text.split('\n')

letters = "abcdefghijklmnopqrstuvwxyz"
done = [0 for _ in range(len(letters))]

res = 0

group = ''

for answer in answers:
    group += answer
    if answer == '':
        for i in range(len(letters)):
            if letters[i] in group:
                done[i] = 1
        res += sum(done)
        done = [0 for _ in range(len(letters))]
        group = ''

print(res)
