test = \
    """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

raw = open('AOC11.txt', 'r')
inp = raw.read()


def checkRow(ix):
    for i in range(m):
        if (arr[ix][i] != '.'):
            return 0
    return 1


def checkCol(ix):
    for i in range(n):
        if (arr[i][ix] != '.'):
            return 0
    return 1


arr = []
for line in inp.splitlines():
    arr.append(list(line))

n = len(arr)
m = len(arr[0])
pcol = [0 for i in range(n+1)]
prow = [0 for i in range(m+1)]
for i in range(m):
    prow[i+1] = prow[i] + checkCol(i)
for i in range(n):
    pcol[i+1] = pcol[i] + checkRow(i)

pos = []
for i in range(n):
    for j in range(m):
        if (arr[i][j] == '#'):
            pos.append((i, j))

ans = 0
for i in range(len(pos)):
    for j in range(i+1, len(pos)):
        ans += abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1]) + abs(
            pcol[pos[i][0]] - pcol[pos[j][0]]) + abs(prow[pos[i][1]] - prow[pos[j][1]])

print(ans)
