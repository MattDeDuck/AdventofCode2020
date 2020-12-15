input = [ 0,3,1,6,7,5 ]

def get_num(start,fin):
	spoken_nums = {}

	for i in range(len(start)):
		spoken_nums[start[i]] = i

	speaking = 0

	for i in range(len(start), fin):
	    prev_spoken = speaking
	    if speaking not in spoken_nums.keys():
	    	speaking = 0
	    else:
	    	speaking = i - spoken_nums[speaking]
	    spoken_nums[prev_spoken] = i
	return prev_spoken

p1 = get_num(input,2020)
print(f"Part 1: {p1}")

p2 = get_num(input,30000000)
print(f"Part 2: {p2}")
