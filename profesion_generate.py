import random
import faker

# Generador de datos ficticios
fake = faker.Faker('es')  # Generar datos en español para Costa Rica

# Diccionario para los tipos de profesionales
profesion_dict = {
    "A": "ANALISTA",
    "ARQ": "ARQUITECTO",
    "C": "CONSTRUCTOR",
    "CO": "CONTADOR",
    "D": "DESARROLLADOR",
    "I": "INGENIERO",
    "R": "RESPONSABLE CIVIL"
}

# Función para generar un número de carnet ficticio
def generar_carnet():
    return str(random.randint(1000000000, 9999999999))

# Crear el archivo y escribir los datos
with open("profesionales_cr.txt", "w", encoding="utf-8") as file:
    for _ in range(100):
        # Selección aleatoria de tipo de profesional
        tipo_profesional = random.choice(list(profesion_dict.keys()))
        # Nombre aleatorio del profesional
        nombre_profesional = fake.name().upper()
        # Número de carnet
        carnet = generar_carnet()
        
        # Formato de salida: tipo|carnet|nombre
        file.write(f"|{tipo_profesional}|{carnet}|{nombre_profesional}|\n")

print("Archivo 'profesionales_cr.txt' generado exitosamente.")
