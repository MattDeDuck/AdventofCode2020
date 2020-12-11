with open('input10.txt') as file:
	data = file.readlines()
	data = [ int(line.strip()) for line in data ]

data.sort()
data = [0] + data
data.append(data[-1] + 3)

# Part one

def get_jolt_differences(joltages):
	diff_1 = 0
	diff_3 = 0

	for i in range(len(joltages)-1):
		difference = joltages[i+1] - joltages[i]
		if(difference == 1):
			diff_1 += 1
		if(difference == 3):
			diff_3 += 1
	return diff_1 * diff_3

diff = get_jolt_differences(data)

print(f"Part one: {diff}")


# Part two

visited = {}

def get_routes(number):	
	if(number == len(data)-1):
		return 1

	if(number in visited):
		return visited[number]

	t_routes = 0
	for i in range(number+1, len(data)):
		if(data[i] - data[number] <= 3):
			t_routes += get_routes(i)

	visited[number] = t_routes
	return t_routes

routes = get_routes(0)

print(f"Part two: {routes}")
