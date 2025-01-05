import datos
import listas
import random
import faker

fake = faker.Faker('es')

nombre_tabla = 'SP_PROFESIONALES_BFV'#'SP_PERSONAS_BFV'

filtrados = [tabla for tabla in datos.tablas if tabla["NOMBRE_TABLA"] == nombre_tabla]
tablas_ordenadas = sorted(filtrados, key=lambda x: x["ORDEN"])
mim_orden = 1
max_orden = max(tablas_ordenadas, key=lambda x: x["ORDEN"])["ORDEN"]+1
orden_array = [tabla["ORDEN"] for tabla in tablas_ordenadas]

def generar_cedula_cr():
    """
    Genera un número de cédula costarricense con el formato X-XXXX-XXXX
    """
    tipo = fake.random_int(min=1, max=9)  # El primer dígito es el tipo de persona
    bloque1 = fake.random_int(min=1000, max=9999)  # Primer bloque de 4 dígitos
    bloque2 = fake.random_int(min=1000, max=9999)  # Segundo bloque de 4 dígitos
    return f"{tipo}-{bloque1}-{bloque2}"

def personas(orden_array):
    texto = ''
    for c in datos.clientes:
        linea = ''
        for i in range(mim_orden, max_orden):
            if i in orden_array:
                match i:
                    case 1:
                        linea+=c['IDENTIFICACION']
                    case 3:
                        linea+='CI'
                    case 5:
                        linea+= random.choice(listas.nivelEducativo)["value"]
                    case 7:
                        linea+= random.choice(listas.sexo)["value"]
                    case 9:
                        linea+= random.choice(listas.estadoCivil)["value"]
                    case 12:
                        linea+= c['NOMBRE']
                    case 13:
                        linea+= 'NINGUNA'
                    case 14:
                        linea+= 1
                    case 15:
                        linea+= c['FECHA_NACIMIENTO']
                    case 16:
                        linea+= c['CODIGO_CLIENTE']
                linea+='|'
            else:
                linea+='|'
        if c != datos.clientes[-1]:
            linea+='\n'
        texto+=linea
    return texto

def profesionales(orden_array):
    texto = ''
    for c in range(1,100):
        linea = ''
        for i in range(mim_orden, max_orden):
            if i in orden_array:
                match i:
                    case 2:
                        linea+= random.choice(listas.tipoProfesional)["value"]
                    case 3:
                        linea+= fake.name().upper()
                    case 4:
                        linea+= generar_cedula_cr()
                linea+='|'
            else:
                linea+='|'
        if c != datos.clientes[-1]:
            linea+='\n'
        texto+=linea
    return texto


match nombre_tabla:
    case 'SP_PERSONAS_BFV':
        with open("Personas.txt", "w", encoding="utf-8") as file:
            file.write(personas(orden_array))
    case 'SP_PROFESIONALES_BFV':
        with open("Profesionales.txt", "w", encoding="utf-8") as file:
            file.write(profesionales(orden_array))