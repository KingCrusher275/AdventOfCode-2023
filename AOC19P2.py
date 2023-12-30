import copy
test = \
    """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""
raw = open("AOC19.txt", "r")
inp = raw.read()


def computeAns(rang):
    ans = 1
    for adj in rang:
        ans = ans * (adj[1]-adj[0]+1)
    return ans


def dfs(rang, instruction):

    global ans
    for diff in rang:
        if (diff[0] > diff[1]):
            return
    for cond in conditions[instruction]:

        trang = copy.deepcopy(rang)
        if (len(cond) == 1):
            if (len(cond[0]) == 1):
                if (cond[0] == 'A'):
                    ans += computeAns(rang)

            else:
                dfs(rang, cond[0])
            return

        if (cond[0][1] == '<'):
            trang[ratings[cond[0][0]]][1] = min(
                trang[ratings[cond[0][0]]][1], int(cond[0][2:])-1)

            if (len(cond[1]) == 1):
                if (cond[1][0] == 'A'):
                    ans += computeAns(trang)
            else:
                dfs(trang, cond[1])
            rang[ratings[cond[0][0]]][0] = max(
                rang[ratings[cond[0][0]]][0], int(cond[0][2:]))
        else:
            trang[ratings[cond[0][0]]][0] = max(
                trang[ratings[cond[0][0]]][0], int(cond[0][2:])+1)
            if (len(cond[1]) == 1):
                if (cond[1][0] == 'A'):
                    ans += computeAns(trang)
            else:
                dfs(trang, cond[1])
            rang[ratings[cond[0][0]]][1] = min(
                rang[ratings[cond[0][0]]][1], int(cond[0][2:]))


workflows, parts = inp.split("\n\n")
ratings = {'x': 0, 'm': 1, 'a': 2, 's': 3}
conditions = {}
partNums = []
for line in workflows.splitlines():
    identifier, rest = line.split('{')
    rest = rest[:-1]
    conditions[identifier] = [tmp.split(':') for tmp in rest.split(',')]

ans = 0
dfs([[1, 4000], [1, 4000], [1, 4000], [1, 4000]], 'in')
print(ans)
