from utils import read_input

data = read_input("day7.txt")

map = [list(d) for d in data]
map_height = len(map)
map_width = len(map[0])

beam_y = set(i for i,c in enumerate(map[0]) if c == 'S')

count_split = 0
for y in range(1,map_height):
  new_beam_y = set()
  for b in beam_y:
    loc = map[y][b]
    if loc == '^':
      count_split += 1
      new_beam_y.add(b-1) 
      new_beam_y.add(b+1)
    else:
      new_beam_y.add(b)
  beam_y = new_beam_y

print(count_split)
# 1660

beam_y = {i:1 for i,c in enumerate(map[0]) if c == 'S'}

for y in range(1,map_height):
  new_beam_y = {}
  for b in beam_y:
    loc = map[y][b]
    if loc == '^':
      if (b-1) not in new_beam_y:
        new_beam_y[b-1] = beam_y[b]
      else:
        new_beam_y[b-1] += beam_y[b]
        
      if (b+1) not in new_beam_y:
        new_beam_y[b+1] = beam_y[b]
      else:
        new_beam_y[b+1] += beam_y[b]
    else:
      if b not in new_beam_y:
        new_beam_y[b] = beam_y[b]
      else:
        new_beam_y[b] += beam_y[b]
  beam_y = new_beam_y

result = sum(beam_y.values())

print(result)
# 305999729392659