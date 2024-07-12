from Empleado import Empleado

class EmpleadoPermanente(Empleado):
    def __init__(self, nombre, edad, salario, area, beneficios):
        super().__init__(nombre, edad, salario, area)
        self._beneficios = beneficios

    @property
    def beneficios(self):
        return self._beneficios

    @beneficios.setter
    def beneficios(self, value):
        self._beneficios = value

    def __str__(self):
        return f"[Permanente] " + super().__str__() + f", Beneficios: {self.beneficios}"
