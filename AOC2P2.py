import math

test = \
    """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

raw = open('AOC2.txt', 'r')
inp = raw.read()

ans = 0
start = 1
for game in inp.splitlines():
    filt = game[(math.floor(math.log10(start)) + 8):]
    mxred = mxblue = mxgreen = 0
    turns = filt.split(';')
    for turn in turns:
        subturn = turn.split(',')

        for element in subturn:
            number, color = element.split()
            number = int(number)
            if (color == "red"):
                mxred = max(mxred, number)
            elif (color == "green"):
                mxgreen = max(mxgreen, number)
            elif (color == "blue"):
                mxblue = max(mxblue, number)

    ans += mxred * mxgreen * mxblue
    start += 1

print(ans)
