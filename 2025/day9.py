from utils import read_input
import re

data = read_input('day9.txt')

tiles = [[int(i) for i in re.findall(r'\d+', d)] for d in data]

areas = []

for i,tile1 in enumerate(tiles[:-1]):
  for tile2 in tiles[i+1:]:
    area = (abs(tile1[0]-tile2[0])+1)*(abs(tile1[1]-tile2[1])+1)
    areas.append(area)

print(max(areas))
# 4750176210
