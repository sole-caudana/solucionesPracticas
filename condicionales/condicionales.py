#Condicional IF 
precio = float(input("Ingrese el precio del producto: "))
if precio > 1000:
    print("El precio es mayor a 1000")

#Condicional IF-ELSE
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Condicional IF
edad = int(input("Ingrese su edad: "))
if 18 <= edad <= 65:
    print("Está en edad laboral")

#Condicional IF-ELSE
temperatura = float(input("Ingrese la temperatura: "))
if temperatura < 0 or temperatura > 30:
    print("La temperatura está fuera del rango cómodo")
else:
    print("La temperatura está en el rango cómodo")