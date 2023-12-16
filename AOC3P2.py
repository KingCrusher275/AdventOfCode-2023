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
    val = []
    used = set()
    for k in dx:
        for l in dy:
            if (i + k >= 0 and i + k < len(arr) and j + l >= 0 and j + l < len(arr[0])):
                if (isNumber(arr[i + k][j + l]) and (i+k, j+l) not in used):
                    used.add((i+k, j+l))
                    left = right = j+l
                    while (left - 1 >= 0 and isNumber(arr[i+k][left - 1])):
                        left -= 1
                        used.add((i+k, left))
                    while (right + 1 < len(arr[0]) and isNumber(arr[i+k][right + 1])):
                        right += 1
                        used.add((i+k, right))

                    val.append(int(''.join(arr[i+k][left:right+1])))

    if (len(val) == 2):
        return val[0] * val[1]
    return -1


dx = [-1, 0, 1]
dy = [-1, 0, 1]
arr = [list(line) for line in inp.splitlines()]
ans = 0
i = j = 0
while (i < len(arr)):
    j = 0
    while (j < len(arr[0])):
        if (arr[i][j] == '*'):
            val = checkPos(i, j)
            if (val != -1):
                ans += val
        j += 1
    i += 1

print(ans)
