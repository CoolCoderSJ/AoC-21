from collections import Counter

inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	parsed.append(line)

inputFile.close()

parsed.remove("")

polym = parsed[0]
parsed.remove(polym)
map = {}
for line in parsed:
	src, tgt = line.split(" -> ")
	map[src] = tgt

polymer = []
for char in polym:
	polymer.append(char)

pairs = []
index = 0
for i in polymer:
	if index == len(polymer)-1: break
	pairs.append(i+polymer[index+1])
	index += 1

pairs = Counter(pairs)

for iteration in range(40):
	res = Counter()
	for pair, value in pairs.items():
		res[list(pair)[0]+map[pair]] += value
		res[map[pair]+list(pair)[1]] += value

	pairs = res


res = Counter()
for pair, value in pairs.items():
	res[list(pair)[0]] += value
	res[list(pair)[1]] += value

most = res.most_common(1)[0][0]
least = res.most_common()[-1][0]

import math
print(math.ceil((res[most]-res[least])/2))
