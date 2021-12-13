import visualizer

inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	parsed.append(line)

inputFile.close()

coords = []
directions = []

for line in parsed:
	if line == "":
		break
	line = line.split(",")
	x = int(line[0])
	y = int(line[1])
	coords.append([x, y])

for i in coords:
	parsed.remove(f"{i[0]},{i[1]}")

parsed.remove("")

for i in parsed:
	i = i.split("along ")
	i = i[-1].split("=")
	directions.append([i[0], int(i[1])])

orig = coords.copy()

direction = directions[0]
map = {}
way = direction[0]
unit = direction[1]

if way == "y":
	for coord in coords:
		x, y = coord
		if y > unit:
			new_y = y-((y-unit)*2)
			map[f"{x},{y}"] = [x, new_y]


if way == "x":
	for coord in coords:
		x, y = coord
		if x > unit:
			new_x = x-((x-unit)*2)
			map[f"{x},{y}"] = [new_x, y]


index = 0
for coord in coords:
	x, y = coord
	if f"{x},{y}" in map:
		coords[index] = map[f"{x},{y}"]

	coords[index] = f"{coords[index][0]},{coords[index][1]}"
	index += 1

coords = list(set(coords))

print(len(coords))

coords = orig.copy()
for direction in directions:
	map = {}
	way = direction[0]
	unit = direction[1]

	if way == "y":
		for coord in coords:
			x, y = coord
			if y > unit:
				new_y = y-((y-unit)*2)
				map[f"{x},{y}"] = [x, new_y]


	if way == "x":
		for coord in coords:
			x, y = coord
			if x > unit:
				new_x = x-((x-unit)*2)
				map[f"{x},{y}"] = [new_x, y]


	index = 0
	for coord in coords:
		x = coord[0]
		y = coord[1]
		if f"{x},{y}" in map:
			coords[index] = map[f"{x},{y}"]
		index += 1

index = 0
for coord in coords:
	coords[index] = f"{coords[index][0]},{coords[index][1]}"
	index += 1

coords = list(set(coords))

#For anyone looking at my code, run the code and read the terminal output for the answer- it's rendered with # and . as shown in the example. 
visualizer.run(coords)
