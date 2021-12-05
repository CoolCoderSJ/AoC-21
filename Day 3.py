inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	parsed.append(line)

inputFile.close()

currentDigitsPlace = []

gammaBits = []
epsilonBits = []

for i in range(len(parsed[0])):
	for number in parsed:
		if number != 0:
			currentDigitsPlace.append(number[i])
		else:
			currentDigitsPlace.append(0)
	epsilonBits.append(min(currentDigitsPlace, key=currentDigitsPlace.count))
	gammaBits.append(max(currentDigitsPlace, key=currentDigitsPlace.count))
	currentDigitsPlace.clear()

gammaRate = int("".join(gammaBits), 2)
epsilonRate = int("".join(epsilonBits), 2)

print(gammaRate, epsilonRate)


for i in range(len(parsed[0])):
	for number in parsed:
		currentDigitsPlace.append(number[i])
		
	zeroes = 0
	ones = 0

	for digit in currentDigitsPlace:
		if digit == "0"  : zeroes += 1
		elif digit == "1": ones   += 1

	if len(parsed) == 2:
		highest = "1"
		lowest = "0"
	elif zeroes > ones:
		lowest = "1"
		highest = "0"
	else:
		highest = "1"
		lowest = "0"

	currentDigitsPlace.clear()

	parsed = list(filter(lambda num: num[i]==highest, parsed))

print(parsed[0], int(parsed[0], 2))


inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	parsed.append(line)

inputFile.close()

for i in range(len(parsed[0])):
	for number in parsed:
		currentDigitsPlace.append(number[i])
		
	zeroes = 0
	ones = 0

	for digit in currentDigitsPlace:
		if digit == "0"  : zeroes += 1
		elif digit == "1": ones   += 1

	if len(parsed) == 2:
		highest = "1"
		lowest = "0"
	elif zeroes > ones:
		lowest = "1"
		highest = "0"
	else:
		highest = "1"
		lowest = "0"

	currentDigitsPlace.clear()

	parsed = list(filter(lambda num: num[i]==lowest, parsed))

	if len(parsed) == 1:
		break

print(parsed[0], int(parsed[0], 2))
