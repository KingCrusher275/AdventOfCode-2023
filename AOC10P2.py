import sys
test = \
    """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

test2 = \
    """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

test3 = \
    """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

test4 = \
    """S---7
L--7|
F7.||
|L-J|
L---J
"""

test5 = \
    """S-7F7
L7LJ|
FJ.FJ
|F7L7
LJL-J
"""

test6 = \
    """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

test7 = \
    """
..S7.
.|.L7
.|FFJ
.LJJ.
.....
"""

raw = open('AOC10.txt', 'r')
inp = raw.read()


def ffill(x, y):
    if (not visited[x][y] and not wall[x][y]):
        visited[x][y] = True
        for i in range(4):
            if (x + dx[i] >= 0 and x + dx[i] < len(arr) and y + dy[i] >= 0 and y + dy[i] < len(arr[0]) and not wall[x + dx[i]][y + dy[i]]):
                ffill(x + dx[i], y + dy[i])


def dfs2(x, y, val, dir):
    startx = x
    starty = y

    while True:
        cur = arr[x][y]
        if (dir == "W"):
            if (x + 1 < len(arr)):
                ffill(x+1, y)
        elif (dir == "E"):
            if (x - 1 >= 0):
                ffill(x-1, y)
        elif (dir == "D"):
            if (y + 1 < len(arr[0])):
                ffill(x, y + 1)
        elif (dir == "U"):
            if (y - 1 >= 0):
                ffill(x, y - 1)

        if (x == startx and y == starty and val != 0):
            return val
        if ((cur == '7' and dir == "E") or (cur == 'F' and dir == "W") or (cur == '|' and dir == "D")):
            if (y + 1 < len(arr[0])):
                ffill(x, y + 1)
            x = x+1
            dir = "D"
        elif ((cur == 'J' and dir == "E") or (cur == 'L' and dir == "W") or (cur == '|' and dir == "U")):
            if (y - 1 >= 0):
                ffill(x, y - 1)
            x = x-1
            dir = "U"
        elif ((cur == '-' and dir == "E") or (cur == 'L' and dir == "D") or (cur == 'F' and dir == "U")):
            if (x - 1 >= 0):
                ffill(x-1, y)
            y = y+1
            dir = "E"
        elif ((cur == '-' and dir == "W") or (cur == '7' and dir == "U") or (cur == 'J' and dir == "D")):
            if (x + 1 < len(arr)):
                ffill(x+1, y)
            y = y-1
            dir = "W"
        val += 1


def dfs(x, y, val, dir):
    while True:
        wall[x][y] = True
        cur = arr[x][y]
        if (cur == "S" and val != 0):
            return val
        if ((cur == "S" and dir == "D") or (cur == '7' and dir == "E") or (cur == 'F' and dir == "W") or (cur == '|' and dir == "D")):
            x = x+1
            dir = "D"
        elif ((cur == "S" and dir == "U") or (cur == 'J' and dir == "E") or (cur == 'L' and dir == "W") or (cur == '|' and dir == "U")):
            x = x-1
            dir = "U"
        elif ((cur == "S" and dir == "E") or (cur == '-' and dir == "E") or (cur == 'L' and dir == "D") or (cur == 'F' and dir == "U")):
            y = y+1
            dir = "E"
        elif ((cur == "S" and dir == "W") or (cur == '-' and dir == "W") or (cur == '7' and dir == "U") or (cur == 'J' and dir == "D")):
            y = y-1
            dir = "W"
        val += 1


sys.setrecursionlimit(int(1e5))
sx = -1
sy = -1
arr = []
start = 0
for line in inp.splitlines():
    arr.append(list(line))
    for i in range(len(line)):
        if (line[i] == 'S'):
            sy = i
            sx = start
    start += 1

visited = [[False for _ in range(len(arr[0]))] for _ in range(len(arr))]
wall = [[False for _ in range(len(arr[0]))] for _ in range(len(arr))]
action = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(4):
    if (sx + dx[i] >= 0 and sx + dx[i] < len(arr) and sy + dy[i] >= 0 and sy + dy[i] < len(arr[0])):
        cur = arr[sx + dx[i]][sy + dy[i]]
        if (dx[i] == 1 and (cur == '|' or cur == 'L' or cur == 'J')):
            action.append("D")
        elif (dx[i] == -1 and (cur == '|' or cur == '7' or cur == 'F')):
            action.append("U")
        elif (dy[i] == -1 and (cur == '-' or cur == 'L' or cur == 'F')):
            action.append("W")
        elif (dy[i] == 1 and (cur == '-' or cur == '7' or cur == 'J')):
            action.append("E")

dfs(sx, sy, 0, action[0])
action = sorted(action)
if (action[0] == "D" and action[1] == "U"):
    arr[sx][sy] = "|"
elif (action[0] == "E" and action[1] == "W"):
    arr[sx][sy] = "-"
elif (action[0] == "U" and action[1] == "W"):
    arr[sx][sy] = "J"
elif (action[0] == "D" and action[1] == "W"):
    arr[sx][sy] = "7"
elif (action[0] == "D" and action[1] == "E"):
    arr[sx][sy] = "F"
else:
    arr[sx][sy] = "L"

done = False
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if (wall[i][j]):
            dfs2(i, j, 0, "W")
            done = True
            break
    if (done):
        break


ans = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        ans += visited[i][j]
print(ans)
