test = \
    """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

raw = open('AOC5.txt', 'r')
inp = raw.read()


def isNumber(c):
    if (ord(c) - ord('0') >= 0 and ord(c) - ord('0') <= 9):
        return True
    return False


def isLetter(c):
    if (ord(c) - ord('a') >= 0 and ord(c) - ord('a') <= 25):
        return True
    return False


start = 1
nums = []
maps = []
for line in inp.splitlines():
    if (start == 1):
        tmp = line[7:]
        for num in tmp.split():
            nums.append(int(num))
    elif (len(line) == 0):
        pass
    elif (isLetter(line[0])):
        newNums = []
        for num in nums:
            found = False
            for rang in maps:
                if (num >= rang[1] and num < rang[1] + rang[2]):
                    found = True
                    newNums.append(rang[0] + (num - rang[1]))

            if (not found):
                newNums.append(num)
        nums = newNums
        maps = []

    elif (isNumber(line[0])):
        start1, start2, ran = map(int, line.split())
        maps.append((start1, start2, ran))
    start += 1

newNums = []
for num in nums:
    found = False
    for rang in maps:
        if (num >= rang[1] and num < rang[1] + rang[2]):
            found = True
            newNums.append(rang[0] + (num - rang[1]))

    if (not found):
        newNums.append(num)
nums = newNums

nums = newNums
maps = {}

print(sorted(nums)[0])
