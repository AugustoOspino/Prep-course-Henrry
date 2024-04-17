#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

#Fruta	Precio
#Plátano	1.35
#Manzana	0.80
#Pera	0.85
#Naranja	0.70
frutas =  { "Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

fruta = input("Introduce una fruta: ").title()
kilos = int(input("Introduce los kilos: "))

if fruta in frutas:
    print(f"El precio de {kilos} kilos de {fruta} es {frutas[fruta] * kilos}")
else:
    print(f"La fruta {fruta} no existe en el diccionario")