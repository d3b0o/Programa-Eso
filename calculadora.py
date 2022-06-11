#####################################
#                                   #
#     CALCULADORA MATES by d3b0     #
#         Windows and Linux         #
# 	     	04/03/2022              #
#                                   #
#####################################

from dis import Instruction
import math
from msilib.schema import Error
import sqlite3 as sql
import os
from math import sqrt
import time

from numpy import true_divide

def comando():
	
	# IMPORTANTE!!! 
	# - Si estas en LINUX pon un Hashtag en el comando CLS 
	# - Si estas en WINDOWS pon un Hashtag en el comando CLEAR
	# - Por defecto esta por windows

	comando = "cls"
	#comando = "clear"
	return comando

def titulos(titol, subtitol, type):

	if type == "main":
		mensaje = ("{}+{}+\n{}|{}{}|\n{}+{}+\n".format(cyan(),"-" * (len(titol) + len(subtitol)) ,cyan() ,titol, subtitol,cyan(), "-" * (len(titol) + len(subtitol))))
	
	elif type == "sub":
		mensaje = "{}{}{}\n{}\n".format(cyan(), titol, subtitol, "=" * ((len(titol)) + len(subtitol)))
	
	return mensaje

### COLORES ###
def cyan():
	cyan = "\x1b[1;36m"
	return cyan

def white():
	white = "\x1b[1;37m"
	return white

def red():
	red = "\x1b[1;31m"
	return red

def error():
	error = "\x1b[1;31m"+"[!]"
	return error

def naranja():
	naranja = "\x1b[1;33m"
	return naranja
################

def main():
	os.system(comando())
	print(titulos("MAIN", " by d3b0", "main"))
	opcion = int(input("{}\t1- Mates\n\n\t2- Ingles\n\n\t0- Exit\n\n\t\t>{} ".format(naranja(), white())))
	if opcion == 1:
		mates()
	elif opcion == 2:
		ingles()
	elif opcion == 0:
		os.system(comando())
		print("{}[!] Saliendo...{}".format(red(), white()))
		exit()
	
def ingles():
	os.system(comando())
	print(titulos("Ingles", "", "main"))
	opcion = int(input("{}\t1- Irregular Verbs\n\n\t0- Menu\n\n\t\t>{} ".format(naranja(), white())))
	if opcion == 1:
		irregularVerbs()
	elif opcion == 0:
		main()

