raw = open('AOC15.txt', 'r')
inp = raw.read()

test = \
    """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

boxes = [[] for _ in range(256)]
ans = 0
codes = inp.replace("\n", "").split(',')
for code in codes:
    curval = 0

    if (code[-1] == '-'):
        for i in code[:-1]:
            curval += ord(i)
            curval *= 17
            curval %= 256
    else:
        for i in code[:-2]:
            curval += ord(i)
            curval *= 17
            curval %= 256

    if (code[-1] == '-'):
        i = 0
        while (i < len(boxes[curval])):
            if (boxes[curval][i][:-2] == code[:-1]):
                boxes[curval].pop(i)
                i -= 1
            i += 1
    else:
        found = False
        i = 0
        while (i < len(boxes[curval])):
            if (boxes[curval][i][:-2] == code[:-2]):
                found = True
                boxes[curval][i] = code
                break
            i += 1
        if (not found):
            boxes[curval].append(code)

for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        ans += (i + 1) * (j+1) * int(boxes[i][j][-1])

print(ans)
