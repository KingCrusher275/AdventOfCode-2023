from collections import deque
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
visited = [[-1 for _ in range(len(arr[0]))] for _ in range(len(arr))]
visited[sx][sy] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while (len(q) > 0):
    x, y, dist = q.popleft()
    for i in range(4):
        if (x + dx[i] >= 0 and x + dx[i] < len(arr) and y + dy[i] >= 0 and y + dy[i] < len(arr[0]) and arr[x+dx[i]][y+dy[i]] != '#' and visited[x+dx[i]][y+dy[i]] == -1):
            q.append((x+dx[i], y+dy[i], dist+1))
            visited[x+dx[i]][y+dy[i]] = dist+1

n = 26501365 // len(arr)
oddcorners = evencorners = oddfull = evenfull = 0

wall = 0
for i in range(len(visited)):
    for j in range(len(visited[0])):
        if (visited[i][j] != -1):
            oddfull += visited[i][j] % 2
            evenfull += 1 - visited[i][j] % 2
            oddcorners += (visited[i][j] % 2 and visited[i][j] > 65)
            evencorners += (1 - visited[i][j] % 2 and visited[i][j] > 65)
        wall += visited[i][j] == -1

print((n+1)**2 * oddfull + n**2 * evenfull - (n+1)*oddcorners+n*evencorners)
