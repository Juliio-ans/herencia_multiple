from class_persona import  Persona
from class_departamento import  DEpartamento

class jefedeArea(Persona,DEpartamento):
    def __init__(self):
        Persona.__init__(self)
        DEpartamento.__init__(self)
        self.area_especifica = ""
        self.normativas = ""
        self.recursos_asignados = ""

    def get_area_especifica(self):
        return self.area_especifica

    def set_area_especifica(self, area_especifica):
        self.area_especifica = area_especifica

    def get_normativas(self):
        return self.normativas
    def set_normativas(self, normativas):
        self.normativas = normativas

    def get_recursos_asignados(self):
        return self.recursos_asignados
    def set_recursos_asignados(self, recursos_asignados):
        self.recursos_asignados = recursos_asignados

    def mostrar_informacion(self):
        base_info_persona = Persona.mostrar_informacion(self)
        base_info_DEpartamento = DEpartamento.mostrar_informacion(self)
        return f"{base_info_persona},area especifica :{self.area_especifica}, {base_info_DEpartamento}, normativas :{self.normativas}, recursos asignados :{self.recursos_asignados}"
