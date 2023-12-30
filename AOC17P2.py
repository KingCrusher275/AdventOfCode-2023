import numpy as np
import heapq
import sys
test = \
    """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

test2 = \
    """111111111111
999999999991
999999999991
999999999991
999999999991
"""
raw = open("AOC17.txt", "r")
inp = raw.read()

arr = []

# 0 is North, 1 is East, 2 is South, 3 is West


def shortestPath(startdir):
    ans = int(1e10)
    pq = [(0, 0, 0, startdir)]
    while (len(pq) > 0):

        front = heapq.heappop(pq)
        x = front[1]
        y = front[2]
        di = front[3]

        if (front[0] == dist[x][y][di]):
            tmpdist = 0
            for i in range(1, 11):
                if (i == 10 and not (x == 0 and y == 0 and (di == 1 or di == 2))):
                    continue
                if (x + dx[di] * i >= 0 and x + dx[di] * i < len(arr) and y + dy[di] * i >= 0 and y + dy[di] * i < len(arr[0])):
                    tmpdist += arr[x + dx[di] * i][y + dy[di] * i]
                else:
                    break

                if (x + dx[di] * i == goalx and y + dy[di] * i == goaly and i >= 3):
                    ans = min(ans, dist[x][y][di] + tmpdist)

                if ((i < 4 and (x == 0 and y == 0 and (di == 1 or di == 2))) or i < 3):
                    continue
                for j in [1, 3]:
                    newx = x + dx[di] * i + dx[(di + j) % 4]
                    newy = y + dy[di] * i + dy[(di + j) % 4]
                    if (newx >= 0 and newx < len(arr) and newy >= 0 and newy < len(arr[0])):
                        if (dist[x][y][di] + tmpdist + arr[newx][newy] < dist[newx][newy][(di + j) % 4]):
                            dist[newx][newy][(di + j) % 4] = dist[x][y][di] + \
                                tmpdist + arr[newx][newy]
                            heapq.heappush(
                                pq, (dist[newx][newy][(di + j) % 4], newx, newy, (di + j) % 4))
    return ans


sys.setrecursionlimit(int(1e6))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for line in inp.splitlines():
    arr.append(list(map(int, list(line))))

goalx = len(arr)-1
goaly = len(arr[0])-1

ans = int(1e10)
dist = np.ones((len(arr), len(arr[0]), 4)) * int(1e10)
dist[0][0][1] = 0
ans = min(ans, shortestPath(1))

dist = np.ones((len(arr), len(arr[0]), 4)) * int(1e10)
dist[0][0][2] = 0
ans = min(ans, shortestPath(2))

print(ans)
