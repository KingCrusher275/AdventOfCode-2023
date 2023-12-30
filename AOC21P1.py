from collections import deque
test = \
    """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""
raw = open("AOC21.txt", "r")
inp = raw.read()

arr = []
for line in inp.splitlines():
    arr.append(line)

sx, sy = -1, -1
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if (arr[i][j] == 'S'):
            sx, sy = i, j

q = deque()
q.append((sx, sy, 0))

goaldist = 64
ans = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = set()
while (len(q) > 0):
    x, y, dist = q.popleft()
    if (dist == goaldist):
        ans += 1
    elif (dist > goaldist):
        break
    for i in range(4):
        if (x + dx[i] >= 0 and x + dx[i] < len(arr) and y + dy[i] >= 0 and y + dy[i] < len(arr[0]) and arr[x+dx[i]][y+dy[i]] != '#' and (x+dx[i], y+dy[i], dist+1) not in visited):
            q.append((x+dx[i], y+dy[i], dist+1))
            visited.add((x+dx[i], y+dy[i], dist+1))
print(ans)