def irregularVerbs():		
	os.system(comando())
	def infinitive(verb):
		conn = sql.connect("IrregularVerbs.db")
		cursor = conn.cursor()
		cursor.execute(f"SELECT * FROM IrregularVerbs WHERE infinitive=:verb", {"verb": verb})
		datosinfinitive = cursor.fetchall()
		conn.commit()
		conn.close()
		return datosinfinitive
	
	def pastsimple(verb):
		conn = sql.connect("IrregularVerbs.db")
		cursor = conn.cursor()
		cursor.execute(f"SELECT * FROM IrregularVerbs WHERE pastsimple=:verb", {"verb": verb})
		datossimple = cursor.fetchall()
		conn.commit()
		conn.close()
		return datossimple

	def pastparticiple(verb):
		conn = sql.connect("IrregularVerbs.db")
		cursor = conn.cursor()
		cursor.execute(f"SELECT * FROM IrregularVerbs WHERE pastparticiple=:verb", {"verb": verb})
		datosParticiple = cursor.fetchall()
		conn.commit()
		conn.close()
		return datosParticiple

	print(titulos("Irregular Verbs", "", "sub"))
	verb = input("{}[*] Introduce el {}verbo{} que quieres buscar:{} ".format(naranja(),white(),naranja(),white()))
	
	a = infinitive(verb)
	b = pastsimple(verb)
	c = pastparticiple(verb)	
	
	print(a)
	print(b)
	print(c)
	
	if len(a) != 0:
		for item in a:
			primero = item[0]
			segundo = item[1]
			tercero = item[2]

		os.system(comando())
		print(titulos("Irregular Verbs", "", "sub"))
		opcion = int(input("{}Que quieres consultar del verbo '{}{}{}'\n\n\t1- Toda la fila\n\n\t2- Past simple\n\n\t3- Past participle\n\n\t\t>{} ".format(naranja(),white(), verb, naranja(), white())))
		if opcion == 1:
			os.system(comando())
			print(titulos("Irregular Verbs", "", "sub"))
			print("{}Verbo: {}{}{}\n\nInfinitive: {}{}{}\nPast simple: {}{}{}\nPast Participle: {}{}{}".format(naranja(), white(), verb,  naranja(), white(),primero, naranja(), white(), segundo,naranja(), white(),tercero, naranja()))
			opcion = input("\n[*] Pulsa 'm' para volver al menu\n    Pulsa 'r' para buscar otro verbo")
			if opcion == "m":
				main()
			if opcion == "r":
				irregularVerbs()
		elif opcion == 2:
			os.system(comando())
			print("Past simple de {}: {}".format(verb,segundo))

		elif opcion == 3:
			os.system(comando())
			print("Past participle de {}: {}".format(verb,tercero))

	elif len(b) != 0:
		for item in b:
			primero = item[0]
			segundo = item[1]
			tercero = item[2]

		os.system(comando())
		opcion = int(input("Que quieres consultar del verbo '{}'\n1- Toda la fila\n2- Infinitive\n3- Past participle\n\n\t".format(verb)))
		if opcion == 1:
			os.system(comando())
			print("Verb: {}\n\nInfinitive: {}\nPast simple: {}\nPast Participle: {}".format(verb,primero, segundo, tercero))

		elif opcion == 2:
			os.system(comando())
			print("Infinitive de {}: {}".format(verb,primero))

		elif opcion == 3:
			os.system(comando())
			print("Past participle de {}: {}".format(verb,tercero))
	elif len(c) != 0:
		for item in c:
			primero = item[0]
			segundo = item[1]
			tercero = item[2]

		os.system(comando())
		opcion = int(input("Que quieres consultar del verbo '{}'\n1- Toda la fila\n2- Infinitive\n3- Past participle\n\n\t".format(verb)))
		if opcion == 1:
			os.system(comando())
			print("Verb: {}\n\nInfinitive: {}\nPast Simple: {}\nPast Participle: {}".format(verb,primero, segundo, tercero))

		elif opcion == 2:
			os.system(comando())
			print("Infinitive de {}: {}".format(verb,primero))

		elif opcion == 3:
			os.system(comando())
			print("Past Simple de {}: {}".format(verb,segundo))

def mates():

	
	os.system(comando())

	print(titulos(" PROGRAMA DE MATES", "by d3b0", "main"))
	
	print("{} La raiz cuadrada esta expresada con '{}~{}'\n".format(error(), white(),red()))
	opcion = input("{}\n\t1- Equaciones\n\n\t2- Operaciones Basicas\n\n\t3- Funcions\n\n\t4- Trigonometria\n\n\t0- Exit\n\n\t\t>{} ".format(naranja(), white()))
	if opcion == "mila":
		os.system(comando())
		titol = " Insultos"
		subtitol = " mila "
		type = "main"
		print(titulos(titol,subtitol,type))
		print("{}Asquerosa\nSucia\nMal olienta".format(white()))
	else:
		opcion = int(opcion)
		if opcion == 1:
			equaciones()
		
		elif opcion == 2:
			opb()

		elif opcion == 3:
			funcions()
		
		elif opcion == 4:
			trigonometria()

		elif opcion == 0:
			os.system(comando())
			
			print("\n{} Saliendo...".format(error()))

		else:
			error()
		
def equaciones():
	titol = "Equaciones"
	subtitol = ""
	type = "main"

	os.system(comando())
	print(titulos(titol, subtitol, type))
	
	opcion = int(input("{}\n\t1- [nx^2 nx n] Equaciones de Segundo Grado\n\n\t2- [nx^4 nx^2 n] Equaciones Biquadradas\n\n\t3- [nx^4 nx^3 nx^2 nx n] Equaciones Polinomiques\n\t\n\n\t9- Menu\n\n\t0- Exit\n\n\t\t>{} ".format(naranja(), white())))
	if opcion == 1:
		equaciones2grado()
	elif opcion == 2:
		equacionesBiquadradas()
	elif opcion == 3:
		rufini()
	elif opcion == 0:
		os.system(comando())
		
		print("\n{} Saliendo...".format(error()))
	elif opcion == 9:
		mates()
	else:
		os.system(comando())

		print("\n{} Error".format(error()))

