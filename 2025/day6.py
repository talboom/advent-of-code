import re
from utils import read_input

data = read_input("day6.txt")

# Part 1
rows = [[int(x) for x in re.findall(r'[+*]|\d+', d)] for d in data[:-1]]
operators = re.findall(r'[+*]', data[-1])
calcs = [1 if o == '*' else 0 for o in operators]

for numbers in rows:
  for i,n in enumerate(numbers):
    if operators[i] == '+':
      calcs[i] += n
    else:
      calcs[i] *= n

print(sum(calcs))
# 5316572080628

# Part 2
numbers = data[:-1]
operators = data[-1]

co = None
number = 0
sum_part2 = 0

i = 0
max_i = max(len(n) for n in numbers)
operators = operators + ' '*(max_i-len(operators))
# change it to max length 
for i,o in enumerate(operators):
  if o == '+' or o == '*':
    co = o
    sum_part2 += number
    number = 1 if co == '*' else 0

  # get number
  number_in_text = ''
  for j in range(len(numbers)):
    n_extend = numbers[j]  + ' '*(max_i-len(numbers[j]))
    n = n_extend[i]
    if n != ' ':
      number_in_text += n
  
  if number_in_text != '':
    if co == '+':
      number += int(number_in_text)
    else:
      number *= int(number_in_text)

sum_part2 += number

print(sum_part2)
# 11299263623062