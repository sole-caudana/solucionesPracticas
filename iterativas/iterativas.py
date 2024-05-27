#Mostrar los números desde el 0 al número solicitado al usuario
numero = int(input("Ingrese un número: "))
for i in range(numero + 1):
    print(i)

#Mostrar sólo los números pares desde 0 hasta el número ingresado
numero = int(input("Ingrese un número: "))
for i in range(0, numero + 1):
    if i % 2 == 0:
        print(i)

#Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”
while True:
    nombre = input("Ingrese el nombre de una persona (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    print(nombre)