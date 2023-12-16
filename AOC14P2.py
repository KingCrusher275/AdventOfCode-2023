test = \
    """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

raw = open('AOC14.txt', 'r')
inp = raw.read()


def north(grid):
    for j in range(len(grid[0])):
        nx = 0
        for i in range(len(grid)):
            if (grid[i][j] == '#'):
                nx = i + 1
            elif (grid[i][j] == 'O'):
                grid[i][j] = '.'
                grid[nx][j] = 'O'
                nx += 1


def south(grid):
    for j in range(len(grid[0])):
        nx = len(grid)-1
        for i in reversed(range(len(grid))):
            if (grid[i][j] == '#'):
                nx = i - 1
            elif (grid[i][j] == 'O'):
                grid[i][j] = '.'
                grid[nx][j] = 'O'
                nx -= 1


def west(grid):
    for i in range(len(grid)):
        nx = 0
        for j in range(len(grid[0])):
            if (grid[i][j] == '#'):
                nx = j + 1
            elif (grid[i][j] == 'O'):
                grid[i][j] = '.'
                grid[i][nx] = 'O'
                nx += 1


def east(grid):
    for i in range(len(grid)):
        nx = len(arr[0])-1
        for j in reversed(range(len(grid[0]))):
            if (grid[i][j] == '#'):
                nx = j - 1
            elif (grid[i][j] == 'O'):
                grid[i][j] = '.'
                grid[i][nx] = 'O'
                nx -= 1


arr = []
for line in inp.splitlines():
    arr.append(list(line))
cnt = 0

mpp = {}
while (''.join([''.join(v) for v in arr]) not in mpp):
    mpp[''.join([''.join(v) for v in arr])] = cnt
    north(arr)
    west(arr)
    south(arr)
    east(arr)
    cnt += 1

first = mpp[''.join([''.join(v) for v in arr])]

iters = 1000000000
for i in range((iters - first) % (cnt - first)):
    north(arr)
    west(arr)
    south(arr)
    east(arr)

ans = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if (arr[i][j] == 'O'):
            ans += len(arr) - i

print(ans)
