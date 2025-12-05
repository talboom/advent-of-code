import re
from utils import read_input

def stitch(ranges):
  ranges.sort(key=lambda x: x[0])
  ranges_stitched = []
  start_new = ranges[0][0]
  end_prev = ranges[0][1]
  for r in ranges[1:]:
    start, end = r
    if start > end:
      print(r)
    if start > end_prev:
      ranges_stitched.append((start_new,end_prev))
      start_new = start
    end_prev = max(end,end_prev)

  ranges_stitched.append((start_new,end_prev))
  return ranges_stitched


data = read_input("day5.txt")

first_section = True
ranges = []
ids = []

for d in data:
  if d == '':
    first_section = False
  elif first_section:
    start,end = [int(x) for x in re.findall(r'\d+', d)]
    ranges.append([start,end])
  else:
    ids.append(int(d))

ranges = stitch(ranges)

# part 1
ingr_count = 0 

for id in ids:
  for r in ranges:
    start,end = r
    if start <= id <= end: 
      ingr_count += 1
      break

print(ingr_count)
# 744

# part 2
n_ingredients = 0
for r in ranges:
  n_ingredients += r[1]-r[0]+1

print(n_ingredients)
# 347468726696961