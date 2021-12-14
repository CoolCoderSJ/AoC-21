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


for iteration in range(40):
	pairs = []
	index = 0
	for i in polymer:
		if index == len(polymer)-1: break
		pairs.append(i+polymer[index+1])
		index += 1

	insertions = 0
	initialLen = len(polymer)
	for index in range(len(polymer)):
		if index == initialLen-1:
			break

		pair = pairs[insertions]
		polymer.insert(index+1+insertions, map[pair])
		insertions += 1
		

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

def least_frequent(List):
	from collections import Counter
	res = Counter(List)
	return res.most_common()[-1][0]


most = most_frequent(polymer)
least = least_frequent(polymer)

print(polymer.count(most)-polymer.count(least))
