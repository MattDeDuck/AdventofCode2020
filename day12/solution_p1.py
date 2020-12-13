with open('input12.txt') as file:
	data = file.readlines()
	data = [ line.strip() for line in data ]

nav = [ 'N', 'E', 'S', 'W' ]

def change_dir(facing,command,value):	
	f = nav.index(facing)
	if(command == 'R'):	f += value // 90
	if(command == 'L'): f -= value // 90
	f = f % 4
	return nav[f]

def get_ship_location():
	x, y = 0, 0
	face = 'E'

	for line in data:
		cmd, num = line[:1], int(line[1:])
		
		if(cmd == 'N') or (cmd == 'F' and face == 'N'): y += num
		elif(cmd == 'E') or (cmd == 'F' and face == 'E'): x += num
		elif(cmd == 'S') or (cmd == 'F' and face == 'S'): y -= num
		elif(cmd == 'W') or (cmd == 'F' and face == 'W'): x -= num

		if(cmd == 'L' or cmd == 'R'):
			face = change_dir(face,cmd,num)

	return abs(x) + abs(y)

print(f"Part 1: {get_ship_location()}")
