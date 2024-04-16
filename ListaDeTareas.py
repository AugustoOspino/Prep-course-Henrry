from itertools import islice


tareas = ["comprar leche", "limpiar el baño", "ir al gimnasio", "programar en python"]
while True:
 #Crear un listado de tareas por hacer 

 print("########__MENU DE TAREAS__########")
 print("# 1. Crear una nueva tarea       #")
 print("# 2. Mostrar el listado tareas   #")
 print("# 3. Eliminar una tarea          #")
 print("# 4. Salir                       #")
 print("##################################")

 opcion = int(input("Ingresa una opcion: "))
 if opcion == 1:
    nueva_tarea = input("Ingresa una nueva tarea: ")
    tareas.append(nueva_tarea)
    print("Tarea agregada correctamente")
    print("  ")
 elif opcion == 2:
    print("Listado de tareas por hacer:")
    for tarea in tareas:
        print( tareas.index(tarea) + 1,"->",tarea)
    print("  ")
 elif opcion == 3:
    tarea_a_eliminar = input("Ingresa la tarea a eliminar: ")  
    if tarea_a_eliminar in tareas:
        tareas.remove(tarea_a_eliminar) 
        print("Tarea eliminada correctamente")
        print("  ")
    else:
        print("Tarea no encontrada")
 elif opcion == 4:
    print("Hasta luego")
    print("  ")
    break
 else:
     print("Opcion invalida")


