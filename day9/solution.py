with open('input9.txt') as f:
    data = [int(line.rstrip()) for line in f.readlines()]

# Part one

def get_number(numbers, preamble):
	for i in range(preamble, len(numbers)):
		number = numbers[i]
		valid = False
		for j in range(i - preamble, i):
			for k in range(j, i):
				if(numbers[j] + numbers[k] == number):
					valid = True
					break
			if(valid):
				break
		if(not valid):
			return number

print(get_number(data,25))

# Part two

def get_contig_numbers(numbers, invalid_number):
    for i, num in enumerate(numbers): 
        line_index = 0
        result = [] 

        for number in numbers[i:len(numbers)]:
            result.append(number)
            line_index += number 

            if line_index == invalid_number:
                return result
    
    return False

bad_num = get_number(data,25)
print(min(get_contig_numbers(data,bad_num)) + max(get_contig_numbers(data,bad_num)))
