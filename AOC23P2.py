from collections import deque
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


def buildgraph(x, y, dist, prevVert):
    visited[x][y] = True
    for i in range(4):
        if (x + dx[i] >= 0 and x + dx[i] < len(arr) and y + dy[i] >= 0 and y + dy[i] < len(arr)):
            if (visited[x+dx[i]][y+dy[i]]):
                if ((x+dx[i], y+dy[i]) in vertices and (x+dx[i], y+dy[i]) != prevVert):
                    adj_list[vertices[prevVert]].append(
                        (vertices[(x+dx[i], y+dy[i])], dist+1))
                    adj_list[vertices[(x+dx[i], y+dy[i])]
                             ].append((vertices[prevVert], dist+1))
            elif (arr[x+dx[i]][y+dy[i]] != '#'):
                if ((x+dx[i], y+dy[i]) in vertices):
                    adj_list[vertices[prevVert]].append(
                        (vertices[(x+dx[i], y+dy[i])], dist+1))
                    adj_list[vertices[(x+dx[i], y+dy[i])]
                             ].append((vertices[prevVert], dist+1))
                    if (not visited[x+dx[i]][y+dy[i]]):
                        buildgraph(x+dx[i], y+dy[i],
                                   0, (x+dx[i], y+dy[i]))
                else:
                    buildgraph(x+dx[i], y+dy[i], dist+1, prevVert)


def longestPath(num, dist):
    if (num == mappedgoal):
        return dist

    visited[num] = True
    bst = -1
    for j in adj_list[num]:
        if (not visited[j[0]]):
            bst = max(bst, longestPath(j[0], dist+j[1]))
    visited[num] = False
    return bst


raw = open("AOC23.txt", "r")
inp = raw.read()

arr = []
cnt = 0
sx, sy, gx, gy = -1, -1, -1, -1

vertexcnt = 0
vertices = {}
for line in inp.splitlines():
    for i in range(len(line)):
        if (line[i] == '.'):
            if (cnt == 0):
                sx, sy = cnt, i
            elif (cnt == len(line)-1):
                gx, gy = cnt, i
            if (cnt == 0 or cnt == len(line)-1):
                vertices[(cnt, i)] = vertexcnt
                vertexcnt += 1

    arr.append(line)
    cnt += 1
n = len(arr)
for i in range(n):
    for j in range(n):
        if (arr[i][j] == '.'):
            tmp = 0
            for k in range(4):
                if (i + dx[k] >= 0 and i + dx[k] < n and j + dy[k] >= 0 and j + dy[k] < n and arr[i+dx[k]][j+dy[k]] != '#'):
                    tmp += 1
            if (tmp >= 3):
                vertices[(i, j)] = vertexcnt
                vertexcnt += 1

adj_list = [[] for _ in range(vertexcnt)]
visited = [[False for _ in range(n)] for _ in range(n)]
buildgraph(sx, sy, 0, (sx, sy))

mappedstart = vertices[(sx, sy)]
mappedgoal = vertices[(gx, gy)]

visited = [False for _ in range(vertexcnt)]
print(longestPath(mappedstart, 0))
