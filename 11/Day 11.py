import debugger

inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	parsed.append(line)

inputFile.close()

coords = {}

ycount = 0
for line in parsed:
	counter = 0
	for char in line:
		x = counter
		y = ycount
		coords[f'{x},{y}'] = char
		counter += 1
	ycount += 1

orig_coords = coords.copy()

flashes = 0

def get_coords(string): return int(string.split(",")[0]), int(string.split(",")[1])
def tuple_to_str(tupl): return f"{tupl[0]},{tupl[1]}"

def add_adj(x, y):
	global coords, flashes, flashed
	if (x, y) not in flashed:
		flashes += 1
		flashed.append((x, y))
		coords[tuple_to_str((x, y))] = 0
		positions = {
		"left"        : (x-1, y),
		"right"       : (x+1, y),
		"up"          : (x, y-1),
		"down"        : (x, y+1),

		"topleft"     : (x-1, y-1),
		"topright"    : (x+1, y-1),
		"bottomleft"  : (x-1, y+1),
		"bottomright" : (x+1, y+1),
		}


		for pos in positions:
			x = positions [pos][0]
			y = positions [pos][1]
			if tuple_to_str(positions[pos]) in coords:
				if positions[pos] not in flashed:
					adjval = int(coords[tuple_to_str(positions[pos])])
					if positions[pos] not in flashed: coords[tuple_to_str(positions[pos])] = adjval + 1
					if adjval+1 > 9:
						add_adj(x, y)
		

for i in range(100):
	flashed = []
	for coord in coords:
		x, y = get_coords(coord)
		val = int(coords[coord])
		if val < 9 and (x, y) not in flashed:
			coords[coord] = val+1
		else:
			add_adj(x, y)

		#debugger.run(coords, get_coords, flashed, parsed, newline=True, inp=True, clear=True)

print(flashes)


steps = 0
coords = orig_coords

while 1:
	flashed = []
	for coord in coords:
		x, y = get_coords(coord)
		val = int(coords[coord])
		if val < 9 and (x, y) not in flashed:
			coords[coord] = val+1
		
		else:
			add_adj(x, y)
	
	steps += 1
	if len(flashed) == len(coords): break


print(steps)
