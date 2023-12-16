import numpy as np
test = \
    """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

raw = open('AOC12.txt', 'r')
inp = raw.read()


def genSequence(pos, curStreak, chrs, vals, valsPos):
    if (valsPos == len(vals)):
        for i in range(pos, len(chrs)):
            if (chrs[i] == '#'):
                return 0
        return 1
    elif (pos == len(chrs)):
        if (valsPos == len(vals) - 1 and curStreak == vals[valsPos]):
            return 1
        return 0
    elif (curStreak > vals[valsPos]):
        return 0
    elif (dp[pos][valsPos][curStreak] != -1):
        return dp[pos][valsPos][curStreak]

    ans = 0
    if (chrs[pos] == '.'):
        if (curStreak == vals[valsPos]):
            ans += genSequence(pos+1, 0, chrs, vals, valsPos + 1)
        elif (curStreak == 0):
            ans += genSequence(pos+1, 0, chrs, vals, valsPos)
    elif (chrs[pos] == '#'):
        ans += genSequence(pos+1, curStreak+1, chrs, vals, valsPos)
    else:
        if (curStreak == vals[valsPos]):
            ans += genSequence(pos+1, 0, chrs, vals, valsPos + 1)
        elif (curStreak == 0):
            ans += genSequence(pos+1, 0, chrs, vals, valsPos)
        ans += genSequence(pos+1, curStreak+1, chrs, vals, valsPos)

    dp[pos][valsPos][curStreak] = ans
    return ans


recordChr = []
recordNum = []

for line in inp.splitlines():
    chrs, nums = line.split()
    nums = list(map(int, nums.split(',')))
    totalNums = []
    totalChrs = ""
    for i in range(5):
        if (i < 4):
            totalChrs += chrs + "?"
        else:
            totalChrs += chrs
        totalNums += nums
    recordChr.append(totalChrs)
    recordNum.append(totalNums)


ans = 0

for i in range(len(recordChr)):
    dp = np.zeros((105, 50, 20)) - 1
    ans += genSequence(0, 0, recordChr[i], recordNum[i], 0)
print(int(ans))
