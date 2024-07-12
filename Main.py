from GestionEmpleados import GestionEmpleados

def main():
    gestion = GestionEmpleados()

    while True:
        print("\n        SURA")
        print("1. Agregar empleado")
        print("2. Mostrar empleados")
        print("3. Buscar empleado por nombre")
        print("4. Editar empleado")
        print("5. Salir")
        opcion = input("\nIngrese una opción: ")

        if opcion == '1':
            gestion.agregar_empleado()
        elif opcion == '2':
            gestion.mostrar_empleados()
        elif opcion == '3':
            nombre_buscar = input("Ingrese el nombre del empleado a buscar: ")
            gestion.buscar_empleado(nombre_buscar)
        elif opcion == '4':
            gestion.editar_empleado()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
