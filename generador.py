import datos
from obtener_datos import ObtenerDatos

tablas = ['SP_PERSONAS_BFV', 'SP_PROFESIONALES_BFV', 'SP_ESTADOS_BFV','SP_OPERACIONES_BFV', 'SP_NUCLEO_BFV']
nombre_tabla = tablas[4]

filtrados = [tabla for tabla in datos.tablas if tabla["NOMBRE_TABLA"] == nombre_tabla]
tablas_ordenadas = sorted(filtrados, key=lambda x: x["ORDEN"])
mim_orden = 1
max_orden = max(tablas_ordenadas, key=lambda x: x["ORDEN"])["ORDEN"]+1
orden_array = [tabla["ORDEN"] for tabla in tablas_ordenadas]

match nombre_tabla:
    case 'SP_PERSONAS_BFV':
        with open("archivos/Personas.txt", "w", encoding="utf-8") as file:
            file.write(ObtenerDatos.personas(orden_array,mim_orden, max_orden))

    case 'SP_PROFESIONALES_BFV':
        with open("archivos/Profesionales.txt", "w", encoding="utf-8") as file:
            file.write(ObtenerDatos.profesionales(orden_array,mim_orden, max_orden))
            
    case 'SP_ESTADOS_BFV':
        with open("archivos/Estados.txt", "w", encoding="utf-8") as file:
            file.write(ObtenerDatos.estados(orden_array,mim_orden, max_orden))

    case 'SP_OPERACIONES_BFV':
        with open("archivos/Operaciones.txt", "w", encoding="utf-8") as file:
            file.write(ObtenerDatos.operaciones(orden_array,mim_orden, max_orden))
    
    case 'SP_NUCLEO_BFV':
        with open("archivos/Nucleos.txt", "w", encoding="utf-8") as file:
            file.write(ObtenerDatos.nucleos(orden_array,mim_orden, max_orden))