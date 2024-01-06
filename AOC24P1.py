raw = open("AOC24.txt", "r")
inp = raw.read()

test = \
    """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

low, high = 200000000000000, 400000000000000
# low, high = 7, 27
positions, velocities = [], []

for line in inp.splitlines():
    pos, vel = line.split(' @ ')
    positions.append([int(x) for x in pos.split(', ')])
    velocities.append([int(x) for x in vel.split(', ')])

ans = 0
for i in range(len(positions)):
    for j in range(i+1, len(positions)):
        try:
            t2 = (positions[i][0] + velocities[i][0] * positions[j][1]/velocities[i][1] - velocities[i][0] * positions[i][1] /
                  velocities[i][1] - positions[j][0])/(velocities[j][0] - velocities[i][0] * velocities[j][1]/velocities[i][1])
            t1 = (positions[j][1] - positions[i][1] +
                  velocities[j][1] * t2)/velocities[i][1]

        except:
            continue
        if (t2 >= 0 and t1 >= 0):
            x = positions[j][0] + velocities[j][0] * t2
            y = positions[j][1] + velocities[j][1] * t2
            if (x >= low and x <= high and y >= low and y <= high):
                ans += 1

print(ans)
