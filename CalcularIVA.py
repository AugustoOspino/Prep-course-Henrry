#Diseña un algoritmo que calcule el IVA (19%) de un producto dado su precio de venta sin IVA.

precio = int(input("Ingresa el precio de venta sin IVA: "))

iva = precio * 0.19

print("El IVA es: ", iva)
print("El precio de venta con IVA es: ", precio + iva)