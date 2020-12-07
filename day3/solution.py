with open('input3.txt') as file:
	datamap = file.readlines()

map = [ row.strip() for row in datamap ]

# Part one

trees = 0
row, col = 0, 0

while row + 1 < len(map):
	row += 1
	col += 3

	boundary = (col % len(map[row]))
	area = map[row][boundary]

	if(area == '#'):
		trees += 1

print(trees)

# Part two

paths = [ (1,1),(3,1),(5,1),(7,1),(1,2) ]

total = 1

for attempts in paths:
	treess = 0
	row, col = 0, 0

	while row + 1 < len(map):
		row += attempts[1]
		col += attempts[0]

		boundary = (col % len(map[row]))
		area = map[row][boundary]

		if(area == '#'):
			treess += 1

	total *= treess

print(total)
