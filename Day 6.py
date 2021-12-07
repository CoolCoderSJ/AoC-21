from collections import Counter

inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	line = line.split(",")
	for x in line:
		parsed.append(int(x))


fish = Counter(parsed)

for i in range(256):
	result = Counter()
	for timer, nums in fish.items():
		if timer == 0:
			result[6] += nums
			result[8] += nums
		else:
			result[timer-1] += nums
	fish = result

result = sum(fish.values())
print(result)
