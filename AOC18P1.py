test = \
    """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

raw = open("AOC18.txt", "r")
inp = raw.read()

dirs = []
for line in inp.splitlines():
    dirs.append(line.split()[:2])

for i in range(len(dirs)):
    dirs[i][1] = int(dirs[i][1])
dx = {"U": -1, "L": 0, "R": 0, "D": 1}
dy = {"U": 0, "L": -1, "R": 1, "D": 0}

pts = [(0, 0)]
bpts = 0
for i in range(len(dirs)):
    pts.append((pts[-1][0] + dx[dirs[i][0]] * dirs[i][1],
               pts[-1][1] + dy[dirs[i][0]] * dirs[i][1]))
    bpts += dirs[i][1]
sm = 0
for i in range(len(pts)):
    sm += pts[i][0] * pts[(i+1) % len(pts)][1] - \
        pts[i][1] * pts[(i+1) % len(pts)][0]

sm = abs(sm)/2
interior = sm - bpts//2 + 1
print(interior + bpts)
