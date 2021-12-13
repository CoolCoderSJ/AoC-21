def run(coords):
	max_x = 0
	max_y = 0
	for coord in coords:
		coord = coord.split(",")
		x = int(coord[0])
		y = int(coord[1])

		if x > max_x: max_x = x
		if y > max_y: max_y = y
			

	for i in range(max_y+1):
		for j in range(max_x+1):
			if f"{j},{i}" in coords:
				if j == max_x:
					print("#", end="\n")
				else:
					print("#", end=" ")

			else:
				if j == max_x:
					print(" ", end="\n")
				else:
					print(" ", end=" ")
