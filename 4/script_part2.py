import re
with open('input.txt', 'r') as file:
    lines = file.readlines()
asleep = []
date = []
for line in lines:
    ts = [line[6:17].replace(':', '').replace('-', '').replace(' ', ''), line[19:len(line)-1]]
    date.append(ts)

out = []
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

asl = [[] for i in range(60)]

for ts in asleep:
    for i in range(ts[2], ts[1]):
        asl[i].append(ts[0])

maximum = [0, 0, 0]  # num times asleep, guard id, minute
for idx, minute in enumerate(asl):
    for guard in guards:
        if minute.count(guard) > maximum[0]:
            maximum[0] = minute.count(guard)
            maximum[1] = int(guard)
            maximum[2] = idx
print(maximum[2] * maximum[1])  # minute * guard id


