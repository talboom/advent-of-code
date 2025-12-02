from utils import read_input

def valid_id(id):
  hp = len(str(id)) // 2
  return id // (10**hp) == id % (10**hp)

def valid_id2(id):
  id_str = str(id)
  hp = len(id_str) // 2
  for i in range (1,hp+1):
    if len(id_str) % i == 0:
      parts = []
      for j in range(0, len(id_str), i):
        parts.append(id_str[j:j+i])
        if len(set(parts)) > 1:
          break
      if len(set(parts)) == 1:
        return True
  return False
        
data = read_input("day2.txt")

ranges =  [d.split('-') for d in data[0].split(',')]

sum_part1 = 0
for r in ranges:
  r1 = int(r[0])
  r2 = int(r[1])
  for n in range(r1,r2+1):
    sum_part1 += n * (valid_id(n))

print(sum_part1)

sum_part2 = 0
for r in ranges:
  r1 = int(r[0])
  r2 = int(r[1])
  for n in range(r1,r2+1):
    sum_part2 += n * (valid_id2(n))

print(sum_part2)
  