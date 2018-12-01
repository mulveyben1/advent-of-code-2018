frequency = 0
seen_frequencies = []
with open('input.txt', 'r') as file:
    lines = file.readlines()

for i in range(150):
    for line in lines:
        frequency += int(line)
        if frequency in seen_frequencies:
            print(frequency)
            break
        seen_frequencies.append(frequency)
