import pickle
from Empleado import Empleado
from EmpleadoPer import EmpleadoPermanente
from EmpleadoTem import EmpleadoTemporal

class GestionEmpleados:
    def __init__(self):
        self.empleados = []
        self.cargar_datos()

    def agregar_empleado(self):
        tipo_empleado = input("Ingrese el tipo de empleado (permanente/temporal): ").lower()
        nombre = input("Ingrese el nombre del empleado: ")
        while True:
            try:
                edad = int(input("Ingrese la edad del empleado (mayor o igual a 16): "))
                if edad < 16:
                    raise ValueError("La edad debe ser mayor o igual a 16.")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                salario = float(input("Ingrese el salario del empleado: "))
                if salario < 0:
                    raise ValueError("El salario no puede ser negativo.")
                break
            except ValueError as e:
                print(e)
        area = input("Ingrese el área de trabajo del empleado: ")

        if tipo_empleado == 'permanente':
            beneficios = input("Ingrese los beneficios del empleado permanente: ")
            empleado = EmpleadoPermanente(nombre, edad, salario, area, beneficios)
        elif tipo_empleado == 'temporal':
            fecha_fin_contrato = input("Ingrese la fecha de fin de contrato del empleado temporal: ")
            empleado = EmpleadoTemporal(nombre, edad, salario, area, fecha_fin_contrato)
        else:
            print("Tipo de empleado no válido. Se creará un empleado genérico.")
            empleado = Empleado(nombre, edad, salario, area)

        self.empleados.append(empleado)
        self.guardar_datos()
        print("Empleado agregado correctamente.")

    def mostrar_empleados(self):
        if not self.empleados:
            print("No hay empleados para mostrar.")
        else:
            print("\nLista de empleados:")
            for idx, empleado in enumerate(self.empleados):
                print(f"{idx + 1}. {empleado}")

    def buscar_empleado(self, nombre):
        for empleado in self.empleados:
            if empleado.nombre == nombre:
                print(f"Empleado encontrado - {empleado}")
                return empleado
        print(f"No se encontró ningún empleado con el nombre '{nombre}'")
        return None

    def editar_empleado(self):
        nombre_buscar = input("Ingrese el nombre del empleado que desea editar: ")
        empleado = self.buscar_empleado(nombre_buscar)

        if empleado:
            opcion = input("¿Qué desea editar? (nombre/edad/salario/area): ").lower()

            if opcion == 'nombre':
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                empleado.nombre = nuevo_nombre
            elif opcion == 'edad':
                while True:
                    try:
                        nueva_edad = int(input("Ingrese la nueva edad (mayor o igual a 16): "))
                        empleado.edad = nueva_edad
                        break
                    except ValueError as e:
                        print(e)
            elif opcion == 'salario':
                while True:
                    try:
                        nuevo_salario = float(input("Ingrese el nuevo salario: "))
                        empleado.salario = nuevo_salario
                        break
                    except ValueError as e:
                        print(e)
            elif opcion == 'area':
                nueva_area = input("Ingrese la nueva área de trabajo: ")
                empleado.area = nueva_area
            else:
                print("Opción no válida.")
            self.guardar_datos()
        else:
            print(f"No se encontró ningún empleado con el nombre '{nombre_buscar}'")

    def guardar_datos(self):
        with open('empleados.dat', 'wb') as file:
            pickle.dump(self.empleados, file)
        print("Datos guardados correctamente.")

    def cargar_datos(self):
        try:
            with open('empleados.dat', 'rb') as file:
                self.empleados = pickle.load(file)
            print("Datos cargados correctamente.")
        except FileNotFoundError:
            print("No se encontraron datos previos. Se creará un nuevo archivo al guardar.")