def equaciones2grado():
	titol = "Equaciones de 2 Grado"
	subtitol = ""
	type = "sub"
	
	os.system(comando())
	
	def fin():
		mensaje = "{}\n[*] Para VOLVER al MENU pulsa '{}m{}'\n    Para HACER OTRA pulsa '{}r{}'\n\t>{} ".format(naranja(),white(),naranja(),white(),naranja(),white())
		return mensaje
	
	def mostrar():
		mensaje = "{}\n[*] Para MOSTRAR los pasos pulsa '{}o{}'\n    Para HACER OTRA equacion pulsa '{}r{}'\n    Para VOLVER al MENU pulsa '{}m{}'\n\t>{} ".format(naranja(),white(),naranja(),white(),naranja(),white(),naranja(),white())
		return mensaje
	
	def pasos(a, b, c):
		times = 0.2
		f1 = "-b+-~b^2-4·a·c"
		f2 = int(len(f1) / 2.5)
		print("\n\t\t{}{}\n\t    x = --------------\n\t\t{}2 · a".format(white(),f1, " " * f2))
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
		print("\n\n\t\t{}Opcion 1:{}".format(naranja(), white()))
		f1 = "{}".format(-b + sqrt((b ** 2) - (4 * a * c)))			
		f2 = int(len(f1) / 2.2)
		time.sleep(times)
		print("\n\t\t{}\n\t\t{} = {}\n\t\t{}{}".format(f1, "-" * len(f1), (-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a), " " * f2 , 2 * a))
		time.sleep(times)
		print("\n\n\t\t{}Opcion 2:{}".format(naranja(), white()))
		f1 = "{}".format(-b - sqrt((b ** 2) - (4 * a * c)))			
		f2 = int(len(f1) / 2.2)
		time.sleep(times)
		print("\n\t\t{}\n\t\t{} = {}\n\t\t{}{}".format(f1, "-" * len(f1), (-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a), " " * f2 , 2 * a))
	
	print(titulos(titol, subtitol, type))
	
	print("{}[*] Ejemplo 1x^2-5x+6".format(naranja()))
	inp = input("\n\t> {}".format(white()))

	a = int(inp.split("x")[0])
	b = int(inp.split("^2")[-1].split("x")[0])
	c = int(inp.split("x")[-1])
	
	print("\n{}a = {}{}{}\nb = {}{}{}\nc = {}{}{}".format(naranja(),white(), a,naranja(),white(), b,naranja(),white(), c, naranja()))

	b1 = -b
	if ((b**2)-4*a*c) < 0:
		print("\n{}No tiene Resultado o a ocurrido un errror, revisa los datos introducidos".format(error()))
		while True:
			opcion = input(fin())
			if opcion == "m":
				equaciones()
				break
			
			elif opcion == "r":
				equaciones2grado()
				break
			
			else:
				os.system(comando())
				print("\n{}[!] Error la letra introducida no es valida".format(red()))

	else:
		xpositiva = (-b+sqrt(b**2-(4*a*c)))/(2*a)
		xnegativa = (-b-sqrt(b**2-(4*a*c)))/(2*a)
		
		print("\n{}[*] Resultado: {}{} {}/{} {}".format(naranja(), white(), xpositiva, naranja(), white(), xnegativa))
		
		time.sleep(1)
		
		while True:
			opcion = input(mostrar())
			if opcion == "m":
				equaciones()
				break
			elif opcion == "r":
				equaciones2grado()
				break
			elif opcion == "o":
				pasos(a, b, c)
				break
			else:
				os.system(comando())
				print("\n{}[!] Error la letra introducida no es valida".format(red()))
				
		while True:
			opcion = input(fin())
			if opcion == "m":
				equaciones()
				break
			elif opcion == "r":
				equaciones2grado()
				break
			else:
				os.system(comando())
				print("\n{}[!] Error la letra introducida no es valida".format(red()))
			
