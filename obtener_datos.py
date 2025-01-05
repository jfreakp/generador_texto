import listas
import random
import faker
import datos

from datetime import datetime
# Obtener la fecha actual
fecha_actual = datetime.now()

# Formatear la fecha en formato dd/mm/yyyy
formato_fecha = fecha_actual.strftime('%d/%m/%Y')

fake = faker.Faker('es')

class ObtenerDatos:
    def generar_cedula_cr():
        """
        Genera un número de cédula costarricense con el formato X-XXXX-XXXX
        """
        tipo = fake.random_int(min=1, max=9)  # El primer dígito es el tipo de persona
        bloque1 = fake.random_int(min=1000, max=9999)  # Primer bloque de 4 dígitos
        bloque2 = fake.random_int(min=1000, max=9999)  # Segundo bloque de 4 dígitos
        return f"{tipo}-{bloque1}-{bloque2}"

    def personas(orden_array, mim_orden, max_orden):
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

    def profesionales(orden_array, mim_orden, max_orden):
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
                            linea+= ObtenerDatos.generar_cedula_cr()
                    linea+='|'
                else:
                    linea+='|'
            if c != datos.clientes[-1]:
                linea+='\n'
            texto+=linea
        return texto
    
    def estados(orden_array, mim_orden, max_orden):
        texto = ''
        for c in range(1,100):
            linea = ''
            for i in range(mim_orden, max_orden):
                if i in orden_array:
                    match i:
                        case 1:
                            linea+= str(c)
                        case 4:
                            linea+= 'RL'
                        case 5:
                            linea+= formato_fecha
                    linea+='|'
                else:
                    linea+='|'
            if c != 99:
                linea+='\n'
            texto+=linea
        return texto
    
    def operaciones(orden_array, mim_orden, max_orden):
        texto = ''
        for c in range(1,100):
            P = random.choice([i for i in range(1000, 150000, 1000)])  # Monto del préstamo
            tasa_anual = (random.randint(4, 18))/100 #0.12  # Tasa anual en porcentaje (12%)
            n = random.choice([i for i in range(12, 61, 6)])  # Plazo en meses

            # Cálculo de la tasa mensual
            r = tasa_anual / 12 
            cuota = round(P * r * (1 + r)**n / ((1 + r)**n - 1), 4)
            linea = ''
            for i in range(mim_orden, max_orden):
                if i in orden_array:
                    match i:
                        case 1:
                            linea+= str(c)
                        case 3:
                            linea+= random.choice(listas.tipoPeriodicidad)["value"]
                        case 4:
                            linea+= '4020'
                        case 5:
                            linea+= random.choice(listas.tipoCuota)["value"]
                        case 6:
                            linea+= str(P)
                        case 7:
                            linea+= str(tasa_anual)
                        case 8:
                            linea+= str(n)
                        case 9:
                            linea+= str(P)
                        case 10:
                            linea+= str(n)
                        case 11:
                            linea+= '1000'
                        case 12:
                            linea+= str(cuota)
                        case 13:
                            linea+= str(cuota)
                        case 14:
                            linea+= str(P)
                        case 15:
                            linea+= str(0)
                        case 16:
                            linea+= str(P)
                        case 17:
                            linea+= str(0)
                        case 18:
                            linea+= str(500)    
                        case 19:
                            linea+= str(0)   
                        case 20:
                            linea+=''   
                        case 21:
                            linea+=''   
                        case 22:
                            linea+='' 
                        case 23:
                            linea+= str(P)
                        case 24:
                            linea+= str(P)
                    linea+='|'
                else:
                    linea+='|'
            if c != 99:
                linea+='\n'
            texto+=linea
        return texto