with open('input.txt', 'r') as file:
    line = file.readlines()[0].strip('\n')


def check_case(char0, char1):
    if char0.lower() != char1.lower():
        return False
    if char0.islower() and char1.isupper():
        return True
    elif char0.isupper() and char1.islower():
        return True


for idx, i in enumerate(line):
    if idx + 1 == len(line):
        break
    print(i + ' ' + line[idx+1])
    print(check_case(i, line[idx+1]))
