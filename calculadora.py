from distutils.log import error
import os
from math import fsum, sqrt
import time

def menu():
	error = "\x1b[1;31m"+"[!]"
	naranja ="\x1b[1;33m"
	cyan = "\x1b[1;36m"
	azul = "\x1b[1;34m"
	morado = "\x1b[1;35m"
	blanco = "\x1b[1;37m"
	red = "\x1b[1;31m"
	
	os.system("clear")

	titol = "PROGRAMA DE MATES"
	subtitol = " by d3b0"
	print("{}+{}+\n{}|{}{}|\n{}+{}+\n".format(cyan,"-" * (len(titol) + len(subtitol)) ,cyan ,titol, subtitol,cyan, "-" * (len(titol) + len(subtitol))))
	
	print("{} La raiz cuadrada esta expresada con '{}~{}'\n".format(error, blanco,red))
	opcion = int(input("{}Equaciones:\n\n\t1- Equaciones 2 Grado\n\t2- Equacions Biquadrades\n\nOperaciones Basicas:\n\n\t3- Suma\n\t4- Resta\n\t5- Multiplicacion\n\t6- Division\n\t7- Potencias\n\t8- Raiz Cuadrada\n\n\t0- Exit\n\n\t\t>{} ".format(naranja, blanco)))
	if opcion == 1:
		equaciones2grado()
	
	elif opcion == 2:
		equacionesBiquadradas()

	elif opcion == 3:
		sumas()

	elif opcion == 4:
		Restas()

	elif opcion == 5:
		Multiplicacions()

	elif opcion == 6:
		Divisiones()

	elif opcion == 7:
		Potencies()

	elif opcion == 8:
		Raiz()

	elif opcion == 0:
		os.system("clear")
		
		print("\n{} Saliendo...".format(error))

	else:
		os.system("clear")

		print("\n{} Error".format(error))
		


