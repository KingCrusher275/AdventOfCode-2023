import numpy as np
import sys
test = \
    r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""
raw = open('AOC16.txt', 'r')
inp = raw.read()


# 0 North, 1 East, 2 South, 3 West

# x vertical, y horizontal


def computeVisited(arr):
    ans = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            found = False
            for k in range(4):
                if (visited[i][j][k] == 1):
                    found = True
            ans += found
    return ans


def recurseMaze(posx, posy, dir):
    if ((posx < 0 or posx >= len(arr) or posy < 0 or posy >= len(arr[0])) or not visited[posx][posy][dir] == 1):
        if (posy >= 0 and posx >= 0 and posy < len(arr[0]) and posx < len(arr)):
            visited[posx][posy][dir] = 1
        if (dir == 0):
            posx -= 1
        elif (dir == 1):
            posy += 1
        elif (dir == 2):
            posx += 1
        else:
            posy -= 1

        if (not (posx < 0 or posx >= len(arr) or posy < 0 or posy >= len(arr[0]))):

            if (arr[posx][posy] == '.'):
                recurseMaze(posx, posy, dir)
            elif (arr[posx][posy] == '/'):
                if (dir == 0):
                    recurseMaze(posx, posy, 1)
                elif (dir == 1):
                    recurseMaze(posx, posy, 0)
                elif (dir == 2):
                    recurseMaze(posx, posy, 3)
                else:
                    recurseMaze(posx, posy, 2)
            elif (arr[posx][posy] == "\\"):
                if (dir == 0):
                    recurseMaze(posx, posy, 3)
                elif (dir == 1):
                    recurseMaze(posx, posy, 2)
                elif (dir == 2):
                    recurseMaze(posx, posy, 1)
                else:
                    recurseMaze(posx, posy, 0)
            elif (arr[posx][posy] == "|"):
                if (dir == 0 or dir == 2):
                    recurseMaze(posx, posy, dir)
                else:
                    recurseMaze(posx, posy, 0)
                    recurseMaze(posx, posy, 2)
            else:
                if (dir == 1 or dir == 3):
                    recurseMaze(posx, posy, dir)
                else:
                    recurseMaze(posx, posy, 1)
                    recurseMaze(posx, posy, 3)


sys.setrecursionlimit(int(1e5))
arr = []
for line in inp.splitlines():
    arr.append(line)


mx = 0
for ii in range(len(arr)):
    visited = np.zeros((len(arr), len(arr[0]), 4))
    recurseMaze(ii, -1, 1)
    mx = max(mx, computeVisited(arr))
    visited = np.zeros((len(arr), len(arr[0]), 4))
    recurseMaze(ii, len(arr[0]), 3)
    mx = max(mx, computeVisited(arr))

for ii in range(len(arr[0])):
    visited = np.zeros((len(arr), len(arr[0]), 4))
    recurseMaze(-1, ii, 2)
    mx = max(mx, computeVisited(arr))
    visited = np.zeros((len(arr), len(arr[0]), 4))
    recurseMaze(len(arr), ii, 4)
    mx = max(mx, computeVisited(arr))
print(mx)
