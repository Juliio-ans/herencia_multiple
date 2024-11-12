class DEpartamento:
    def __init__(self):
        self._sede = ""
        self._codigo_departamento = ""
        self._tipo = ""

    def get_sede(self):
        return self._sede

    def set_sede(self, sede):
        self._sede = sede

    def get_codigo_departamento(self):
        return self._codigo_departamento

    def set_codigo_departamento(self, codigo_departamento):
        self._codigo_departamento = codigo_departamento

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def mostrar_informacion(self):
        return f" la sede es {self._sede}, codigo de departamento {self._codigo_departamento}, tipo de departamento {self._tipo}"