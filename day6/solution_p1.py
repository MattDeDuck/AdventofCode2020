with open('input6.txt') as file:
	data = file.read().split('\n\n')
	data = [ line.replace('\n','') for line in data ]

unique_answers = [ set(i) for i in data ]

total = 0

for sets in unique_answers:
	total += len(sets)

print(total)
