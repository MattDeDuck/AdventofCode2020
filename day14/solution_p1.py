with open('input14.txt') as file:
	data = file.readlines()
	data = [ line.strip() for line in data ]

def to_binary(dec):
	return "{0:036b}".format(dec)

def to_dec(bin):
	return int(bin,2)

def get_total():
	final_mem = {}
	total = 0
	
	for line in data:
		line = line.split(' = ')

		if 'mask' in line[0]:
	           bit_mask = line[1]
		else:
			mem_add = line[0][4:-1]
			value = int(line[1])
			bin_value = list(to_binary(value))

			for i in range(len(bit_mask)):
				if(bit_mask[i] != 'X'):
					bin_value[i] = bit_mask[i]

			mem_masked = ''.join(bin_value)
			mem_masked_value = to_dec(mem_masked)
			if(mem_masked_value != 0):
				final_mem[mem_add] = mem_masked_value
				
	return sum(final_mem.values())			

print(get_total())
