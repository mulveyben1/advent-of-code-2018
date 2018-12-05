import re
with open('input.txt', 'r') as file:
    lines = file.readlines()
asleep = []
date = []
for line in lines:
    ts = [line[6:17].replace(':', '').replace('-', '').replace(' ', ''), line[19:len(line)-1]]
    date.append(ts)

date.sort(key=lambda x: x[0])

global time
global begins
global ends
global guard
guards = []

for ts in date:
    if ts[1].find('begins') != -1:
        gid = re.search('[0-9]+', ts[1])
        guard = gid.group(0)
        begins = 0
        ends = 0
        guards.append(guard)

    if ts[1].find('wakes') != -1:
        ends = int(ts[0][4:])
        asleep.append([guard, ends, begins])
    if ts[1].find('falls') != -1:
        begins = int(ts[0][4:])

guards = set(guards)
asl = [0 for i in range(10000)]

for line in asleep:
    guard = line[0]
    asl[int(guard)] += line[1]-line[2]

maximum = [0, 0]
for idx, num in enumerate(asl):
    if num > maximum[0]:
        maximum[0] = num
        maximum[1] = idx

sleepiest_guard = maximum[1]

sleeping = [0 for i in range(60)]

for ts in asleep:
    if str(ts[0]) == str(sleepiest_guard):
        for i in range(ts[2], ts[1]):
            sleeping[i] += 1

maximum = [0, 0]
for idx, i in enumerate(sleeping):
    if i > maximum[0]:
        maximum[0] = i
        maximum[1] = idx

print(maximum[1] * sleepiest_guard)
