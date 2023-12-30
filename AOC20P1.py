from collections import deque
test = \
    r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

test2 = \
    r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""
raw = open("AOC20.txt", "r")
inp = raw.read()

q = deque()

moduleTypes = {}
conjInputs = {}
ffstate = {}
moduleOutputs = {}
for line in inp.splitlines():
    input, outputs = line.split(" -> ")

    if (input[0] == '&'):
        name = input[1:]
        moduleTypes[name] = 0
        moduleOutputs[name] = outputs.split(', ')
    elif (input[0] == '%'):
        name = input[1:]
        moduleTypes[name] = 1
        ffstate[name] = 0
        moduleOutputs[name] = outputs.split(', ')
    else:
        moduleTypes[input] = 2
        moduleOutputs[input] = outputs.split(', ')

for input, outputs in moduleOutputs.items():
    for output in outputs:
        if (output in moduleTypes and moduleTypes[output] == 0):
            if (output not in conjInputs):
                conjInputs[output] = {input: 0}
            else:
                conjInputs[output][input] = 0

low = 0
high = 0
for _ in range(1000):
    low += 1
    for output in moduleOutputs['broadcaster']:
        q.appendleft(('broadcaster', output, 0))
        low += 1
    while (len(q) > 0):
        inp, out, typ = q.popleft()
        if (out not in moduleTypes):
            continue
        elif (moduleTypes[out] == 0):
            conjInputs[out][inp] = typ
            allHigh = True
            for key, value in conjInputs[out].items():
                if (value == 0):
                    allHigh = False
            if (allHigh):
                for next in moduleOutputs[out]:
                    q.appendleft((out, next, 0))
                    low += 1
            else:
                for next in moduleOutputs[out]:
                    q.appendleft((out, next, 1))
                    high += 1
        elif (moduleTypes[out] == 1):
            if (typ == 0):
                if (ffstate[out] == 0):
                    ffstate[out] = 1
                    for next in moduleOutputs[out]:
                        q.appendleft((out, next, 1))
                        high += 1
                else:
                    ffstate[out] = 0
                    for next in moduleOutputs[out]:
                        q.appendleft((out, next, 0))
                        low += 1
print(low * high)
