# © 2025 Dorayakis007 — CC BY-NC 4.0 — https://github.com/Dorayakis007/AdventOfCode

import hashlib
md5_hash:str = ""
user_input:str = ""
hash_digerido:str = ""
cantidad_ceros:int = 0
conseguido:bool = False
input_con_num:str = ""
numero_actual:int = -1
ceros_queridos:int = 0

user_input = input("Input: ") # Pilla el user input
ceros_queridos = int(input("Por cuantos ceros quieres que empiece el hash? "))

while not(conseguido):
	numero_actual += 1 
	input_con_num = str(user_input) + str(numero_actual) # Junta input con el numero
	md5_hash = hashlib.md5() # Reiniciamos el hash
	md5_hash.update(input_con_num.encode()) # Actualiza el md5
	hash_digerido = md5_hash.hexdigest() # Actualiza la variable con el hex del hash

	# Checkeo de si da cinco ceros o no
	for char in list(hash_digerido):
		if (char == "0"):
			cantidad_ceros += 1
			if (cantidad_ceros == ceros_queridos):
				conseguido = True
				break
			else:
				continue
		else:
			break
	cantidad_ceros = 0

print("")
print("Hash final:", hash_digerido)
print("Input final:", input_con_num)
print("Numero solo:", numero_actual)
print("Lo hice?: ", conseguido)