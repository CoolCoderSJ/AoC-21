import os
def run(coords, get_coords, flashed, parsed, newline=True, inp=True, clear=True):
	for item in coords:
		x, y = get_coords(item)
		if (x, y) in flashed: start = "\033[33m"
		else: start = ""
		if x != len(parsed[0])-1: print(f"{start}{coords[item]}\033[0m", end=" ")
		else: print(f"{start}{coords[item]}\033[0m")
	if newline:
		print("\n\n\n")
	if inp:
		input()
	if clear:
		os.system("clear")