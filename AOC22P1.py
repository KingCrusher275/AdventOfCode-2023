test = \
    """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

raw = open("AOC22.txt", "r")
inp = raw.read()

pos = []
for line in inp.splitlines():
    cur = line.split('~')
    pos.append([[int(z) for z in x.split(',')] for x in cur])


pos = sorted(pos, key=lambda x: x[1][2])

on = []
for i in range(len(pos)):
    z = 0
    on.append([])
    for j in range(i):
        if (max(pos[i][0][0], pos[j][0][0]) <= min(pos[i][1][0], pos[j][1][0]) and max(pos[i][0][1], pos[j][0][1]) <= min(pos[i][1][1], pos[j][1][1])):
            if (pos[j][1][2] == z):
                on[-1].append(j)
            elif (pos[j][1][2] > z):
                on[-1] = [j]
                z = pos[j][1][2]

    pos[i][0][2], pos[i][1][2] = z+1, z+1+(pos[i][1][2] - pos[i][0][2])

ans = len(pos)
check = set()
for i in range(len(pos)):
    if (len(on[i]) == 1 and on[i][0] not in check):
        ans -= 1
        check.add(on[i][0])
print(ans)
