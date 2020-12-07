with open('input1.txt') as f:
	data = f.readlines()

numbers = [ int(nums.strip()) for nums in data ]

totalnumber = 2020

# Part one

for i, number in enumerate(numbers):
	for j in range(i+1, len(numbers)):
		total = numbers[i] + numbers[j]
		if(total == totalnumber):
			print(numbers[i] * numbers[j])

# Part two

for i, number in enumerate(numbers):
	for j in range(i+1, len(numbers)):
		for k in range(j+1, len(numbers)):
			total = numbers[i] + numbers[j] + numbers[k]
			if(total == totalnumber):
				print(numbers[i] * numbers[j] * numbers[k])
