inputFile = open("input.txt", "r")
parsed = []

for line in inputFile:
	line = line.strip()
	nums = []
	for i in line.split(" "):
		try:
			nums.append(int(i))
		except: pass
	parsed.append(nums)

while [] in parsed:
	parsed.remove([])

inputFile.close()

numbers = [31,88,35,24,46,48,95,42,18,43,71,32,92,62,97,63,50,2,60,58,74,66,15,87,57,34,14,3,54,93,75,22,45,10,56,12,83,30,8,76,1,78,82,39,98,37,19,26,81,64,55,41,16,4,72,5,52,80,84,67,21,86,23,91,0,68,36,13,44,20,69,40,90,96,27,77,38,49,94,47,9,65,28,59,79,6,29,61,53,11,17,73,99,25,89,51,7,33,85,70]

def divide_chunks(l, n):
    for i in range(0, len(l), n): 
        yield l[i:i + n]
  
n = 5
parsed = list(divide_chunks(parsed, n))

cardIndex = 0
done = []

def check_bingo():
	global cardIndex
	for card in parsed:
		for row in card:
			horizontal = 0
			for number in row:
				if number in called:
					horizontal += 1
			if horizontal == 5:
				cardIndex = parsed.index(card)
				if cardIndex not in done:
					done.append(cardIndex)
				if len(done) == len(parsed):
					return "BINGO"
	
	for card in parsed:
		for i in range(5):
			cardIndex = parsed.index(card)

			if card[0][i] in called and card[1][i] in called and card[2][i] in called and card[3][i] in called and card[4][i] in called:
				if cardIndex not in done:
					done.append(cardIndex)
				if len(done) == len(parsed):
					return "BINGO"
	

called = []
for i in numbers:
	called.append(i)
	if check_bingo() == "BINGO":
		break

inputFile = open("input.txt", "r")
singles = []

for line in inputFile:
	line = line.strip()
	for i in line.split(" "):
		try:
			singles.append(int(i))
		except: pass

  
singles = list(divide_chunks(singles, 25))

unmarked = 0

for number in singles[cardIndex]:
	if number not in called: unmarked += number

print(unmarked)
print(called[-1])