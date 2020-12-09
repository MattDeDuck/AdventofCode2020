from copy import deepcopy

with open('input8.txt') as f:
	data = f.readlines()
	data = [ line.strip() for line in data ]

# Part one

def total_acc():
	used = set()
	acc = 0
	line_index = 0

	while True:
		if(line_index >= len(data)):
			return acc
		instruction = data[line_index].split()
		cmd = instruction[0]
		num = int(instruction[1])
		if(line_index in used):
			return acc
		used.add(line_index)
		if(cmd == 'acc'):
			acc += num
			line_index += 1
		elif(cmd == 'jmp'):
			line_index += num
		elif(cmd == 'nop'):
			line_index += 1


print(f'Part 1: {total_acc()}')

# Part two

def get_acc(commands):
    acc = 0
    line_index = 0
    used = set()

    while True:
        if(line_index == len(commands) or line_index in used):
            break
        else:
            used.add(line_index)

        inst = commands[line_index]
        instructions_split = inst.split()
        cmd = instructions_split[0]
        num = int(instructions_split[1])

        if(cmd == 'acc'):
            acc += num
            line_index += 1
        if(cmd == 'jmp'):
            line_index += num
        if(cmd == 'nop'):
            line_index += 1

    return line_index, acc

for j, inst in enumerate(data):
    cmd = inst.split(' ')[0]
    if(cmd == 'nop' or cmd == 'jmp'):
        changed = deepcopy(data)

        if(cmd == 'nop'):
            changed[j] = 'jmp' + changed[j][3:]
        if(cmd == 'jmp'):
            changed[j] = 'nop' + changed[j][3:]

        final_acc = get_acc(changed)

        if(final_acc[0] == len(data)):
            break
    else:
        continue


print(f'Part 2: {final_acc[1]}')
