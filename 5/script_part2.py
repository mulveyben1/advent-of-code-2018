def removeletters(line, char):
    for idx, i in enumerate(line):
        if i.lower == char:
            del line[idx]
    return line


def check_case(char0, char1):
    if char0.lower() != char1.lower():
        return False
    if char0.islower() and char1.isupper():
        return True
    elif char0.isupper() and char1.islower():
        return True


def get_first_match(lin):
    for idx, i in enumerate(lin):
        if idx + 1 < len(lin):
            if check_case(i, lin[idx+1]):
                return [idx, idx+1]
        else:
            return [0, 0]
    else:
        return [0, 0]


def remove(li, lin):
    for i in range(li[0], li[1]):
        if li[0] == 0 and li[1] == 0:
            return False
        else:
            del lin[i]
            del lin[i]
            return True


alphas = 'abcdefghijklmnopqrstuvwxyz'
lengths = [0 for i in range(26)]
for i in range(26):
    with open('input.txt', 'r') as file:
        line = file.readlines()[0].strip('\n')
    line = list(line)
    result = True
    line = removeletters(line, alphas[i])
    print('Removing %s' % alphas[i])
    while result:
        remove(get_first_match(line), line)
        result = remove(get_first_match(line), line)
    else:
        lengths[i] = len(line)

