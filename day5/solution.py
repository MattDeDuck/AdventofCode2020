with open('input5.txt') as file:
	data = file.readlines()
	data = [ line.strip() for line in data ]

# Part one

seatIDs = []

for line in data:	
	new = line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')

	row = int(new[:-3], 2)
	column = int(new[-3:], 2)

	seat_id = row * 8 + column
	seatIDs.append(seat_id)

print(max(seatIDs))

# Part two

sorted_seats = sorted(seatIDs)
my_seat = next(i + sorted_seats[0] for i in range(len(sorted_seats)) if sorted_seats[i] != i + sorted_seats[0])

print(my_seat)
