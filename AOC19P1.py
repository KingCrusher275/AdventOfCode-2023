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

workflows, parts = inp.split("\n\n")
ratings = {'x': 0, 'm': 1, 'a': 2, 's': 3}
conditions = {}
partNums = []
for line in parts.splitlines():
    cats = line[1:-1].split(',')
    for i in range(len(cats)):
        cats[i] = int(cats[i][2:])
    partNums.append(cats)
for line in workflows.splitlines():
    identifier, rest = line.split('{')
    rest = rest[:-1]
    conditions[identifier] = [tmp.split(':') for tmp in rest.split(',')]

ans = 0
for part in partNums:
    curWf = 'in'
    while True:
        for order in conditions[curWf]:
            done = False
            if (len(order) == 1):
                if (len(order[0]) == 1):
                    done = True
                    if (order[0] == 'A'):
                        ans += sum(part)
                else:
                    curWf = order[0]
                break
            else:

                if (order[0][1] == '<'):

                    if (part[ratings[order[0][0]]] < int(order[0][2:])):

                        if (len(order[1]) == 1):
                            done = True
                            if (order[1] == 'A'):
                                ans += sum(part)
                        else:
                            curWf = order[1]
                        break
                elif (order[0][1] == '>'):
                    if (part[ratings[order[0][0]]] > int(order[0][2:])):
                        if (len(order[1]) == 1):
                            done = True
                            if (order[1] == 'A'):
                                ans += sum(part)
                        else:
                            curWf = order[1]
                        break
        if (done):
            break

print(ans)
