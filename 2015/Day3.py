# © 2025 Dorayakis007 — CC BY-NC 4.0 — https://github.com/Dorayakis007/AdventOfCode

# Global Variables
part_selection:str = ""

santa_x:int = 0
santa_y:int = 0

moves_list:list = []
coords_list:list = ["0,0"]

unique_houses:set = {}
total_houses:int = 0

# Part 2 Variables
robo_x:int = 0
robo_y:int = 0

is_santa:bool = True
mover_x:int = 0
mover_y:int = 0

list_pos:int = 0


# User Input
moves_list = list(input("Insert Santa Claus' moves: "))

# Choose Part 1 or Part 2 of the day's calculations
while part_selection not in ("1", "2"):
	part_selection = input("Choose which part to calculate"
						 + "\n 1 - Santa\n 2 - Santa + Robo-Santa\n")


# Calculations
for move in moves_list:
	list_pos += 1

	if (part_selection == "1"):
		is_santa, mover_x, mover_y = True, santa_x, santa_y
	else:
		if (list_pos % 2):
			is_santa, mover_x, mover_y = False, robo_x, robo_y
		else:
			is_santa, mover_x, mover_y = True, santa_x, santa_y
		
	if (move == "^"):
		mover_y += 1
	elif (move == "v"):
		mover_y -= 1
	elif (move == ">"):
		mover_x += 1
	elif (move == "<"):
		mover_x -= 1
	
	coords_list.append(f"{mover_x},{mover_y}")

	if (is_santa):
		santa_x, santa_y = mover_x, mover_y
	else:
		robo_x, robo_y = mover_x, mover_y

unique_houses = set(coords_list)

# Final Output
print(f"Total unique houses visited: {len(unique_houses)}")