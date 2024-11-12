from class_persona import  Persona
from class_departamento import  DEpartamento

class gerente(Persona,DEpartamento):
    def __init__(self):
        Persona.__init__(self)
        DEpartamento.__init__(self)
        self._objetivos_mensuales = ""
        self._evaluacion_desempeno = ""

    def get_objetivos_mensuales(self):
        return self._objetivos_mensuales

    def set_objetivos_mensuales(self, objetivos_mensuales):
        self._objetivos_mensuales = objetivos_mensuales

    def get_evaluacion_desempeno(self):
        return self._evaluacion_desempeno

    def set_evaluacion_desempeno(self, evaluacion_desempeno):
        self._evaluacion_desempeno = evaluacion_desempeno

    def mostrar_informacion(self):
        base_info_persona = Persona.mostrar_informacion(self)
        base_info_DEpartamento = DEpartamento.mostrar_informacion(self)
        return f"{base_info_persona},objetivo mensual: {self._objetivos_mensuales}, {base_info_DEpartamento}, evaluacion desempeno: {self._evaluacion_desempeno}"
