from utils import read_input

data = read_input("day4.txt")

map = [list(d) for d in data]

def clean_map(map, remove_rolls = False):
  map_height = len(map)
  map_width = len(map[0])
  n_rolls= 0

  for y in range(map_height):
    for x in range(map_width):
      xs = max(0,x-1)
      xe = min(map_width,x+2)
      ys = max(0,y-1)
      ye = min(map_height-1,y+1)

      r1 = map[ys][xs:xe] if y > 0 else []
      r2 = map[y][xs:xe]
      r3 = map[ye][xs:xe] if y < map_height-1 else []
      s = sum(c.count('@') for c in [r1,r2,r3]) 
      reachable = map[y][x] == '@' and sum(c.count('@') for c in [r1,r2,r3]) < 5
      if reachable and remove_rolls:
        map[y][x] = '*'
      n_rolls += reachable

  return n_rolls, map

# Part 1
print(clean_map(map)[0])

# Part 2
n_rolls = 0
while True:
  n_rolls_removed, map = clean_map(map, remove_rolls=True)
  n_rolls += n_rolls_removed
  if n_rolls_removed == 0:
    break

print(n_rolls)