def equaciones2grado():
	error = "\x1b[1;31m"+"[!]"
	naranja ="\x1b[1;33m"
	cyan = "\x1b[1;36m"
	azul = "\x1b[1;34m"
	morado = "\x1b[1;35m"
	blanco = "\x1b[1;37m"
	
	os.system("clear")
	
	titol = "Equaciones 2 Grado"
	print("{}{}\n{}\n".format(cyan, titol, "=" * (len(titol))))
	
	a = int(input("{}[*] a:{} ".format(naranja, blanco)))
	b = int(input("{}[*] b:{} ".format(naranja, blanco)))
	c = int(input("{}[*] c:{} ".format(naranja, blanco)))
	b1 = -b
	#Comprovacio per si l'arrel dona negatiu
	os.system("clear")
	if ((b**2)-4*a*c) < 0:
		print("\n{}No tiene Resultado o a ocurrido un errror, revisa los datos introducidos".format(error))

	else:
		#x+
		xpositiva = (-b+sqrt(b**2-(4*a*c)))/(2*a)
		#x-
		xnegativa = (-b-sqrt(b**2-(4*a*c)))/(2*a)
		print("\n{}[*] Resultado: {}{} {}/{} {}".format(naranja, blanco, xpositiva, naranja, blanco, xnegativa))
		time.sleep(1)
		opcion = input("\n{}[!] Para MOSTRAR los PASOS pulsa '{}m{}'\n    Para VOLVER al MENU pulsa '{}r{}'\n       >{}".format(naranja, blanco, naranja, blanco, naranja, blanco))
		if opcion == "r":
			menu()
		else:
			times = 0.2

			f1 = "-b+-~b^2-4·a·c"
			f2 = int(len(f1) / 2.5)

			print("\n\t\t{}\n\t    x = --------------\n\t\t{}2 · a".format(f1, " " * f2))

			f1 = "-{}+-~{}^2-4·{}·{}".format(b, b, a, c,)
			f2 = int(len(f1) / 2.5)
			
			time.sleep(times)

			print("\n\t\t{}\n\t\t{}\n\t\t{}2 · {}".format(f1, "-" * len(f1), " " * f2, a))
			
			f1 = "{}+-~{}-{}".format(-b, b ** 2, 4 * a * c)
			f2 = int(len(f1) / 2.2)
			
			time.sleep(times)

			print("\n\t\t{}\n\t\t{}\n\t\t{}{}".format(f1, "-" * len(f1), " " * f2, 2 * a))
			
			f1 = "{}+-~{}".format(-b,(b ** 2) - (4 * a * c) )
			f2 = int(len(f1) / 2.2)
			
			time.sleep(times)

			print("\n\t\t{}\n\t\t{}\n\t\t{}{}".format(f1, "-" * len(f1), " " * f2, 2 * a))

			f1 = "{}+-{}".format(-b, sqrt((b ** 2) - (4 * a * c)))
			f2 = int(len(f1) / 2.2)

			time.sleep(times)
			
			print("\n\t\t{}\n\t\t{}\n\t\t{}{}".format(f1, "-" * len(f1), " " * f2, 2 * a))

			time.sleep(times)

			print("\n\n\t\t{}Opcion 1:{}".format(naranja, (blanco)))

			f1 = "{}".format(-b + sqrt((b ** 2) - (4 * a * c)))			
			f2 = int(len(f1) / 2.2)

			time.sleep(times)

			print("\n\t\t{}\n\t\t{} = {}\n\t\t{}{}".format(f1, "-" * len(f1), (-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a), " " * f2 , 2 * a))

			time.sleep(times)

			print("\n\n\t\t{}Opcion 2:{}".format(naranja, blanco))

			f1 = "{}".format(-b - sqrt((b ** 2) - (4 * a * c)))			
			f2 = int(len(f1) / 2.2)
			
			time.sleep(times)

			print("\n\t\t{}\n\t\t{} = {}\n\t\t{}{}".format(f1, "-" * len(f1), (-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a), " " * f2 , 2 * a))

			opcion = input("\n\n{}Para volver al menu pulsa '{}m{}', para hacer otra equacion pulsa '{}r{}'\n\n\t>{}".format(naranja, blanco, naranja, blanco, naranja, blanco))
			if opcion == "m":
				menu()
			elif opcion == "r":
				equaciones2grado()
			else:
				menu()


