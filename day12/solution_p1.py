
Save New Duplicate & Edit Just Text Twitter
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
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
