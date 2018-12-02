count_twice = 0
count_three = 0
with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    eligible_2 = True
    eligible_3 = True
    for letter in line.split("\n")[0]:
        if line.split("\n")[0].count(letter) == 2 and eligible_2:
            count_twice += 1
            eligible_2 = False
        if line.split("\n")[0].count(letter) == 3 and eligible_3:
            count_three += 1
            eligible_3 = False

print(count_three)
print(count_twice)
print(count_three * count_twice)
