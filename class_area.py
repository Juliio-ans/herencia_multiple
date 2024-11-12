from  class_departamento  import DEpartamento

class Area(DEpartamento):
    def __init__(self):
        super().__init__()
        self._estrategia = ""
        self._horario = ""
        self._vision = ""

    def get_estrategia(self):
        return self._estrategia

    def set_estrategia(self, estrategia):
        self._estrategia = estrategia

    def get_horario(self):
        return self._horario

    def set_horario(self, horario):
        self._horario = horario

    def get_vision(self):
        return self.vision

    def set_vision(self, vision):
        self.vision = vision

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info},la estrategia es: {self._estrategia}, horarios: {self._horario}, vision :{self.vision}"