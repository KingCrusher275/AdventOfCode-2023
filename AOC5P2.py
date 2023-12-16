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

abcdefg
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
        spl = tmp.split()
        for i in range(0, len(spl), 2):
            nums.append((int(spl[i]), int(spl[i+1]) + int(spl[i])))
    elif (len(line) == 0):
        pass
    elif (isLetter(line[0])):
        transformed = []
        for rang in maps:
            i = 0
            newNums = []
            while (i < len(nums)):
                if (max(nums[i][0], rang[1]) <= min(nums[i][1], rang[1] + rang[2])):
                    loff = max(nums[i][0], rang[1]) - rang[1]
                    hoff = min(nums[i][1], rang[1] + rang[2] - 1) - rang[1]
                    transformed.append((rang[0] + loff, rang[0] + hoff))
                    if (nums[i][0] < rang[1]):
                        newNums.append((nums[i][0], rang[1] - 1))
                    if (nums[i][1] >= rang[1] + rang[2]):
                        newNums.append((rang[1] + rang[2], nums[i][1]))
                else:
                    newNums.append(nums[i])
                i += 1
            nums = newNums

        for elem in nums:
            transformed.append(elem)

        nums = transformed
        maps = []
    elif (isNumber(line[0])):
        start1, start2, ran = map(int, line.split())
        maps.append((start1, start2, ran))
    start += 1

print(sorted(nums, key=lambda x: x[0])[0][0])