def equacionesBiquadradas():
	error = "\x1b[1;31m"+"[!]"
	naranja ="\x1b[1;33m"
	cyan = "\x1b[1;36m"
	azul = "\x1b[1;34m"
	morado = "\x1b[1;35m"
	blanco = "\x1b[1;37m"
	
	os.system("clear")

	titol = "Equaciones Biquadradas"
	print("{}{}\n{}{}\n".format(cyan, titol, cyan, "=" * (len(titol))))
	
	print("\n{}Llena los espacios'[]' con el numero correspondiente".format(naranja))
	
	a = int(input("{}\n[{}".format(naranja, blanco)))
	os.system("clear")
	
	titol = "Equaciones Biquadradas"
	print("{}{}\n{}{}\n".format(cyan, titol,cyan , "=" * (len(titol))))
	print("\n{}Llena los espacios'[]' con el numero correspondiente".format(naranja))
	b = int(input("\n{}{}x^4 {}[{}".format(blanco, a, naranja, blanco)))
	os.system("clear")
	
	titol = "Equaciones Biquadradas"
	print("{}{}\n{}{}\n".format(cyan, titol, cyan , "=" * (len(titol))))
	print("\n{}Llena los espacios'[]' con el numero correspondiente".format(naranja))
	c = int(input("{}\n{}x^4 {}x^2 [".format(blanco, a, b)))
	os.system("clear")
	
	titol = "Equaciones Biquadradas"
	print("{}{}\n{}{}\n".format(cyan, titol, cyan , "=" * (len(titol))))
	print("\n{}Llena los espacios'[]' con el numero correspondiente".format(naranja))
	print("\n{}{}x^4 {}x^2 {}".format(blanco, a, b, c))

	print("\nx^2 = z\nx^4 = z^2")
	print("\n{}z^2 {}z {}".format(a, b, c))
	print("\na = {}\nb = {}\nc = {}".format(a, b, c))

	if ((b**2)-4*a*c) < 0:
		print("\n""\x1b[1;31m"+"[!] ""\x1b[1;33m"+"No tiene Resultado o a ocurrido un errror, revisa los datos introducidos")

	else:
		#x+
		xpositiva = sqrt((-b+sqrt(b**2-(4*a*c)))/(2*a))
		#x-
		xnegativa = sqrt((-b-sqrt(b**2-(4*a*c)))/(2*a))
		print("\n{}[*] Resultado: {}+-{}{} / {}+-{}".format(naranja,blanco ,xpositiva,naranja, blanco,xnegativa))
		time.sleep(1)
		opcion = input("\n{}{} Para MOSTRAR los PASOS pulsa {}'m'{}\n    Para VOLVER al MENU pulsa {}'r'\n       >".format(error, naranja, blanco, naranja, blanco ))
		if opcion == "r":
			menu()
		else:
			times = 0.2

			f1 = "-b+-~b^2-4·a·c"
			f2 = int(len(f1) / 2.5)
			g = "z = "
			print("\n\t\t{}Formula{}".format(naranja, blanco))
			print("\n\t\t{}{}\n\t\t{}--------------\n\t\t{}2 · a".format(" " * len(g),f1,g,  " " * f2))
			f1 = "-{}+-~{}^2-4·{}·{}".format(b, b, a, c,)
			f2 = int(len(f1) / 2.5)
			
			time.sleep(times)
			print("\n\n\t\t{}Se substituye a b c por los numeros corespondientes{}".format(naranja, blanco))
			print("\n\t\t{}\n\t\t{}\n\t\t{}2 · {}".format(f1, "-" * len(f1), " " * f2, a))
			
			f1 = "{}+-~{}-{}".format(-b, b ** 2, 4 * a * c)
			f2 = int(len(f1) / 2.2)
			
			time.sleep(times)
			print("\n\n\t\t{}Se calcula {}^2 y 4 * {} * {}{}".format(naranja, b, a, c, blanco))
			print("\n\t\t{}\n\t\t{}\n\t\t{}{}".format(f1, "-" * len(f1), " " * f2, 2 * a))
			
			f1 = "{}+-~{}".format(-b,(b ** 2) - (4 * a * c) )
			f2 = int(len(f1) / 2.2)
			
			time.sleep(times)

			print("\n\n\t\t{}Se calcula {}-{}{}".format(naranja, b ** 2, 4 * a * c, blanco))
			print("\n\t\t{}\n\t\t{}\n\t\t{}{}".format(f1, "-" * len(f1), " " * f2, 2 * a))

			f1 = "{}+-{}".format(-b, sqrt((b ** 2) - (4 * a * c)))
			f2 = int(len(f1) / 2.2)

			time.sleep(times)
			
			print("\n\n\t\t{}Se calcula la raiz cuadrada de {}{}".format(naranja, (b ** 2) - (4 * a * c), blanco))			
			print("\n\t\t{}\n\t\t{}\n\t\t{}{}".format(f1, "-" * len(f1), " " * f2, 2 * a))

			time.sleep(times)

			print("\n\n\n\t\t\t{}Opcion 1:{}".format(naranja, blanco))

			f1 = "{}".format(-b + sqrt((b ** 2) - (4 * a * c)))
			f2 = int(len(f1) / 2.2)
			r2 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
			r4 = sqrt((-b+sqrt(b**2-(4*a*c)))/(2*a))

			time.sleep(times)

			print("\n\t\t\t{}\n\t\t\t{} = {} => x^2 = {} => x = +-~{} => x= +-{}\n\t\t\t{}{}".format(f1, "-" * len(f1), r2 , r2, r2, r4, " " * f2, 2 * a))
			
			time.sleep(times)

			print("\n\n\t\t\t{}Opcion 2:{}".format(naranja, blanco))

			f1 = "{}".format(-b - sqrt((b ** 2) - (4 * a * c)))		
			f2 = int(len(f1) / 2.2)
			r2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
			r4 = sqrt((-b-sqrt(b**2-(4*a*c)))/(2*a))
			
			time.sleep(times)
			
			print("\n\t\t\t{}\n\t\t\t{} = {} => x^2 = {} => x = +-~{} => x= +-{}\n\t\t\t{}{}".format(f1, "-" * len(f1), r2 , r2, r2, r4, " " * f2, 2 * a))


			opcion = input("\n\n{}Para volver al menu pulsa '{}m{}', para hacer otra equacion pulsa '{}r{}'\n\n\t>{}".format(naranja, blanco, naranja, blanco, naranja, blanco))
			if opcion == "m":
				menu()
			elif opcion == "r":
				equacionesBiquadradas()
			else:
				menu()
			