def equacionesBiquadradas():
	titol = "Equaciones Biquadradas"
	subtitol = ""
	type = "sub"

	def fin():
		mensaje = "{}\n[*] Para VOLVER al MENU pulsa '{}m{}'\n    Para HACER OTRA pulsa '{}r{}'\n\t>{} ".format(naranja(),white(),naranja(),white(),naranja(),white)
		return mensaje

	def mostrar():
		mensaje = "{}\n[*] Para MOSTRAR los pasos pulsa '{}o{}'\n    Para HACER OTRA equacion pulsa '{}r{}'\n    Para VOLVER al MENU pulsa '{}m{}'\n\t> ".format(naranja(),white(),naranja(),white(),naranja(),white(),naranja(),white)
		return mensaje
	
	def pasos(a,b,c):
		times = 0.2
		f1 = "-b+-~b^2-4·a·c"
		f2 = int(len(f1) / 2.5)
		g = "z = "
		print("\n\t\t{}Formula{}".format(naranja(), white()))
		print("\n\t\t{}{}\n\t\t{}--------------\n\t\t{}2 · a".format(" " * len(g),f1,g,  " " * f2))
		f1 = "-{}+-~{}^2-4·{}·{}".format(b, b, a, c,)
		f2 = int(len(f1) / 2.5)
		time.sleep(times)
		print("\n\n\t\t{}Se sustituye a b c por los numeros corespondientes{}".format(naranja(), white()))
		print("\n\t\t{}\n\t\t{}\n\t\t{}2 · {}".format(f1, "-" * len(f1), " " * f2, a))
		f1 = "{}+-~{}-{}".format(-b, b ** 2, 4 * a * c)
		f2 = int(len(f1) / 2.2)
		time.sleep(times)
		print("\n\n\t\t{}Se calcula {}^2 y 4 * {} * {}{}".format(naranja(), b, a, c, white()))
		print("\n\t\t{}\n\t\t{}\n\t\t{}{}".format(f1, "-" * len(f1), " " * f2, 2 * a))
		f1 = "{}+-~{}".format(-b,(b ** 2) - (4 * a * c) )
		f2 = int(len(f1) / 2.2)
		time.sleep(times)
		print("\n\n\t\t{}Se calcula {}-{}{}".format(naranja(), b ** 2, 4 * a * c, white()))
		print("\n\t\t{}\n\t\t{}\n\t\t{}{}".format(f1, "-" * len(f1), " " * f2, 2 * a))
		f1 = "{}+-{}".format(-b, sqrt((b ** 2) - (4 * a * c)))
		f2 = int(len(f1) / 2.2)
		time.sleep(times)
		print("\n\n\t\t{}Se calcula la raiz cuadrada de {}{}".format(naranja(), (b ** 2) - (4 * a * c), white()))			
		print("\n\t\t{}\n\t\t{}\n\t\t{}{}".format(f1, "-" * len(f1), " " * f2, 2 * a))
		time.sleep(times)
		if (-b+sqrt(b**2-(4*a*c)))/(2*a) < 0:
			...
		else:
			print("\n\n\n\t\t\t{}Opcion 1:{}".format(naranja(), white()))
			f1 = "{}".format(-b + sqrt((b ** 2) - (4 * a * c)))
			f2 = int(len(f1) / 2.2)
			r2 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
			r4 = sqrt((-b+sqrt(b**2-(4*a*c)))/(2*a))
			time.sleep(times)
			print("\n\t\t\t{}\n\t\t\t{} = {} => x^2 = {} => x = +-~{} => x= +-{}\n\t\t\t{}{}".format(f1, "-" * len(f1), r2 , r2, r2, r4, " " * f2, 2 * a))
		if (-b-sqrt(b**2-(4*a*c)))/(2*a) < 0:
			...
		else:
			time.sleep(times)
			print("\n\n\t\t\t{}Opcion 2:{}".format(naranja(), white()))
			f1 = "{}".format(-b - sqrt((b ** 2) - (4 * a * c)))		
			f2 = int(len(f1) / 2.2)
			r2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
			r4 = sqrt((-b-sqrt(b**2-(4*a*c)))/(2*a))
			time.sleep(times)
			print("\n\t\t\t{}\n\t\t\t{} = {} => x^2 = {} => x = +-~{} => x= +-{}\n\t\t\t{}{}".format(f1, "-" * len(f1), r2 , r2, r2, r4, " " * f2, 2 * a))
		
	def Resolver(a,b,c):
		mas = sqrt((-b+sqrt(b**2-(4*a*c)))/(2*a))
		menos = sqrt((-b-sqrt(b**2-(4*a*c)))/(2*a))
		resultat = []
		eq = b**2 - 4 * a * c
		if eq < 0:
			while True:
				print("{}\n[!] Los datos introducidos no son validos o a ocurrido un error\n".format(red()))
				opcion = input(fin()) 
				if opcion == 'm':
					equaciones()
					break
				elif opcion == 'r':
					equacionesBiquadradas()
					break
				else:
					os.system(comando())
					print("\n{}[!] Error la letra introducida no es valida".format(red()))
		
		elif eq == 0:
			x = -b / (2 * a)
			print("La unica solucion es {}".format(x))
		
		else:
			if (-b+sqrt(b**2-(4*a*c)))/(2*a) < 0:
				...
			else:
				resultat.append(mas)
			
			if (-b-sqrt(b**2-(4*a*c)))/(2*a) < 0:
				...
			else:
				resultat.append(menos)
			
			print("\n{}[*] Resultat:".format(naranja()),end=" ") 
			for i in resultat:
				print("{}+-{}{}".format(naranja(), white(), i),end=" ")
			print("")

			
			
	
	
	os.system(comando())
	print(titulos(titol, subtitol, type))
	print("{}[*] Ejemplo 1x^4-10x^2+9=0".format(naranja()))
	inp = input("\n\t> {}".format(white()))

	a = int(inp.split("x")[0])
	b = int(inp.split("^4")[-1].split("x")[0])
	c = int(inp.split("^2")[-1].split("=")[0])
	
	print("\n{}x^2 = {}z\n{}x^4 = {}z^2".format(naranja(), white(), naranja(), white()))
	print("\n{} = {}z^2 {}z {} = 0".format(inp, a, b, c))
	print("\n{}a = {}{}\n{}b = {}{}\n{}c = {}{}".format(naranja(), white(), a,naranja(), white() ,b, naranja(), white(), c))
	
	Resolver(a, b, c)
	
	opcion = input(mostrar())
	
	if opcion == "r":
		equacionesBiquadradas()
		
	elif opcion == "o":
		pasos(a,b,c)
		time.sleep(1)
		while True:
			opcion = input(fin())
			if opcion == "m":
				equaciones()
				break
			
			elif opcion == "r":
				equaciones2grado()
				break
			
			else:
				os.system(comando())
				print("\n{}[!] Error la letra introducida no es valida".format(red()))
			
	elif opcion == "m":
		equaciones()
		
	else:
		mates()
			
