# © 2025 Dorayakis007 — CC BY-NC 4.0 — https://github.com/Dorayakis007/AdventOfCode

# Global Variables
FILE_PATH:str = "(Your path)" # This day's input contains multiple lines, so it's easier to just have them all in a single file 
input_file:str = ""
part_selection:str = ""

current_string_list:list = []

total_nice_strings:int = 0
total_naughty_strings:int = 0

# Part 2 Variables
current_string:str = ""

# Old Rules function
def OldCheckString(string):
	global total_nice_strings
	global total_naughty_strings

	current_letter:str = ""
	last_letter:str = ""

	vowel_amount:int = 0

	has_3_vowels:bool = False
	has_double:bool = False
	has_banned_pair:bool = False
	
	for current_letter in string:
		has_banned_pair = last_letter + current_letter in ("ab", "cd", "pq", "xy")

		if (has_banned_pair):
			break
		if (not(has_3_vowels)):
			if (current_letter in ("a", "e", "i", "o", "u")):
				vowel_amount += 1
				has_3_vowels = vowel_amount == 3
		if (not(has_double)):
			has_double = current_letter == last_letter
		
		last_letter = current_letter
	
	if (not(has_banned_pair) and has_3_vowels and has_double):
		total_nice_strings += 1
	else:
		total_naughty_strings += 1

# New Rules function
def NewCheckString(string):
	global total_nice_strings
	global total_naughty_strings

	current_letter:str = ""
	last_letter:str = ""
	second_to_last_letter:str = ""

	has_space_repeat:bool = False
	has_twice_repeat:bool = False
	
	for current_letter in string:

		if (not(has_twice_repeat) and last_letter != ""):
			has_twice_repeat = current_string.count(last_letter + current_letter) > 1
		if (not(has_space_repeat)):
			has_space_repeat = second_to_last_letter == current_letter
		
		second_to_last_letter = last_letter
		last_letter = current_letter

	if (has_twice_repeat and has_space_repeat):
		total_nice_strings += 1
	else:
		total_naughty_strings += 1


# Choose Part 1 or Part 2 of the day's calculations
while part_selection not in ("1", "2"):
	part_selection = input("Choose which part to calculate"
						+ "\n 1 - Old Rules\n 2 - New Rules\n")


# Calculations start
with open(FILE_PATH) as input_file:	
	match part_selection:
		case "1":
			current_string_list = list(input_file.readline().strip())
			while current_string_list != []: 
				OldCheckString(current_string_list)
				current_string_list = list(input_file.readline().strip())
		
		case "2":
			current_string = input_file.readline().strip()
			current_string_list = list(current_string)
			while current_string_list != []: 
				NewCheckString(current_string_list)
				current_string = input_file.readline().strip()
				current_string_list = list(current_string)
	
# Final Output
print(f"Total number of Nice Strings: {total_nice_strings}\n"
	+ f"Total number of Naughty Strings: {total_naughty_strings}")