def sumas():
	error = "\x1b[1;31m"+"[!]"
	naranja ="\x1b[1;33m"
	cyan = "\x1b[1;36m"
	azul = "\x1b[1;34m"
	morado = "\x1b[1;35m"
	blanco = "\x1b[1;37m"
	
	a = []
	while True:
		os.system("clear")

		titol = "Sumas"
		print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))
		print("{}[*] Para romper el bucle pulsa 0{}\n".format(naranja, blanco))
		
		for valor in a:
			print("{}{}+".format(blanco, valor),end="")


		num = float(input(""))
		if num == 0:
			break
		
		else:
			os.system("clear")
			a.append(num)
		
	os.system("clear")

	titol = "Sumas"
	print("{}{}\n{}{}\n".format(cyan, titol,cyan,  "=" * (len(titol))))
	print("{}[*] Para romper el bucle pulsa 0{}\n".format(naranja, blanco))

	for valor in a:
			print("{}+".format(valor),end="")
	print(" = {}".format(fsum(a)))

	
	opcion = input("\n\n{}Para volver al menu pulsa '{}m{}', para hacer otra suma pulsa '{}r{}'\n\n\t>{}".format(naranja, blanco, naranja, blanco, naranja, blanco))
	if opcion == "m":
		menu()
	elif opcion == "r":
		sumas()
	else:
		menu()

def Restas():
	error = "\x1b[1;31m"+"[!]"
	naranja ="\x1b[1;33m"
	cyan = "\x1b[1;36m"
	azul = "\x1b[1;34m"
	morado = "\x1b[1;35m"
	blanco = "\x1b[1;37m"
	
	
	
	os.system("clear")

	titol = "Restas"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	num1 = float(input("{}".format(blanco)))

	
	os.system("clear")

	titol = "Restas"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	num2 = float(input("{}{}{} -{} ".format(blanco,num1,naranja,blanco)))

	
	os.system("clear")

	titol = "Restas"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	print("{}{}{} - {}{}{} = {}{}".format(blanco,num1,naranja,blanco,num2,naranja,blanco, num1 - num2))


	opcion = input("\n\n{}Para volver al menu pulsa '{}m{}', para hacer otra resta pulsa '{}r{}'\n\n\t>{}".format(naranja, blanco, naranja, blanco, naranja, blanco))
	if opcion == "m":
		menu()
	elif opcion == "r":
		Restas()
	else:
		menu()

