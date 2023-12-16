test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

input = open("AOC1.txt", "r")
stuff = input.read()

sm = 0
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in stuff.splitlines():
    first = True
    firstNum = -1
    lastNum = -1
    for ix in range(len(line)):
        if (ord(line[ix]) - ord('0') >= 0 and ord(line[ix]) - ord('0') <= 9):
            if (first):
                firstNum = ord(line[ix]) - ord('0')
                first = False
            else:
                lastNum = ord(line[ix]) - ord('0')
        else:
            for i in range(len(nums)):
                if (line[ix:].startswith(nums[i])):
                    if (first):
                        firstNum = i + 1
                        first = False
                    else:
                        lastNum = i + 1
    if (lastNum == -1):
        lastNum = firstNum

    # print(f"{firstNum} {lastNum}")
    sm += 10 * firstNum + lastNum

print(sm)
