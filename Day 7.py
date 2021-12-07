inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	line = line.split(",")
	for x in line:
		parsed.append(int(x))

results = []

def calculate_dist(num):
	fuel = 0
	for item in parsed:
		fuel += sum(range(abs(item-num)+1))

	results.append(fuel)

for item in parsed:
	calculate_dist(item)

results.sort()
print(results[0])
