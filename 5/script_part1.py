with open('input1.txt', 'r') as file:
    line = file.readlines()[0].strip('\n')

line = list(line)
def check_case(char0, char1):
    if char0.lower() != char1.lower():
        return False
    if char0.islower() and char1.isupper():
        return True
    elif char0.isupper() and char1.islower():
        return True


def get_first_match(lin):
    for idx, i in enumerate(lin):
        if check_case(i, lin[idx+1]):
            return [idx, idx+1]
        else:
            return [0, 0]


def remove(li, lin):
    for i in range(li[0], li[1]):
        del lin[i]
        del lin[i]


