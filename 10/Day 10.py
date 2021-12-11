inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	parsed.append(line)

inputFile.close()

beginnings = []

matches = {
	"(": ")",
	"[": "]",
	"{": "}",
	"<": ">"
}

scores = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
}
score = 0

allowed_starts = ["(", "[", "{", "<"]

counter = 0
illegal_lines = []
for line in parsed:
	for char in line:
		if char in allowed_starts:
			beginnings.append(char)
		elif char == matches[beginnings[-1]]:
			beginnings.pop(-1)
		else:
			illegal_lines.append(counter)
			score += scores[char]
			break
	counter += 1


print(score)


parsed = list(filter(lambda line: parsed.index(line) not in illegal_lines, parsed))
scores = []
charScores = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4
}

for line in parsed:
	beginnings = []
	score = 0
	for char in line:
		if char in allowed_starts:
			beginnings.append(char)
		else:
			beginnings.pop(-1)
	beginnings.reverse()
	for i in beginnings:
		score *= 5
		score += charScores[matches[i]]
	scores.append(score)

scores.sort()
index = int(len(scores)/2-0.5)
print(scores[index])
