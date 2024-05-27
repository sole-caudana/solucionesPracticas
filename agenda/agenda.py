def mostrar_menu():
    print("\nAgenda Telefónica")
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

def agregar_persona(agenda):
    dni = input("Ingrese el DNI: ")
    if dni in agenda:
        print("El DNI ya está registrado en la agenda.")
        return
    apellido = input("Ingrese el apellido: ")
    nombre = input("Ingrese el nombre: ")
    email = input("Ingrese el email: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[dni] = {
        "Apellido": apellido,
        "Nombre": nombre,
        "Email": email,
        "Teléfono": telefono
    }
    print("Persona agregada correctamente.")

def modificar_persona(agenda):
    dni = input("Ingrese el DNI de la persona a modificar: ")
    if dni not in agenda:
        print("El DNI no se encuentra en la agenda.")
        return
    print("Deje en blanco los campos que no desea modificar.")
    apellido = input(f"Ingrese el nuevo apellido (actual: {agenda[dni]['Apellido']}): ")
    nombre = input(f"Ingrese el nuevo nombre (actual: {agenda[dni]['Nombre']}): ")
    email = input(f"Ingrese el nuevo email (actual: {agenda[dni]['Email']}): ")
    telefono = input(f"Ingrese el nuevo número de teléfono (actual: {agenda[dni]['Teléfono']}): ")
    if apellido:
        agenda[dni]['Apellido'] = apellido
    if nombre:
        agenda[dni]['Nombre'] = nombre
    if email:
        agenda[dni]['Email'] = email
    if telefono:
        agenda[dni]['Teléfono'] = telefono
    print("Persona modificada correctamente.")

def eliminar_persona(agenda):
    dni = input("Ingrese el DNI de la persona a eliminar: ")
    if dni in agenda:
        del agenda[dni]
        print("Persona eliminada correctamente.")
    else:
        print("El DNI no se encuentra en la agenda.")

def mostrar_todos(agenda):
    if not agenda:
        print("La agenda está vacía.")
        return
    for dni, datos in agenda.items():
        print(f"DNI: {dni}")
        for key, value in datos.items():
            print(f"{key}: {value}")
        print("-" * 20)

def main():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_persona(agenda)
        elif opcion == "2":
            modificar_persona(agenda)
        elif opcion == "3":
            eliminar_persona(agenda)
        elif opcion == "4":
            mostrar_todos(agenda)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()