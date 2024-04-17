#haga una lista de listas para poder almacenar peliculas que va a contener nombre genero y calificacion 
peliculas = [
    ["titanic", "Romance", 10],["Deadpool", "Accion", 8],["Shrek", "Animacion", 9],["Coco", "Animacion", 10]
]

while True:
    print("########__MENU DE PELICULAS__########")
    print("# 1. Agregar una nueva pelicula      #")
    print("# 2. Mostrar la lista de peliculas   #")
    print("# 3. Editar una calificacion        #")
    print("# 4. Salir                           #")
    print("######################################")                           

    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        nueva_pelicula = input("Ingresa una nueva pelicula: ")
        genero = input("Ingresa el genero: ")
        calificacion = input("Ingresa la calificacion: ")
        peliculas.append([nueva_pelicula, genero, calificacion])
        print("Pelicula agregada correctamente")

    elif opcion == 2:
        print("Listado de peliculas:")
        for pelicula in peliculas:
            print( peliculas.index(pelicula) + 1,"->",pelicula)

    elif opcion == 3:
      #cambiar la calificacion de la una pelicula 
        print("Listado de peliculas:")
        for pelicula in peliculas:
            print( peliculas.index(pelicula) + 1,"->",pelicula)
        indice = int(input("Ingresa el indice de la pelicula: "))
        calificacion = float(input("Ingresa la calificacion: "))
        peliculas[indice - 1][2] = calificacion
        print("Pelicula editada correctamente")
    
    elif opcion == 4:
        break
