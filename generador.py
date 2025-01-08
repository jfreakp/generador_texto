import datos
from obtener_datos import ObtenerDatos

tablas = ['SP_PERSONAS_BFV', 'SP_PROFESIONALES_BFV', 'SP_ESTADOS_BFV','SP_OPERACIONES_BFV', 'SP_NUCLEO_BFV', 'SP_LOTE_BFV', 'SP_CONSTRUCCION_BFV', 'SP_APORTES_BFV', 'SP_GASTOS_BFV','SP_CASOS_BFV']

def generar_all(num_tabla):
    nombre_tabla = tablas[num_tabla]

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

        case 'SP_LOTE_BFV':
            with open("archivos/Lotes.txt", "w", encoding="utf-8") as file:
                file.write(ObtenerDatos.lotes(orden_array,mim_orden, max_orden))

        case 'SP_CONSTRUCCION_BFV':
            with open("archivos/Construccion.txt", "w", encoding="utf-8") as file:
                file.write(ObtenerDatos.construccion(orden_array,mim_orden, max_orden))

        case 'SP_APORTES_BFV':
            with open("archivos/Aportes.txt", "w", encoding="utf-8") as file:
                file.write(ObtenerDatos.aportes(orden_array,mim_orden, max_orden))

        case 'SP_GASTOS_BFV':
            with open("archivos/Gastos.txt", "w", encoding="utf-8") as file:
                file.write(ObtenerDatos.gastos(orden_array,mim_orden, max_orden))

        case 'SP_CASOS_BFV':
            with open("archivos/Casos.txt", "w", encoding="utf-8") as file:
                file.write(ObtenerDatos.casos(orden_array,mim_orden, max_orden))

for i in range(1,len(tablas)):
    generar_all(i)

