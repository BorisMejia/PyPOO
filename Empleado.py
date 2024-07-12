class Empleado:
    def __init__(self, nombre, edad, salario):
        self._nombre = nombre
        self._edad = edad
        self._salario = salario

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if value >= 16:
            self._edad = value
        else:
            raise ValueError("La edad debe ser mayor o igual a 16.")

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        if value >= 0:
            self._salario = value
        else:
            raise ValueError("El salario no puede ser negativo.")

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}"
