import math
raw = open('AOC2.txt', 'r')
inp = raw.read()

test = \
    """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

ans = 0
start = 1
for game in inp.splitlines():
    filt = game[(math.floor(math.log10(start)) + 8):]
    # print(start)
    possible = True
    turns = filt.split(';')
    for turn in turns:
        subturn = turn.split(',')

        for element in subturn:
            number, color = element.split()
            if (color == "red" and int(number) > 12):
                possible = False
            elif (color == "green" and int(number) > 13):
                possible = False
            elif (color == "blue" and int(number) > 14):
                possible = False
    if (possible):
        ans += start
    start += 1

print(ans)
