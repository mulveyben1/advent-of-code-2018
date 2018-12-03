with open('input.txt', 'r') as file:
    lines = file.readlines()

claimed = [[[] for x in range(1000)] for y in range(1000)]
invalid = []
possible = []
for line in lines:
    x, y = (line.split(' ')[2]).strip(':').split(',')
    width, height = (line.split(' ')[3]).strip('\n').split('x')
    for r in range(int(x), int(width)+int(x)):
        for c in range(int(y), int(height)+int(y)):
            claimed[c][r].append(line.split(' ')[0])

for r in range(1000):
    for c in range(1000):
        if len(claimed[c][r]) > 1:
            for i in range(len(claimed[c][r])):
                invalid.append(claimed[c][r][i])
        if len(claimed[c][r]) == 1:
            for i in range(1):
                possible.append(claimed[c][r][i])

print(set(possible)-set(invalid))
