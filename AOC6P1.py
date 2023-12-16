test = \
    """Time:      7  15   30
Distance:  9  40  200
"""

raw = open('AOC6.txt', 'r')
inp = raw.read()


def bsearch(typ, time, dist):
    lo = 0
    hi = time

    if (typ == 0):
        ans = 1e10
    else:
        ans = -1

    while (lo <= hi):
        mid = (lo + hi) // 2
        if (mid * (time - mid) > dist):
            if (typ == 0):
                hi = mid - 1
                ans = min(ans, mid)
            else:
                lo = mid + 1
                ans = max(ans, mid)
        else:
            if (typ == 0):
                lo = mid + 1
            else:
                hi = mid - 1

    return ans


start = 1
times = []
dists = []
for line in inp.splitlines():
    nums = list(map(int, line.split(':')[1].split()))
    if (start == 1):
        times = nums
    else:
        dists = nums
    start += 1
ans = 1
for i in range(len(times)):
    lo = bsearch(0, times[i], dists[i])
    hi = bsearch(1, times[i], dists[i])
    ans *= (hi - lo + 1)

print(ans)
