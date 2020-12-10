with open('input10.txt') as file:
	data = file.readlines()
	data = [ int(line.strip()) for line in data ]

def get_jolt_diffs(joltages):
	joltages.sort()
	
	diff_3 = 1
	diff_1 = 1

	for i in range(len(joltages) - 1):
		difference = joltages[i+1] - joltages[i]
		if(difference == 3):
			diff_3 += 1
		if(difference == 1):
			diff_1 += 1
	return diff_3, diff_1

three, one = get_jolt_diffs(data)

print(one * three)
