with open('input2.txt') as file:
	data = file.readlines()

passlist = [ items.strip() for items in data ]

# Part one

valid_count = 0

for idx, entries in enumerate(passlist):

	original = entries.split(' ')
	letter_range = original[0].split('-')
	letter = original[1][:1]
	pass_entry = original[2]
	charcount = pass_entry.count(letter)

	if(int(letter_range[0]) <= charcount <= int(letter_range[1])):
		valid_count += 1

print(valid_count)

# Part two

valid_count_two = 0

for idx, entries in enumerate(passlist):

	original = entries.split(' ')
	letter_pos = original[0].split('-')
	letter = original[1][:1]
	pass_entry = original[2]

	first = pass_entry[int(letter_pos[0]) - 1]
	second = pass_entry[int(letter_pos[1]) - 1]
	
	if(first == letter and second != letter) or (second == letter and first != letter):
		valid_count_two += 1

print(valid_count_two)
