def l(): print("");
# Generador de números primos

print("DECOMPONER EN FACTORES PRIMOS")
print("ARNALDO CISNEROS")
print("NOVIEMBRE DE 2020")

while True:
	l()
	numero_para_descomponer=int(input("Inserta un número para descomponer: "))
	numero_temporal=numero_para_descomponer
	factores_primos=[]
	
	# **** CODIGO PARA DESCOMPONER
	divisor_primo=2
	while divisor_primo<=(numero_para_descomponer/2):

		while True: # Bucle para ir descomponiendo el número entre el número primo actual
			if numero_temporal%divisor_primo==0:
				factores_primos.append(divisor_primo)
				numero_temporal=numero_temporal/divisor_primo
			else:
				break;

		numero_evaluado=divisor_primo+1
		while True: # Bucle para encontrar el siguiente primo cuando el anterior ya no funciona
			
			primo_encontrado=True
			divisor_maximo=numero_evaluado/2
			divisor_actual=2 
			while divisor_actual<divisor_maximo:
				resto=numero_evaluado%divisor_actual
				if resto==0:
					numero_evaluado+=1
					primo_encontrado=False
					break;
				else:
					divisor_actual+=1		
			
			if primo_encontrado: # Numero primo encontrado
				divisor_primo=numero_evaluado
				break;


	# **************************************
	
	cadena_de_factores="1"
	for i in factores_primos:
		cadena_de_factores=cadena_de_factores+", "+str(i)

	print(str(numero_para_descomponer)+" = "+cadena_de_factores)

	l()
	salir=input("¿Deseas hacer otra descompocisión? y/n: ")
	if salir=="n":
		break;
	elif salir=="y":
		pass
	else:
		print("Respuesta no válida, finalizando el programa")
		input()
		break;