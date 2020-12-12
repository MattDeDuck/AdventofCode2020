with open('input12.txt') as file:
	data = file.readlines()
	data = [ line.strip() for line in data ]

def change_dir(command, current_direction, dist):
	if(command == 'L'):
		if(current_direction == 'North'):
			if(dist == 90): return 'West'
			if(dist == 180): return 'South'
			if(dist == 270): return 'East'
		if(current_direction == 'East'):
			if(dist == 90): return 'North'
			if(dist == 180): return 'West'
			if(dist == 270): return 'South'
		if(current_direction == 'South'):
			if(dist == 90): return 'East'
			if(dist == 180): return 'North'
			if(dist == 270): return 'West'
		if(current_direction == 'West'):
			if(dist == 90): return 'South'
			if(dist == 180): return 'East'
			if(dist == 270): return 'North'
	if(command == 'R'):
		if(current_direction == 'North'):
			if(dist == 90): return 'East'
			if(dist == 180): return 'South'
			if(dist == 270): return 'West'
		if(current_direction == 'East'):
			if(dist == 90): return 'South'
			if(dist == 180): return 'West'
			if(dist == 270): return 'North'
		if(current_direction == 'South'):
			if(dist == 90): return 'West'
			if(dist == 180): return 'North'
			if(dist == 270): return 'East'
		if(current_direction == 'West'):
			if(dist == 90): return 'North'
			if(dist == 180): return 'East'
			if(dist == 270): return 'South'

def get_distance():
	x, y = 0, 0
	f = 'East'
	li = 0

	for line in data:
		cmd = line[:1]
		dist = int(line[1:])
				
		if(cmd == 'L' or cmd == 'R'):
			f = change_dir(cmd,f,dist)

		if(cmd != 'R' or cmd != 'L'):
			if(cmd == 'N'): y += dist
			if(cmd == 'E'):	x += dist
			if(cmd == 'S'):	y -= dist
			if(cmd == 'W'):	x -= dist
			
			if(cmd == 'F'):
				if(f == 'North'): y += int(dist)
				if(f == 'East'): x += int(dist)
				if(f == 'South'): y -= int(dist)
				if(f == 'West'): x -= int(dist)
		
	return (x,y), f

ship,facing = get_distance()

print(ship,facing)

print(f"Part 1: {abs(ship[0]) + abs(ship[1])}")
