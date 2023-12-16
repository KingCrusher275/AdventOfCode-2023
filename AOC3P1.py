test = \
    """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
raw = open('AOC3.txt', 'r')
inp = raw.read()


def isNumber(c):
    if (ord(c) - ord('0') >= 0 and ord(c) - ord('0') <= 9):
        return True
    return False


def isSymbol(c):
    if (not isNumber(c) and ord(c) != 46):
        return True
    return False


def checkPos(i, j):
    for k in dx:
        for l in dy:
            if (i + k >= 0 and i + k < len(arr) and j + l >= 0 and j + l < len(arr[0])):
                if (isSymbol(arr[i + k][j + l])):
                    left = right = j
                    while (left - 1 >= 0 and isNumber(arr[i][left - 1])):
                        left -= 1
                    while (right + 1 < len(arr[0]) and isNumber(arr[i][right + 1])):
                        right += 1

                    return int(''.join(arr[i][left:right+1])), right
    return -1, -1


dx = [-1, 0, 1]
dy = [-1, 0, 1]
arr = [list(line) for line in inp.splitlines()]
ans = 0
i = j = 0
while (i < len(arr)):
    j = 0
    while (j < len(arr[0])):
        if (isNumber(arr[i][j])):
            val, pos = checkPos(i, j)
            if (val != -1):
                ans += val
                j = pos
        j += 1
    i += 1

print(ans)
