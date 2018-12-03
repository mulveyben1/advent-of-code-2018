with open('input.txt', 'r') as file:
    lines = file.readlines()
# 1000x1000 inches
claimed = [[0 for x in range(1000)] for y in range(1000)]
overlap = 0
for line in lines:
    x, y = (line.split(' ')[2]).strip(':').split(',')
    width, height = (line.split(' ')[3]).strip('\n').split('x')
    for r in range(int(x), int(width)+int(x)):
        for c in range(int(y), int(height)+int(y)):
            claimed[c][r] += 1

for r in range(1000):
    for c in range(1000):
        if claimed[c][r] > 1:
            overlap += 1

print(overlap)
