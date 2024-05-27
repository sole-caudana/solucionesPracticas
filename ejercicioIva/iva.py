# Calcular IVA

# Ingresar el precio del producto
precio = float(input("Ingrese el precio del producto: "))

# Calcular el IVA
iva = precio * 0.21

# Calcular el precio final
precio_final = precio + iva

# Mostrar el precio final
print("El precio final con IVA incluido es:", precio_final)