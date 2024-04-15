# cuantos dias han pasao desde tu nacimiento
nacimiento = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")
#obtener la fecha de hoy
from datetime import datetime
hoy = datetime.now()
#convertir la fecha de nacimiento a un objeto datetime
nacimiento_obj = datetime.strptime(nacimiento, '%d/%m/%Y')
#obtener la diferencia entre la fecha de nacimiento y la fecha de hoy
diferencia = hoy - nacimiento_obj
#obtener la diferencia en dias
dias = diferencia.days
print("Has vivido", dias, "dias")