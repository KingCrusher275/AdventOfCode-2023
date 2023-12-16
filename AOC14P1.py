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

arr = []
for line in inp.splitlines():
    arr.append(line)

ans = 0
for j in range(len(arr[0])):
    nx = -1
    for i in range(len(arr)):
        if (arr[i][j] == 'O'):
            ans += len(arr) - nx - 1
            nx += 1
        elif (arr[i][j] == '#'):
            # ans += len(arr) - i
            nx = i

print(ans)
