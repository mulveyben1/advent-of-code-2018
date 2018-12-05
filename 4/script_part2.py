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
print(date)

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
        print(guard + ' on @ ' + str(ts))

    if ts[1].find('wakes') != -1:
        ends = int(ts[0][4:])
        asleep.append([guard, ends, begins])
    if ts[1].find('falls') != -1:
        begins = int(ts[0][4:])
    if begins != 0:  # falling asleep
        print(guard + ' asleep @ ' + str(begins))
    if ends != 0:
        print(guard + ' awake @ ' + str(ends))

guards = set(guards)
asl = [0 for i in range(10000)]

for line in asleep:
    guard = line[0]
    asl[int(guard)] += line[1]-line[2]


maximum = [0, 0]
print(asl)
for idx, num in enumerate(asl):
    if num > maximum[0]:
        maximum[0] = num
        maximum[1] = idx

sleepiest_guard = maximum[1]
print(sleepiest_guard)

sleeping = [0 for i in range(60)]

for ts in asleep:
    if str(ts[0]) == str(sleepiest_guard):
        for i in range(ts[2], ts[1]):
            sleeping[i] += 1




