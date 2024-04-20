
#Escribir un programa que cree un diccionario simulando una cesta de la compra.
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
# hasta que el usuario decida terminar. 
#Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

# cesta de  compras 
cesta = {}

conti = True
while conti:
    print ("ingrese los datos de compra ")
    nombre = input ("ingrese el producto: ")
    valor = int(input("ingrese el valor: "))
    cesta[nombre]=valor
    conti = input("¿desea agregar otro elemento?(s/n) ") == 's'

for datos, valor  in cesta.items():
     print(f'{datos}: {valor}')

print("total a pagar: ", sum(cesta.values()))       