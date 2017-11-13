print("Este programa calculará la potencia de una base.\n¿Desea continuar con la ejecución del programa?(s/n): ")

while respuesta.lower() in ("s"):
	base = int(input("Introduzca la base: "))
	exponente = int(input("Introduzca el exponente: ")) 

	i = 1
	if exponente == 0:
		print("El resultado es 1.")
		respuesta = input("¿Quiere repetir?(s/n): ")
	else:

		while i < exponente:
			resultado = base**exponente
			print ("El resulatado es",resultado)
			respuesta = input("¿Quiere repetir?(s/n): ")
			break
else:
	print("Nos vemos.")
