# © 2025 Dorayakis007 — CC BY-NC 4.0 — https://github.com/Dorayakis007/AdventOfCode

# Global Variables
FILE_PATH:str = "(Your path)" # This day's input contains multiple lines, so it's easier to just have them all in a single file 
input_file:str = ""
part_selection:str = ""

current_line:str = None
current_values:list = []

total_material:int = 0

# Part 1 Variables
box_lw:int = 0
box_wh:int = 0
box_hl:int = 0

box_wrap:int = 0
extra_wrap:int = 0

# Part 2 Variables
rib_l:int = 0
rib_w:int = 0
rib_h:int = 0

rib_wrap:int = 0
rib_bow:int = 0

# Choose Part 1 or Part 2 of the day's calculations
while part_selection not in ("1", "2"):
	part_selection = input("Choose which part to calculate"
						+ "\n 1 - Wrapping\n 2 - Ribbons\n")

match part_selection:
	case "1":
		with open(FILE_PATH) as input_file:
			
			# Part 1 Calculations
			current_line = input_file.readline().strip()
			
			while current_line != "": 
				current_values = current_line.split("x")
				
				box_lw = int(current_values[0]) * int(current_values[1])
				box_wh = int(current_values[1]) * int(current_values[2])
				box_hl = int(current_values[2]) * int(current_values[0])

				box_wrap = (2 * box_lw) + (2 * box_wh) + (2 * box_hl)
				extra_wrap = min(box_lw, box_wh, box_hl)

				total_material += box_wrap + extra_wrap

				current_line = input_file.readline().strip()

		# Part 1 Output
		print(f"Total square feet of wrapping paper used: {total_material}")
	
	case "2":
		with open(FILE_PATH) as input_file:
			
			# Part 2 Calculations
			current_line = input_file.readline().strip()
			
			while current_line != "": 
				current_values = current_line.split("x")
				
				rib_l = int(current_values[0])
				rib_w = int(current_values[1])
				rib_h = int(current_values[2])

				rib_wrap = (2 * rib_l) + (2 * rib_w) + (2 * rib_h) - (2 * max(rib_l, rib_w, rib_h))
				rib_bow = rib_l * rib_w * rib_h

				total_material += rib_wrap + rib_bow

				current_line = input_file.readline().strip()

		# Part 2 Output
		print(f"Total feet of ribbon used: {total_material}")