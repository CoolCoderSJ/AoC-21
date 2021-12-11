from itertools import permutations

inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	line = line.split(" | ")
	combinations = line[0]
	outputs = line[1]
	parsed.append({
		"combinations": combinations.split(" "),
		"outputs": outputs.split(" ")
	})

inputFile.close()

output = 0

for digit in parsed:
	outputs = digit["outputs"]
	for i in outputs:
		if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
			output += 1

print(output)

path = "input.txt"
with open(path) as f:
	lines = f.read().splitlines()


DIGITS = (
	frozenset("ABCEFG"),
	frozenset("CF"),
	frozenset("ACDEG"),
	frozenset("ACDFG"),
	frozenset("BCDF"),
	frozenset("ABDFG"),
	frozenset("ABDEFG"),
	frozenset("ACF"),
	frozenset("ABCDEFG"),
	frozenset("ABCDFG"),
)

REFERENCE = tuple("ABCDEFG")

def backmap(segments, p):
	result = set()
	for segment in segments:
		result.add(REFERENCE[p.index(segment)])
	return result

def solve_permutation(displays):
	for p in permutations(REFERENCE):
		if all(backmap(segments, p) in DIGITS for segments in displays):
			return p

result = 0
for line in lines:
	displays, target = line.split(" | ")
	displays = displays.split(" ")
	displays = [segments.upper() for segments in displays]
	p = solve_permutation(displays)
	
	target = target.split(" ")
	target = [segments.upper() for segments in target]
	digits = [DIGITS.index(backmap(segments, p)) for segments in target]
	n = int("".join(str(x) for x in digits))
	result += n

print(result)
