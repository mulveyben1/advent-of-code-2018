with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    for line_ in lines:
        diffs = 0
        for i, char in enumerate(line):
            if char != line_[i]:
                diffs += 1
        if diffs == 1:
            ans = [char for i, char in enumerate(line) if line_[i] == char]
            print(ans)
