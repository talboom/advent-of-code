from utils import read_input

data = read_input("day4.txt")

puzzle = [list(d) for d in data]

max_x = len(puzzle)
max_y = len(puzzle[0])

directions = [
    [0, 1],  # right
    [1, 1],  # down-right
    [1, 0],  # down
    [1, -1], # down-left
    [0, -1], # left
    [-1, -1], # up-left
    [-1, 0], # up
    [-1, 1]  # up-right
]
x_positions = []
search_word = "XMAS"
result_part1 = 0

for x,r in enumerate(puzzle):
    for y,c in enumerate(r):
        if c == "X":
            x_positions.append((x,y))

for x, y in x_positions:
    for dx, dy in directions:
        x_cursor, y_cursor, xmas_index = x, y, 1
        while True:
            x_cursor += dx
            y_cursor += dy
            if not(0 <= x_cursor < max_x and 0 <= y_cursor < max_y):
                break
            if xmas_index < len(search_word) and puzzle[x_cursor][y_cursor] == search_word[xmas_index]:
                xmas_index += 1
                if xmas_index == len(search_word):
                    result_part1 += 1
                    break
            else:
                break

print(result_part1)

a_positions = []
result_part2 = 0

for x,r in enumerate(puzzle):
    for y,c in enumerate(r):
        if c == "A":
            a_positions.append((x,y))

for x,y in a_positions:
    if 1 <= x < max_x-1 and 1 <= y < max_y-1:
        topleft_to_botright = (puzzle[x+1][y+1] == "M" and puzzle[x-1][y-1] == "S") or (puzzle[x+1][y+1] == "S" and puzzle[x-1][y-1] == "M")
        botleft_to_topright = (puzzle[x+1][y-1] == "M" and puzzle[x-1][y+1] == "S") or (puzzle[x+1][y-1] == "S" and puzzle[x-1][y+1] == "M")

        if (topleft_to_botright and botleft_to_topright):
            result_part2 +=1

print(result_part2)
