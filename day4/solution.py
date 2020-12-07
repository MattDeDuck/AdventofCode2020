import re

with open('input4.txt') as file:
	data = file.read().split("\n\n")

# Part one

sections = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]

valid = 0

for line in data:
    line = line.replace("\n", " ")
    
    fieldCheck = all(fields in line for fields in sections)
    if(fieldCheck):
    	valid += 1

print(valid)

# Part two

def check_byr(byr): # 4 digits, between 1920-2002
	return True if(1920 <= int(byr) <= 2002) else False

def check_iyr(iyr): # 4 digits, between 2010-2020
	return True if(2010 <= int(iyr) <= 2020) else False

def check_eyr(eyr): # 4 digits, between 2020-2030
	return True if(2020 <= int(eyr) <= 2030) else False

def check_hgt(hgt): # cm(150-193) in(59-76)
	if(hgt[-2:] not in ['in', 'cm']):
		return False

	number = hgt[:-2]

	if(hgt[-2:] == 'cm') and (150 <= int(number) <= 193):
		return True

	if(hgt[-2:] == 'in') and (59 <= int(number) <= 76):
		return True

def check_hcl(hcl):
	if(hcl[0] != '#'):
		return False
	hcl_number = hcl[1:]
	if(len(hcl_number) != 6):
		return False
	pattern = re.compile("[A-Fa-f0-9]+")
	return True if(pattern.fullmatch(hcl_number)) else False

def check_ecl(ecl):
	valid_colours = [ 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' ]
	return True if (ecl in valid_colours) else False

def check_pid(pid):
	return True if(pid.isdigit() and len(pid) == 9) else False

def has_valid_passport(pp):
	pp_data = pp.split(' ')
	passport_data = {}

	#print(pp_data)

	for field in pp_data:
		key = field[:3]
		value = field[4:]
		passport_data[key] = value

	if(not check_byr(passport_data['byr'])):
		return False

	if(not check_iyr(passport_data['iyr'])):
		return False

	if(not check_eyr(passport_data['eyr'])):
		return False

	if(not check_hgt(passport_data['hgt'])):
		return False

	if(not check_hcl(passport_data['hcl'])):
		return False

	if(not check_ecl(passport_data['ecl'])):
		return False

	if(not check_pid(passport_data['pid'])):
		return False

	return True

valid_count = 0

# sorting passports
passports = []

for line in data:
    line = line.replace("\n", " ")
    fieldCheck = all(fields in line for fields in sections)
    if(fieldCheck):
    	passports.append(line)


for passport in passports:
	if(has_valid_passport(passport)):
		valid_count += 1

print(valid_count)
