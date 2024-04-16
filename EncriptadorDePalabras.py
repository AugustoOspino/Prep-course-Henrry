#encriptador de palabras 
#creamos un diccionario de letras del abecedario
abecedario_numeros = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    ' ': 0

}
abecedario_numeros_invertido = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z',
    0: ' '
}



def encriptar(palabra_a_encriptar):

 #convertimos la palabra en minusculas
    palabra_a_encriptar = palabra_a_encriptar.lower()
    #pasamos la palabra a un vector
    vector_palabra = list(palabra_a_encriptar)
    #creamos una variable vacia para la palabra encriptada
    palabra_encriptada = []
    #recorremos el vector de la palabra
    for letra in vector_palabra:
        #buscamos la letra en el diccionario
        if letra in abecedario_numeros:
            #si la letra esta en el diccionario, la encriptamos
            numero_encriptado = abecedario_numeros[letra]
            #agregamos el numero encriptado a la palabra encriptada
            palabra_encriptada.append(str(numero_encriptado))
        else:
            #si la letra no esta en el diccionario, no la encriptamos
            palabra_encriptada.append(letra)
     #retornamos la palabra encriptada imprimiendo el vector
    return "-".join(palabra_encriptada)

   
      


 

def desencriptar(palabra_a_desencriptar):
    #separamos los numeros por el guion
    numeros_separados = palabra_a_desencriptar.split('-')
    #convertimos los numeros a enteros
    numeros_en_enteros = [int(numero) for numero in numeros_separados]
    #creamos una variable vacia para la palabra desencriptada
    palabra_desencriptada = ""
    #recorremos el vector de los numeros en enteros
    for numero_en_entero in numeros_en_enteros:
        #buscamos el numero en el diccionario
        if numero_en_entero in abecedario_numeros_invertido:
            #si el numero esta en el diccionario, la desencriptamos
            letra_desencriptada = abecedario_numeros_invertido[numero_en_entero]
            #agregamos la letra desencriptada a la palabra desencriptada
            palabra_desencriptada += letra_desencriptada
        else:
            #si el numero no esta en el diccionario, no la desencriptamos
            palabra_desencriptada += str(numero_en_entero)
    #retornamos la palabra desencriptada imprimiendo el vector
    return palabra_desencriptada


#creamos un menu para encriptar o desencriptar
print("1. Encriptar")
print("2. Desencriptar")
output = int(input("Ingresa una opcion: "))
if output == 1:
    palabra_a_encriptar = input("Ingresa una palabra: ")
    print("La palabra encriptada es: ",encriptar(palabra_a_encriptar))
elif output == 2:
    palabra_a_desencriptar = input("Ingresa una palabra: ")
    print("La palabra desencriptada es: ",desencriptar(palabra_a_desencriptar))
else:
    print("Opcion invalida")

