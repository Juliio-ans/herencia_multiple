from class_persona import  Persona
from class_departamento import  DEpartamento

class director(Persona,DEpartamento):
    def __init__(self):
        Persona.__init__(self)
        DEpartamento.__init__(self)
        self._habilidades = ""
        self._certificado = ""

    def get_habilidades(self):
        return self._habilidades
    def set_habilidades(self, habilidades):
        self._habilidades = habilidades
    def get_certificado(self):
        return self._certificado
    def set_certificado(self, certificado):
        self._certificado = certificado
    def mostrar_informacion(self):
        base_info_persona = Persona.mostrar_informacion(self)
        base_info_DEpartamento = DEpartamento.mostrar_informacion(self)
        return f"{base_info_persona}, habilidades: {self._habilidades}, {base_info_DEpartamento}, certificado: {self._certificado}"


