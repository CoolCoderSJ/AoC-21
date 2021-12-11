file = open("input.txt", "r")
parsed = []

for line in file:
	line = line.strip()
	line = line.split(" ")
	parsed.append({
		"direction": line[0],
		"distance": int(line[1])
	})

file.close()

depth = 0
position = 0
aim = 0

for movement in parsed:
	if movement['direction'] == "up":
		aim -= movement['distance']
	
	elif movement['direction'] == "down":
		aim += movement['distance']

	elif movement['direction'] == "forward":
		position += movement['distance']
		depth += aim * movement['distance']

print(f"Depth: {depth}")
print(f"Position: {position}")
print(f"Aim: {aim}")
print(f"Product: {depth*position}")