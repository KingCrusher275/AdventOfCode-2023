from functools import cmp_to_key
test = \
    """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

raw = open('AOC7.txt', 'r')
inp = raw.read()

vals = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


def handType(hand):
    sortHand = sorted(hand)
    counts = []
    cnt = 1
    for i in range(len(hand) - 1):
        if (sortHand[i] == sortHand[i+1]):
            cnt += 1
        else:
            counts.append(cnt)
            cnt = 1
    counts.append(cnt)

    counts = sorted(counts)
    if (counts[-1] == 5):
        return 7
    elif (counts[-1] == 4):
        return 6
    elif (counts[-1] == 3 and counts[-2] == 2):
        return 5
    elif (counts[-1] == 3):
        return 4
    elif (counts[-1] == 2 and counts[-2] == 2):
        return 3
    elif (counts[-1] == 2):
        return 2
    else:
        return 1


def compare(item1, item2):
    h1 = handType(item1[0])
    h2 = handType(item2[0])
    if (h1 < h2):
        return -1
    elif (h2 < h1):
        return 1
    else:
        for i in range(len(item1[0])):
            if (vals[item1[0][i]] < vals[item2[0][i]]):
                return -1
            elif (vals[item1[0][i]] > vals[item2[0][i]]):
                return 1
        return 1


hands = []
for line in inp.splitlines():
    tmp = line.split()
    tmp[1] = int(tmp[1])
    hands.append(tmp)

hands = sorted(hands, key=cmp_to_key(compare))

# print(handType('T55J5'))
# print(hands)
ans = 0
for i in range(len(hands)):
    ans += hands[i][1] * (i + 1)

print(ans)
