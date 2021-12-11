inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	lineToAdd = []
	for i in line:
		lineToAdd.append(int(i))
	parsed.append(lineToAdd)

inputFile.close()

coords = {}
sinks = {}

for i in parsed:
	counter = 0
	for j in i:
		coords[f"{counter},{parsed.index(i)}"] = j
		counter += 1


def right(x, y):
	x += 1
	return coords[f"{x},{y}"]

def left(x, y):
	x -= 1
	return coords[f"{x},{y}"]

def up(x, y):
	y -= 1
	return coords[f"{x},{y}"]

def down(x, y):
	y += 1
	return coords[f"{x},{y}"]

for coord in coords.items():
	x = int(coord[0].split(",")[0])
	y = int(coord[0].split(",")[1])

	value = coord[1]
	coord = [x, y]

	if x == 0 and y == 0:
		if value < down(x,y) and value < right(x,y): sinks[f"{x},{y}"] = value

	elif x != len(parsed[0])-1 and y == 0:
		if value < down(x,y) and value < left(x,y) and value < right(x,y): sinks[f"{x},{y}"] = value

	elif x == len(parsed[0])-1 and y == 0:
		if value < down(x,y) and value < left(x,y): sinks[f"{x},{y}"] = value

	elif x ==  0 and y == len(parsed)-1:
		if value < up(x,y) and value < right(x,y): sinks[f"{x},{y}"] = value

	elif x != len(parsed[0])-1 and y == len(parsed)-1:
		if value < up(x,y) and value < left(x,y) and value < right(x,y): sinks[f"{x},{y}"] = value

	elif x == len(parsed[0])-1 and y == len(parsed)-1:
		if value < up(x,y) and value < left(x,y): sinks[f"{x},{y}"] = value

	elif x == 0:
		if value < up(x,y) and value < down(x,y) and value < right(x,y): sinks[f"{x},{y}"] = value

	elif x == len(parsed[0])-1:
		if value < up(x,y) and value < down(x,y) and value < left(x,y): sinks[f"{x},{y}"] = value

	else:
		if value < down(x,y) and value < right(x,y) and value < left(x,y) and value < up(x,y): sinks[f"{x},{y}"] = value


print(sum(sinks.values())+len(sinks))

def right(x, y):
	x += 1
	return coords[f"{x},{y}"], x, y

def left(x, y):
	x -= 1
	return coords[f"{x},{y}"], x, y

def up(x, y):
	y -= 1
	return coords[f"{x},{y}"], x, y

def down(x, y):
	y += 1
	return coords[f"{x},{y}"], x, y


def check_adj(x, y):
	adj = []
	
	if x > 0:
		adj.append(left(x, y))
	
	if x < len(parsed[0])-1:
		adj.append(right(x, y))

	if y > 0:
		adj.append(up(x, y))
	
	if y < len(parsed)-1:
		adj.append(down(x, y))

	value = coords[f"{x},{y}"]
	resp = []
	for val in adj:
		if val[0] > value and val[0] != 9:
			resp.append([val[1], val[2]])

	return resp

basins = []


def add_nums(num):
	x = num[0]
	y = num[1]
	largerNums = check_adj(x, y)
	for num in largerNums:
		if num not in basin:
			basin.append(num)
			add_nums(num)

for low in sinks.items():
	x = int(low[0].split(",")[0])
	y = int(low[0].split(",")[1])
	basin = [[x, y]]
	add_nums([x, y])
	
	basins.append(len(basin))

basins.sort()


print(basins[-1] * basins[-2] * basins[-3])
