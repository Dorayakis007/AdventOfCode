# © 2025 Dorayakis007 — CC BY-NC 4.0 — https://github.com/Dorayakis007/AdventOfCode

# Variables
FILE_PATH:str = "(Your Path)" # This day's input contains multiple lines, so it's easier to just have them all in a single file 
ROWS:int = 1000
COLS:int = 1000

lights_grid:list = [[[0 for value in range(2)] for light in range(COLS)] for light in range(ROWS)]

total_lights:int = 0
total_brightness:int = 0

# Defining Main Operation Function
def DoOperation(operation, x1, y1, x2, y2):
	global lights_grid
	
	# list 0 = on/off
	# list 1 = brightness
	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			match operation:
				case "toggle":
					lights_grid[x][y][0] ^= 1
					lights_grid[x][y][1] += 2
				case "on":
					lights_grid[x][y][0] = 1
					lights_grid[x][y][1] += 1
				case "off":
					lights_grid[x][y][0] = 0
					if (lights_grid[x][y][1]):
						lights_grid[x][y][1] -= 1


# Calculations
with open(FILE_PATH) as input_file:		
	for raw_line in input_file:
		# I know this string division is messy, but it works and with this puzzle 
		# I'm mainly focused on making the grid work and understanding it
		# Maybe in the future i re-visit these and make them more efficient/readable
		divided_line = raw_line.strip().removeprefix("turn ").partition(" through ")
		coords2 = divided_line[2].split(",")
		divided_line = divided_line[0].split(" ")
		operation = divided_line[0]
		coords1 = divided_line[1].split(",")

		DoOperation(operation, int(coords1[0]), int(coords1[1]), int(coords2[0]), int(coords2[1]))
		
for x in range(ROWS):
	for y in range(COLS):
		if (lights_grid[x][y][0]):
			total_lights += 1
		total_brightness += lights_grid[x][y][1]


# Final Output
print(f"Total amount of lights turned on: {total_lights}"
	  + f"\nTotal brightness: {total_brightness}")