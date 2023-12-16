raw = open('AOC15.txt', 'r')
inp = raw.read()

test = \
    """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

ans = 0
codes = inp.replace("\n", "").split(',')
for code in codes:
    curval = 0
    for i in code:
        curval += ord(i)
        curval *= 17
        curval %= 256
    ans += curval
print(ans)
