print("hello world")

# crear un menu con opciones para saber los dias de la semana

# crear una lista de dias de la semana
dias_de_la_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# pedir al usuario que ingrese un dia de la semana

dia = int(input("Ingresa un dia de la semana 1- 7 : "))
print(dias_de_la_semana[dia - 1])
