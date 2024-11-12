from class_persona import Persona
from class_departamento import  DEpartamento
from class_empleado import Empleado
from class_area import Area
from class_director import director
from class_gerente import gerente
from class_jefe_area import  jefedeArea

def main():
    persona = Persona()
    persona.set_nombre("juan")
    persona.set_apellido("perez")
    persona.set_edad(15)

    departamento = DEpartamento()
    departamento.set_codigo_departamento("1234")
    departamento.set_sede("los aña")
    departamento.set_tipo("operacional")

    empleado = Empleado()
    empleado.set_nombre("migel")
    empleado.set_apellido("sus")
    empleado.set_edad(18)
    empleado.set_email("aña2000@gmail.com")
    empleado.set_fecha_contratacion("30/3/2001")
    empleado.set_id_empleado("213123")

    area = Area()
    area.set_tipo("humanidades")
    area.set_vision("Liderar la innovación en nuevos productos")
    area.set_horario("Lunes a Viernes, 9:00 a.m. - 6:00 p.m.")
    area.set_sede("principal")
    area.set_tipo("empleado")

    direc = director()
    direc.set_nombre("sus")
    direc.set_apellido("gonzalez")
    direc.set_edad(18)
    direc.set_sede("principal")
    direc.set_tipo("operacional")
    direc.set_certificado("ingeñero")
    direc.set_habilidades("hablar")
    direc.set_codigo_departamento("v46515")

    Gerente = gerente()
    Gerente.set_nombre("johan")
    Gerente.set_apellido("perez")
    Gerente.set_edad(18)
    Gerente.set_sede("principal")
    Gerente.set_tipo("operacional")
    Gerente.set_objetivos_mensuales("destacar")
    Gerente.set_evaluacion_desempeno("informes")

    JEFEDEAREA = jefedeArea()
    JEFEDEAREA.set_nombre("pablo")
    JEFEDEAREA.set_sede("principal")
    JEFEDEAREA.set_tipo("de humanidades ")
    JEFEDEAREA.set_area_especifica("recursos humanos")
    JEFEDEAREA.set_normativas("sus")
    JEFEDEAREA.set_codigo_departamento("v46515")


    print("persona")
    print(persona.mostrar_informacion())

    print("departamento")
    print(departamento.mostrar_informacion())

    print("empleado")
    print(empleado.mostrar_informacion())

    print("area")
    print(area.mostrar_informacion())

    print("director")
    print(direc.mostrar_informacion())

    print("Gerente")
    print(Gerente.mostrar_informacion())

    print("JEFEDEAREA")
    print(JEFEDEAREA.mostrar_informacion())

if __name__ == "__main__":
    main()