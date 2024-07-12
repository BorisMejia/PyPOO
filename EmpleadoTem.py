from Empleado import Empleado

class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, edad, salario, area, fecha_fin_contrato):
        super().__init__(nombre, edad, salario, area)
        self._fecha_fin_contrato = fecha_fin_contrato

    @property
    def fecha_fin_contrato(self):
        return self._fecha_fin_contrato

    @fecha_fin_contrato.setter
    def fecha_fin_contrato(self, value):
        self._fecha_fin_contrato = value

    def __str__(self):
        return f"[Temporal] " + super().__str__() + f", Fecha fin de contrato: {self.fecha_fin_contrato}"
