import re
from utils import read_input

data = read_input("day1.txt")

rotations = [re.findall(r'[LR]|\d+', d) for d in data]

zeros = 0
clicks = 0
dial = 50
for r in rotations:
  start_dial = dial
  # ticks
  ticks = int(r[1])
  # full rounds
  clicks += ticks // 100
  # remove full rounds
  ticks_eff = ticks % 100
  dial += ticks_eff % 100 if (r[0] == 'R') else -ticks_eff
  # count crossing 0 if not started at 0
  clicks += (dial <= 0 or dial > 99) if start_dial > 0 else 0
  # set new dial
  dial = dial % 100
  # count when ending add zero
  zeros += (dial == 0)

print('part 1: ', zeros)
print('part 2: ', clicks)