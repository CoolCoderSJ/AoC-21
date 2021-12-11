inputFile = open("input.txt", "r")
numInput = []

for line in inputFile:
	line = line.strip()
	numInput.append(int(line))

inputFile.close()

final = 0
previousSet = [0, 1, 2]
sumOfThree = 581
index = 0

for number in numInput:
	try:
		currentSum = numInput[previousSet[0]] + numInput[previousSet[1]] + numInput[previousSet[2]]
	except:
		currentSum = numInput[previousSet[0]]
		
	if currentSum > sumOfThree:
		final += 1

	sumOfThree = currentSum
	previousSet.pop(0)
	previousSet.append(previousSet[1]+1)
	index += 1

print(final)