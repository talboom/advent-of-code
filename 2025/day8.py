from utils import read_input
from collections import defaultdict
import re

data = read_input('day8.txt')
junctions = [[int(x) for x in re.findall(r'\d+', d)] for d in data]

n_of_connections = 1000

distance = defaultdict(dict)
connections = []
shortest = []

# find n shortest distances
for i,juncA in enumerate(junctions[:-1]):
  for j,juncB in enumerate(junctions[i+1:]):
    d = (juncA[0]-juncB[0])**2 + (juncA[1]-juncB[1])**2 + (juncA[2]-juncB[2])**2
    if len(shortest) < n_of_connections:
      shortest.append(d)
      if len(shortest) == n_of_connections:
        shortest.sort()
    elif shortest[-1] > d:
      max_d = max(shortest)
      shortest[n_of_connections-1] = d
      shortest.sort()

    distance[i,j+1+i] = (juncA[0]-juncB[0])**2 + (juncA[1]-juncB[1])**2 + (juncA[2]-juncB[2])**2
distance = dict(sorted(distance.items(), key=lambda item: item[1]))
min_keys = [k for k, v in distance.items() if v <= shortest[-1]]

for min_key in min_keys:
  # find shortage connection
  cs = set()
  for i,c in enumerate(connections):
    if min_key[0] in c and min_key[1] in c:
      cs.add(i)
      break
    elif min_key[0] in c and len(cs) == 1:
      cs.add(i)
      break
    elif min_key[0] in c:
      cs.add(i)
    elif min_key[1] in c and len(cs) == 1:
      cs.add(i)
      break
    elif min_key[1] in c:
      cs.add(i)
  
  if len(cs) == 1:
    id = cs.pop()
    if min_key[0] not in connections[id]:
      connections[id].append(min_key[0]) 
    if min_key[1] not in connections[id]:
      connections[id].append(min_key[1])
  elif len(cs) == 2:
      i1 = cs.pop()
      i2 = cs.pop()
      connections[i1] += connections[i2]
      connections.remove(connections[i2])
  elif len(cs) > 2:
    print('error:')
    print(cs)
  else:
    connections.append([min_key[0],min_key[1]])

connections.sort(key=len, reverse= True)

print(len(connections[0])*len(connections[1])*len(connections[2]))
# 6840 too low

checking_set = set()

for d in distance:
  checking_set.add(d[0])
  checking_set.add(d[1])
  if len(checking_set) >= len(junctions):
    break

print(junctions[d[0]][0] * junctions[d[1]][0])