def opb():
	titol = "Operaciones Basicas"
	type = "sub"
	def fin():
		mensaje = "{}\n[!] Error el signo itroducido no es valido\n   Para VOLVER al MENU pulsa '{}m{}'\n   Para HACER OTRA pulsa '{}r{}'\n   >{} ".format(naranja(),white(),naranja(),white(),naranja(),white())
		return mensaje
	
	def final():
		mensaje = "{}\nPara VOLVER al MENU pulsa '{}m{}'\nPara HACER OTRA pulsa '{}r{}'\n\t>{} ".format(naranja(),white(),naranja(),white(),naranja(),white())
		return mensaje
	
	def suma(a, b):
		os.system(comando())
		subtitiol = " (sumas)"
		print(titulos(titol, subtitiol, type))
		print("\t{}{} {}{} {}{} {}= {}{}".format(white(),a,naranja(), s,white(), b ,naranja(),white(), a + b))
	
	def resta(a, b):
		os.system(comando())
		titol = "Operaciones"
		subtitiol = " (restas)"
		type = "sub"
		print(titulos(titol, subtitiol, type))
		print("\t{}{} {}{} {}{} {}= {}{}".format(white(),a,naranja(), s,white(), b ,naranja(),white(), a - b))
	
	def division(a, b):
		os.system(comando())
		titol = "Operaciones Basicas"
		subtitiol = " (divisiones)"
		type = "sub"
		print(titulos(titol, subtitiol, type))
		print("\t{}{} {}{} {}{} {}= {}{}".format(white(),a,naranja(), s,white(), b ,naranja(),white(), a / b))
	
	def multiplicacion(a, b):
		os.system(comando())
		titol = "Operacions Basiques"
		subtitiol = " (multiplicaciones)"
		type = "sub"
		print(titulos(titol, subtitiol, type))
		print("\t{}{} {}{} {}{} {}= {}{}".format(white(),a,naranja(), s,white(), b ,naranja(),white(), a * b))

	titol = " Operaciones Basicas "
	subtitol = ""
	type = "sub"

	os.system(comando())
	print(titulos(titol, subtitol, type))
	print("{}[*] Pon el primer numero y presiona ENTER".format(naranja()))
	a = float(input("\n\t{}".format(white())))

	os.system(comando())
	print(titulos(titol, subtitol, type))
	print("{}[*] Pon el signo y presiona ENTER".format(naranja()))
	s = input("\n\t{}{}{} ".format(white(),a,naranja()))
	
	os.system(comando())
	print(titulos(titol, subtitol, type))
	print("{}[*] Pon el segundo numero y presiona ENTER".format(naranja()))
	b = float(input("\n\t{}{} {}{}{} " .format(white(),a,naranja(),s, white())))

	if s == "+":
		suma(a, b)
		
	elif s == "-":
		resta(a, b)

	elif s == "/":
		division(a, b)

	elif s == "*":
		multiplicacion(a, b)
	
	else:
		while True:
			opcion = input(fin())
			if opcion == "m":
				mates()
				break
			elif opcion == "r":
				opb()
				break
			else:
				os.system(comando())
				print("\n{}[!] Error la letra introducida no es valida".format(red()))
	
	while True:
			opcion = input(final())
			if opcion == "m":
				mates()
				break
			elif opcion == "r":
				opb()
				break
			else:
				...

