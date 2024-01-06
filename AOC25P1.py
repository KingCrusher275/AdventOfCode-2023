import copy
import sys
test = \
    """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

raw = open("AOC25.txt", "r")
inp = raw.read()

sys.setrecursionlimit(int(1e5))


def dfs(num, goal):
    visited[num] = True
    if (num == goal):
        return True

    for i in range(len(adj_list[num])):
        if (adj_list[num][i][1] and not visited[adj_list[num][i][0]]):
            if (dfs(adj_list[num][i][0], goal)):
                adj_list[num][i][1] = False
                return True
    return False


cur = 0
mpp = {}
for line in inp.splitlines():
    s1, s2 = line.split(': ')
    s2 = s2.split()
    if (s1 not in mpp):
        mpp[s1] = cur
        cur += 1
    for comp in s2:
        if comp not in mpp:
            mpp[comp] = cur
            cur += 1

adj_list = [[] for _ in range(len(mpp))]
for line in inp.splitlines():
    s1, s2 = line.split(': ')
    s2 = s2.split()

    for comp in s2:
        adj_list[mpp[s1]].append([mpp[comp], True])
        adj_list[mpp[comp]].append([mpp[s1], True])

mas = copy.deepcopy(adj_list)
visited = [False for _ in range(len(mpp))]
for i in range(1, len(adj_list)):
    adj_list = copy.deepcopy(mas)
    for k in range(4):
        visited = [False for _ in range(len(mpp))]
        dfs(0, i)

    if (not visited[i]):
        ans = 0
        for k in visited:
            ans += k

        print(ans * (len(adj_list) - ans))
        exit()
