from utils import read_input

def find_antinodes(a1, a2):
    dx, dy = a1[0]-a2[0],a1[1]-a2[1]

    an1 = a1[0]+dx,a1[1]+dy
    an2 = a2[0]-dx,a2[1]-dy
    return an1, an2


data = read_input("day8_test.txt")

map = [list(d) for d in data]
map_height = len(map)
map_width = len(map[0])
antennas = {}
antinodes = []

for x,r in enumerate(map):
    for y,c in enumerate(r):
        if c != ".":
            if c not in antennas:
                antennas[c] = []
            antennas[c].append((x,y))

for s in antennas:
    a_temp = antennas[s]
    for i,a in enumerate(a_temp):
        for j,a2 in enumerate(a_temp[i+1:]):
            an1, an2 = find_antinodes(a, a2)
            for  an in [an1, an2]:
                if 0 <= an[0] < map_height and 0 <= an[1] < map_width and an not in antinodes:
                    antinodes.append(an)


print(len(antinodes))
