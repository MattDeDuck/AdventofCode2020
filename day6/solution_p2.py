with open('input6.txt') as file:
	data = file.read().split('\n\n')

def get_unique_count(group):
	char = set()
	for i in group:
		cnt = 0
		for j in i:
			if(sum(j in s for s in group) == len(group)):
				char.add(j)
	return len(char)

groups = []

for answers in data:
	groups.append(answers.split('\n'))

total = []
		
for ind in groups:
	total.append(get_unique_count(ind))

print(sum(total))
