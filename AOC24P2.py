from sympy import solve
from sympy.abc import w, x, y, z

raw = open("AOC24.txt", "r")
inp = raw.read()

test = \
    """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

positions, velocities = [], []

for line in inp.splitlines():
    pos, vel = line.split(' @ ')
    positions.append([int(x) for x in pos.split(', ')])
    velocities.append([int(x) for x in vel.split(', ')])


equations = []


for i in range(4):
    equations.append((x-positions[i][0])*(velocities[i][1]-y) - (z-positions[i][1])*(velocities[i][0]-w))

solutions = solve(equations, w, x, y, z, dict=True)
# print(solutions)
px, py = solutions[0][x], solutions[0][z]
equations.clear()
for i in range(4):
    equations.append((x-positions[i][0])*(velocities[i][2]-y) - (z-positions[i][2])*(velocities[i][0]-w))

solutions = solve(equations, w, x, y, z, dict=True)
# print(solutions)
pz = solutions[0][z]

print(px, py, pz)
print(px+py+pz)