def rufini():
	titol = "Ruffini"
	subtitol = ""
	type = "sub"
	
	def fin():
		mensaje = "{}\n[*] Para VOLVER al MENU pulsa '{}m{}'\n    Para HACER OTRA pulsa '{}r{}'\n\t>{} ".format(naranja(),white(),naranja(),white(),naranja(),white)
		return mensaje
	
	os.system(comando())
	
	print(titulos(titol, subtitol, type))
	print("\n{}Ejemplo: 0x^4+3x^3+2x^2-19x+6=0".format(naranja()))
	inp = input("{}\n\t>{} ".format(naranja(),white()))
	a = int(inp.split("x^4")[0])
	b = int(inp.split("^4")[-1].split("x")[0])
	c = int(inp.split("^3")[-1].split("x")[0])
	d = int(inp.split("^2")[-1].split("x")[0])
	e = int(inp.split("x")[-1].split("=")[0])

	dalt = " {} {} {} {} {}".format(a, b, c, d, e)
	divisors = []
	time = 0
	while True:
		time += 1
		if e % time == 0:
			divisors.append(time)
		elif time == 1000:
			break

	print("\n{}Divisors de{} {}{}: ({} ".format(naranja(),white(),e,naranja(),white()),end="")
	for element in divisors:
		print("+-{}".format(element), end=" ")
	print("{}){}\n".format(naranja(),white()))
	h = -(divisors[0])

	gg = 0
	veces = -1
	while True:
		veces += 1
		if veces == len(divisors):
			gg += 1
			break
		
		a2 = a
		b2 = (a2 * divisors[veces]) + b
		c2 = (b2 * divisors[veces]) + c
		d2 = (c2 * divisors[veces]) + d
		e2 = (d2 * divisors[veces]) + e

		if e2 == 0:
			times = -divisors[veces]
			print("\n{}[*] con {}{} {}da {}0{}!{}".format(naranja(),white(),divisors[veces],naranja(),white(),naranja(),white()))

	veces = -1
	while True:
		veces += 1
		if veces == len(divisors):
			gg += 1
			break
		
		a2 = a
		b2 = (a2 * -divisors[veces]) + b
		c2 = (b2 * -divisors[veces]) + c
		d2 = (c2 * -divisors[veces]) + d
		e2 = (d2 * -divisors[veces]) + e

		if e2 == 0:
			times = -divisors[veces]
			print("\n{}[*] con {}{} {}da {}0{}!{}".format(naranja(),white(),-divisors[veces],naranja(),white(),naranja(),white()))
	
	usados = []
	usados.append(times)

	h = times
	
	a2 = a
	b2 = (a2 * times) + b
	c2 = (b2 * times) + c
	d2 = (c2 * times) + d
	e2 = (d2 * times) + e

	dalt = " {} {} {} {} {}".format(a, b, c, d, e)
	print("\n\n{}|{}\n{}|   {} {} {} {}\n{}+{}".format(" " * len(str(h)) , dalt, times,a2 * times, b2 * times, c2 * times, d2 * times," " * len(str(h)), "-" * len(dalt)))
	print("{}{} {} {} {} {} {}\n\n".format(white()," " * (len(str(h)) + 1),a2, b2, c2, d2, e2))
	if a2 == 0:
		...
	else:
		print("{}x^3".format(a2), end=" ")
	
	if b2 == 0:
		...
	else:
		print("{}x^2".format(b2), end=" ")
	
	if c2 == 0:
		...
	else:
		print("{}x".format(c2), end=" ")
	
	if d2 == 0:
		...
	else:
		print("{}".format(d2), end=" ")

	while True:
		opcion = input("\n{}".format(fin()))
		if opcion == "m":
			equaciones()
			break
		
		elif opcion == "r":
			equaciones2grado()
			break
		
		else:
			os.system(comando())
			print("\n{}[!] Error la letra introducida no es valida".format(red()))

