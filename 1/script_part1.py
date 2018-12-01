frequency = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        frequency += int(line)
print(frequency)
