import math
test = \
    """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

raw = open('AOC8.txt', 'r')
inp = raw.read()


def pathLength(curPos):
    start = 0
    while (curPos[-1] != "Z"):
        curPos = vals[curPos][seq[start % len(seq)] == "R"]
        start += 1

    return start


start = 1
vals = {}
seq = ""
keys = []
for line in inp.splitlines():
    if start == 1:
        seq = list(line.strip())
    elif (len(line) != 0):
        key, val = line.split(" = ")
        val = tuple(val.strip('()').split(', '))
        vals[key] = val
        keys.append(key)
    start += 1

lengths = []
for key in keys:
    if (key[-1] == "A"):
        lengths.append(pathLength(key))


print(math.lcm(*lengths))
