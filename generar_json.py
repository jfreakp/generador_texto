import json
import os

def generar_profesionales_json(profesionales):
    data = {
        "profesionales": profesionales
    }

    # Crear el directorio si no existe
    os.makedirs("json", exist_ok=True)

    # Crear archivo JSON
    with open("json/profesionales.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Archivo JSON creado exitosamente.")
    
def obtener_profesionales_by_filtro(ruta_archivo, te_profesional):
    try:
        # Abrir y leer el archivo JSON
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        # Filtrar los profesionales por te_profesional
        profesionales = data.get("profesionales", [])
        filtrados = [
            profesional for profesional in profesionales
            if profesional.get("te_profesional") == te_profesional
        ]
        
        return filtrados
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no se encontró.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el archivo JSON: {e}")
        return None