def Multiplicacions():
	error = "\x1b[1;31m"+"[!]"
	naranja ="\x1b[1;33m"
	cyan = "\x1b[1;36m"
	azul = "\x1b[1;34m"
	morado = "\x1b[1;35m"
	blanco = "\x1b[1;37m"
	
	
	
	os.system("clear")

	titol = "Multiplicaiones"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	num1 = float(input("{}".format(blanco)))

	
	os.system("clear")

	titol = "Multiplicaciones"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	num2 = float(input("{}{}{} *{} ".format(blanco,num1,naranja,blanco)))

	
	os.system("clear")

	titol = "Multiplicaciones"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	print("{}{}{} * {}{}{} = {}{}".format(blanco,num1,naranja,blanco,num2,naranja,blanco, num1 * num2))


	opcion = input("\n\n{}Para volver al menu pulsa '{}m{}', para hacer otra multiplicacion pulsa '{}r{}'\n\n\t>{}".format(naranja, blanco, naranja, blanco, naranja, blanco))
	if opcion == "m":
		menu()
	elif opcion == "r":
		Multiplicacions()
	else:
		menu()

def Divisiones():
	error = "\x1b[1;31m"+"[!]"
	naranja ="\x1b[1;33m"
	cyan = "\x1b[1;36m"
	azul = "\x1b[1;34m"
	morado = "\x1b[1;35m"
	blanco = "\x1b[1;37m"
	
	
	
	os.system("clear")

	titol = "Multiplicaiones"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	num1 = float(input("{}".format(blanco)))

	
	os.system("clear")

	titol = "Multiplicaciones"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	num2 = float(input("{}{}{} /{} ".format(blanco,num1,naranja,blanco)))

	
	os.system("clear")

	titol = "Multiplicaciones"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	print("{}{}{} / {}{}{} = {}{}".format(blanco,num1,naranja,blanco,num2,naranja,blanco, num1 / num2))


	opcion = input("\n\n{}Para volver al menu pulsa '{}m{}', para hacer otra division pulsa '{}r{}'\n\n\t>{}".format(naranja, blanco, naranja, blanco, naranja, blanco))
	if opcion == "m":
		menu()
	elif opcion == "r":
		Divisiones()
	else:
		menu()


def Potencies():
	error = "\x1b[1;31m"+"[!]"
	naranja ="\x1b[1;33m"
	cyan = "\x1b[1;36m"
	azul = "\x1b[1;34m"
	morado = "\x1b[1;35m"
	blanco = "\x1b[1;37m"
	
	
	
	os.system("clear")

	titol = "Potencias"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	num1 = float(input("{}".format(blanco)))

	
	os.system("clear")

	titol = "Potencias"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	num2 = float(input("{}{}{}^{}".format(blanco,num1,naranja,blanco)))

	
	os.system("clear")

	titol = "Potencias"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	print("{}{}{}^{}{}{} = {}{}".format(blanco,num1,naranja,blanco,num2,naranja,blanco, num1 ** num2))


	opcion = input("\n\n{}Para volver al menu pulsa '{}m{}', para hacer otra potencia pulsa '{}r{}'\n\n\t>{}".format(naranja, blanco, naranja, blanco, naranja, blanco))
	if opcion == "m":
		menu()
	elif opcion == "r":
		Potencies()
	else:
		menu()


def Raiz():
	error = "\x1b[1;31m"+"[!]"
	naranja ="\x1b[1;33m"
	cyan = "\x1b[1;36m"
	azul = "\x1b[1;34m"
	morado = "\x1b[1;35m"
	blanco = "\x1b[1;37m"
	
	
	
	os.system("clear")

	titol = "Raiz Cuadrada"
	print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

	num1 = float(input("{}~ {}".format(naranja,blanco)))
	if num1 < 0:
		os.system("clear")
		
		print("{} Error".format(error))
	
	else:
		os.system("clear")

		titol = "Raiz Cuadrada"
		print("{}{}\n{}{}\n".format(cyan,titol, "=" * (len(titol)), cyan))

		print("{}~ {}{}{} = {}{}".format(naranja,blanco,num1,naranja,blanco, sqrt(num1)))


		opcion = input("\n\n{}Para volver al menu pulsa '{}m{}', para hacer otra raiz pulsa '{}r{}'\n\n\t>{}".format(naranja, blanco, naranja, blanco, naranja, blanco))
		if opcion == "m":
			menu()
		elif opcion == "r":
			Raiz()
		else:
			menu()


menu()