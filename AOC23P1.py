import sys
test = \
    """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""

sys.setrecursionlimit(int(1e5))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

signx = {'>': 0, '<': 0, 'v': 1, '^': -1}
signy = {'>': 1, '<': -1, 'v': 0, '^': 0}


def dfs(x, y, prevx, prevy, dist):
    mx = dist
    for i in range(4):
        if (x + dx[i] >= 0 and x + dx[i] < len(arr) and y + dy[i] >= 0 and y + dy[i] < len(arr) and not (x + dx[i] == prevx and y + dy[i] == prevy)):
            if (arr[x+dx[i]][y+dy[i]] == '.' or (arr[x+dx[i]][y+dy[i]] != '#' and signx[arr[x+dx[i]][y+dy[i]]] == dx[i] and signy[arr[x+dx[i]][y+dy[i]]] == dy[i])):
                mx = max(mx, dfs(x+dx[i], y+dy[i], x, y, dist+1))
    return mx


raw = open("AOC23.txt", "r")
inp = raw.read()

arr = []
cnt = 0
sx, sy = -1, -1
for line in inp.splitlines():
    if (cnt == 0):
        for i in range(len(line)):
            if (line[i] == '.'):
                sx, sy = 0, i
    arr.append(line)
    cnt += 1

print(dfs(sx, sy, -1, -1, 0))
