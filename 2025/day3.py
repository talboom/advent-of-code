from utils import read_input

def get_joltage (bank, digits):
  joltage = 0
  bank_rel = bank
  for i in reversed(range(digits)):
    if i > 0:
      mv = max(bank_rel[:-i])
    else:
      mv = max(bank_rel)
    mi = bank_rel.index(mv)
    joltage += mv * 10**(i)
    bank_rel = bank_rel[mi+1:]
  return joltage 

data = read_input("day3.txt")
banks = [[int(x) for x in d] for d in data]

joltage_part1 = 0
for bank in banks:
  joltage_part1 +=  get_joltage(bank,2)

print(joltage_part1)


joltage_part2 = 0
for bank in banks:
  joltage_part2 += get_joltage(bank,12) 

print(joltage_part2)
