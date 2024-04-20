
#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
#(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
#que se le pida al usuario.
#Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
#diccionario vacio
dicionario_vacio = {}
#variable de cierre de ciclo en true para que se ejecute el while
conti = True

while conti:
    #pide la llave
    llave=input("Que dato desea ingresar:")
    #pide el valor
    valor = input(llave + " :") 
    #agrega la llave y el valor
    dicionario_vacio[llave] = valor
    #imprime el diccionario
    print(dicionario_vacio)
    #si el valor ingresado es s continua, de lo contratio cierra el ciclo porque la senencia pasa a ser false 
    conti = input("Desea continuar? (s/n):") == 's'
    
