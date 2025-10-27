# © 2025 Dorayakis007 — CC BY-NC 4.0 — https://github.com/Dorayakis007/AdventOfCode

the_input_string:str = ""
the_input_list:list = [""]
positive_parenthesis:int = 0
negative_parenthesis:int = 0
total_floors:int = 0
current_list_spot:int = 0
current_list_value:str = ""

the_input_string = input("Input the Input: ")
the_input_list = list(the_input_string)


# Part 1
positive_parenthesis = the_input_list.count("(")
negative_parenthesis = the_input_list.count(")")

total_floors = positive_parenthesis - negative_parenthesis

print("Plantas totales que ha subido:", total_floors)


# Limpiando variables entre parte 1 y parte 2
positive_parenthesis = 0
negative_parenthesis = 0


#Part 2
while True:
	current_list_value = the_input_list[current_list_spot]

	match current_list_value:
		case "(":
			positive_parenthesis += 1
		case ")":
			negative_parenthesis += 1
	
	if(positive_parenthesis - negative_parenthesis == -1):
		print("Caracter en el cual baja al piso -1 por primera vez:", current_list_spot + 1)
		break
	else:
		current_list_spot += 1