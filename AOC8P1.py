test = \
    """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

raw = open('AOC8.txt', 'r')
inp = raw.read()

start = 1
vals = {}
seq = ""
for line in inp.splitlines():
    if start == 1:
        seq = list(line.strip())
    elif (len(line) != 0):
        key, val = line.split(" = ")
        val = tuple(val.strip('()').split(', '))
        vals[key] = val
    start += 1

start = 0
curPos = "AAA"
while (curPos != "ZZZ"):
    curPos = vals[curPos][seq[start % len(seq)] == "R"]
    start += 1

print(start)
