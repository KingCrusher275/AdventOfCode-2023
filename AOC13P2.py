
test = \
    """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

raw = open('AOC13.txt', 'r')
inp = raw.read()


def checkSymmetric(arr, index, grid):
    off = 0
    iz = -1
    for i in range(index + 1):
        if (index + index - i + 1 < len(arr)):
            if (arr[i] != arr[index + index - i + 1]):
                off += 1
                iz = i
            if (off > 1):
                return False
    if (off != 1):
        return False

    off = 0
    for i in range(len(grid[iz])):
        if (grid[iz][i] != grid[index + index - iz + 1][i]):
            off += 1
    if (off != 1):
        return False
    return True


def solveGrid(grid, typ):
    global ans
    rowshash = {}
    rows = []
    cnt = 0
    for row in grid:
        if (row not in rowshash):
            rowshash[row] = cnt
            rows.append(cnt)
            cnt += 1
        else:
            rows.append(rowshash[row])

    for j in range(len(rows)-1):
        if (checkSymmetric(rows, j, grid)):

            ans += (j + 1) * typ
            return True
    return False


def transpose(arr):
    newArr = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            newArr[i][j] = arr[j][i]

        newArr[i] = ''.join(newArr[i])
    return newArr


allgrids = []
cur = []

for line in inp.splitlines():
    if (len(line) == 0):
        allgrids.append(cur)
        cur = []
    else:
        cur.append(line)
allgrids.append(cur)
ans = 0
for grid in allgrids:
    if (solveGrid(grid, 100)):
        continue
    else:
        newGrid = transpose(grid)
        solveGrid(newGrid, 1)

print(ans)
