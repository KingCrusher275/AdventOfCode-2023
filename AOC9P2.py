test = \
    """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

raw = open('AOC9.txt', 'r')
inp = raw.read()


def sumSeq(sequence):
    works = True
    for elem in sequence:
        if elem != 0:
            works = False
    if (works):
        return 0

    newSeq = []
    for i in range(len(sequence) - 1):
        newSeq.append(sequence[i+1] - sequence[i])

    next = sumSeq(newSeq)
    return sequence[0] - next


ans = 0
for line in inp.splitlines():
    sequence = list(map(int, line.split()))
    ans += sumSeq(sequence)

print(ans)