def funcions():
	while True:
		os.system(comando())
		titol = "Funcions"
		subtitol = ""
		type = "sub"
		print(titulos(titol, subtitol, type))
		def info():
			print("""
Ejemplo:
		
	 a     c
	--- + ---
	 b     d
		""".format(naranja()))
			print("[*]Introduze los datos como se muestran arriba\n")
		info()
		a = int(input("a = "))
		os.system(comando())
		print(titulos(titol, subtitol, type))
		info()
		b = int(input("b = "))
		os.system(comando())
		print(titulos(titol, subtitol, type))
		info()
		c = int(input("c = "))
		os.system(comando())
		print(titulos(titol, subtitol, type))
		info()
		d = int(input("d = "))
		os.system(comando())
		print(titulos(titol, subtitol, type))
		ab = a - b
		if ab == 0:
			size = len(str(b))
		print("a = {}  b = {}  c = {}  d = {}".format(a, b, c, d))
		confirmacion = input("\nQuieres hacer algun cambio? [s/n]")
		if confirmacion == "s":
			pass
		elif confirmacion == "n":
			break

	op = input("\nIndica que tipo de operacion quieres hacer [+,-,*]: ")
	
def trigonometria():
	def hipotenusa(a,o,c,h):
		if h != 0:
			print("Error")
		else:
			if c and a != 0:
				hipotenusa = math.cos(a) * c
				print("cos({}) = {}/x => {} * {} = x => x = {}".format(a,c,math.cos(a), c, hipotenusa ))

			elif o and a != 0:
				hipotenusa = math.sin(a) * o
				print("sin({}) = {}/x => {} * {} = x => x = {}".format(a,o,math.sin(a), o, hipotenusa ))
	
	
	def oposat(a,o,c,h):
		if o != 0:
			print("Error")
		else:
			if c and a != 0:
				oposat = math.tan(a) * c
				print("tan({}) = x/{} => {} * {} = x => x = {}".format(a,c,math.tan(a), c, oposat ))
					
			elif h and a != 0:
				oposat = math.sin(a) * h
				print("sin({}) = x/{} => {} * {} = x => x = {}".format(a,h,math.sin(a), h, oposat ))
			

	def contigu(a,o,c,h):
				if c != 0:
					print("Error")
				else:
					if o and a != 0:
						contigu = math.tan(a) * o
						print("tan({}) = {}/x => {} * {} = x => x = {}".format(a,o,math.tan(a), o , contigu))

					elif h and a != 0:
						contigu = math.cos(a) * h
						print("cos({}) = x/{} => {} * {} = x => x = {}".format(a,h,math.cos(a), h ,contigu))

				
			
				

	def pasos(a,o,c,h):
		print("a")
	while True:
		os.system(comando())
		print(titulos("Trigonometria","","sub"))
		print("Si no sabes su valor pon 0")
		a = float(input("α = "))

		
		os.system(comando())
		
		print(titulos("Trigonometria","","sub"))
		print("Si no sabes su valor pon 0")
		o = float(input("Catet Oposat = "))

		os.system(comando())
		print(titulos("Trigonometria","","sub"))
		print("Si no sabes su valor pon 0")
		c = float(input("Catet Contigu = "))

		os.system(comando())
		print(titulos("Trigonometria","","sub"))
		print("Si no sabes su valor pon 0")
		h = float(input("Hipotenusa = "))
		while True:
			os.system(comando())
			print(titulos("Trigonometria","","sub"))
			opcion = int(input("Que quieres saber\n\t1- Hipotenusa\n\t2- Catet Oposat\n\t3- Catet Contigu\n\t\t> "))
			if opcion == 1:
				
				hipotenusa(a,o,c,h)
			elif opcion == 2:

				oposat(a,o,c,h)
			elif opcion == 3:
			
				contigu(a,o,c,h)
			opcionn = input("\n[*]Esriu 'r' per ferne un altre\n\t> ")
			if opcionn == "o":
				print()
			elif opcionn == "r":
				trigonometria()

	

if __name__ == "__main__":
	main()
		

