inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	line = line.split(" -> ")
	x1 = int(line[0].split(",")[0])
	y1 = int(line[0].split(",")[1])
	x2 = int(line[1].split(",")[0])
	y2 = int(line[1].split(",")[1])

	parsed.append([[x1, y1], [x2, y2]])
		
inputFile.close()

totalPoints = []

for coords in parsed:
	x1 = coords[0][0]
	x2 = coords[1][0]
	y1 = coords[0][1]
	y2 = coords[1][1]
	line = [[x1, y1], [x2, y2]]

	if y1 == y2:
		if x1 > x2:
			for i in range(x1 - x2-1):
				line.append([x2+i+1, y1])
		elif x2 > x1:
			for i in range(x2 - x1-1):
				line.append([x1+i+1, y1])

	elif x1 == x2:
		if y1 > y2:
			for i in range(y1 - y2-1):
				line.append([x1, y2+i+1])
		elif y2 > y1:
			for i in range(y2 - y1-1):
				line.append([x1, y1+i+1])

	else:
		for i in range(abs(x2 - x1)-1):
			if x2 > x1 and y2 < y1:
				line.append([x2-i-1, y2+i+1])
			elif x1 > x2 and y1 < y2:
				line.append([x2+i+1, y2-i-1])	
			elif x2 > x1 and y2 > y1:
				line.append([x2-i-1, y2-i-1])
			elif x1 > x2 and y1 > y2:
				line.append([x2+i+1, y2+i+1])

	totalPoints.append(line)


contains = []

def check(item, index):
	for line in totalPoints:
		if totalPoints.index(line) != index and item in line:
			return True

	return None


for line in totalPoints:
	print(totalPoints.index(line))
	for coord in line:
		overlap = check(coord, totalPoints.index(line))
		if overlap:
			if coord not in contains:
				contains.append(coord)

print(len(contains))
