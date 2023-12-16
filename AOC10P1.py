from collections import deque
test = \
    """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

test2 = \
    """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

raw = open('AOC10.txt', 'r')
inp = raw.read()


def dfs(x, y, val, dir):
    # print(f"x: {x} y: {y}")

    while True:
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

action = ""
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(4):
    if (sx + dx[i] >= 0 and sx + dx[i] < len(arr) and sy + dy[i] >= 0 and sy + dy[i] < len(arr[0])):
        cur = arr[sx + dx[i]][sy + dy[i]]
        if (dx[i] == 1 and (cur == '|' or cur == 'L' or cur == 'J')):
            action = "D"
        elif (dx[i] == -1 and (cur == '|' or cur == '7' or cur == 'F')):
            action = "U"
        elif (dy[i] == -1 and (cur == '-' or cur == 'L' or cur == 'F')):
            action = "W"
        elif (dy[i] == 1 and (cur == '-' or cur == '7' or cur == 'J')):
            action = "E"

print(dfs(sx, sy, 0, action)//2)
