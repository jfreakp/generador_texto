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
    
    def nucleos(orden_array, mim_orden, max_orden):
        texto = ''
        for c in range(1,31):
            linea = ''
            for n in range(1,random.randint(1,4)):
                for i in range(mim_orden, max_orden):
                    if i in orden_array:
                        match i:
                            case 1:
                                linea+=str(c)
                            case 2:
                                linea+= ObtenerDatos.generar_cedula_cr()
                            case 3:
                                linea+= '4024'
                            case 4:
                                linea+= str(random.choice(listas.parentesco)["value"])
                            case 5:
                                linea+= '4026'
                            case 6:
                                linea+= 'A'
                            case 7:
                                linea+= str(random.choice(listas.tipoDeudor)["value"])
                            case 8:
                                linea+= str(random.choice(["S", "N"]))
                            case 9:
                                linea+= str(random.choice([i for i in range(1000, 4000, 100)]))
                            case 10:
                                linea+= str(random.choice([i for i in range(100, 400, 100)]))
                            case 11:
                                linea+= str(random.choice(["S", "N"]))
                        linea+='|'
                    else:
                        linea+='|'
                if c != 100:
                    linea+='\n'
                texto+=linea
        return texto
    
    def lotes(orden_array, mim_orden, max_orden):
        texto = ''
        
        for c in range(1,100):
            linea = ''
            area = random.choice([i for i in range(200, 2000, 50)])
            costo = 102
            costo2 = 90
            valor_tasado = area * costo
            valor_venta = area * costo2

            for i in range(mim_orden, max_orden):
                if i in orden_array:
                    match i:
                        case 1:
                            linea+= str(c)
                        case 2:
                            linea+= '1'
                        case 3:
                            linea+= '4022'
                        case 4:
                            linea+= 'A'
                        case 5:
                            linea+= str(random.randint(1,10))
                        case 6:
                            linea+= str(random.randint(1,10))
                        case 7:
                            linea+= str(random.randint(1,10))
                        case 8:
                            linea+= str(random.randint(1,10))
                        case 9:
                            linea+= '1'
                        case 10:
                            linea+= '1'
                        case 11:
                            linea+= '1'
                        case 12:
                            linea+= fake.address().upper()
                        case 13:
                            linea+= str(random.randint(1,10))
                        case 14:
                            linea+= str(area)
                        case 15:
                            linea+= str(costo)
                        case 16:
                            linea+= str(valor_tasado)
                        case 17:
                            linea+= str(valor_venta)
                        case 18:
                            linea+= str(random.randint(1,10))
                        case 19:
                            linea+= str(random.choice(["S", "N"]))
                        case 20:
                            linea+= str(random.choice(["S", "N"]))
                    linea+='|'
                else:
                    linea+='|'
            if c != 99:
                linea+='\n'
            texto+=linea
        return texto
    
    def lotes(orden_array, mim_orden, max_orden):
        texto = ''
        
        for c in range(1,100):
            linea = ''
            area = random.choice([i for i in range(200, 2000, 50)])
            costo = 500
            costo2 = 550
            valor_tasado = area * costo
            valor_venta = area * costo2

            for i in range(mim_orden, max_orden):
                if i in orden_array:
                    match i:
                        case 1:
                            linea+= str(c)
                        case 2:
                            linea+= '1'
                        case 3:
                            linea+= '4019'
                        case 4:
                            linea+= 'A'
                        case 5:
                            linea+= str(area)
                        case 6:
                            linea+= str(costo)
                        case 7:
                            linea+= str(valor_tasado)
                        case 8:
                            linea+= str(valor_venta)
                        case 9:
                            linea+= ''
                        case 10:
                            linea+= '2005'
                        case 11:
                            linea+= str(random.choice(listas.tipoProfesional)["value"])
                        case 12:
                            linea+= ObtenerDatos.generar_cedula_cr
                    linea+='|'
                else:
                    linea+='|'
            if c != 99:
                linea+='\n'
            texto+=linea
        return texto
    

    def piezas(orden_array, mim_orden, max_orden):
        texto = ''
        for c in range(1,100):
            linea = ''
            for n in range(1,9):
                if n in [2,6,8,9]:
                    numero_piezas = 1
                else:
                    numero_piezas = random.randint(1,3)
                for i in range(mim_orden, max_orden):
                    if i in orden_array:
                        match i:
                            case 1:
                                linea+=str(c)
                            case 2:
                                linea+= '1'
                            case 3:
                                linea+= '4005'
                            case 4:
                                linea+= n
                            case 5:
                                linea+= numero_piezas
                        linea+='|'
                    else:
                        linea+='|'
                if c != 100:
                    linea+='\n'
                texto+=linea
        return texto
    
    def acabados(orden_array, mim_orden, max_orden):
        texto = ''
        for c in range(1,100):
            linea = ''
            for n in range(1,9):
                if n in [2,6,8,9]:
                    numero_piezas = 1
                else:
                    numero_piezas = random.randint(1,3)
                for i in range(mim_orden, max_orden):
                    if i in orden_array:
                        match i:
                            case 1:
                                linea+=str(c)
                            case 2:
                                linea+= '1'
                            case 3:
                                linea+= '4006'
                            case 4:
                                linea+= '4'
                            case 5:
                                linea+= '4007'
                            case 6:
                                linea+= '5'
                        linea+='|'
                    else:
                        linea+='|'
                if c != 100:
                    linea+='\n'
                texto+=linea
        return texto
    
    def aportes(orden_array, mim_orden, max_orden):
        texto = ''
        for c in range(1,100):
            linea = ''
            for n in range(1,9):
                if n in [2,6,8,9]:
                    numero_piezas = 1
                else:
                    numero_piezas = random.randint(1,3)
                for i in range(mim_orden, max_orden):
                    if i in orden_array:
                        match i:
                            case 1:
                                linea+=str(c)
                            case 2:
                                linea+= '4023'
                            case 3:
                                linea+= str(random.choice(listas.tipoAporte)["value"])
                            case 4:
                                linea+= str(random.choice([i for i in range(1000, 10000, 1000)]))
                        linea+='|'
                    else:
                        linea+='|'
                if c != 100:
                    linea+='\n'
                texto+=linea
        return texto
    
    def gastos(orden_array, mim_orden, max_orden):
        texto = ''
        for c in range(1,100):
            linea = ''
            for n in range(1,9):
                if n in [2,6,8,9]:
                    numero_piezas = 1
                else:
                    numero_piezas = random.randint(1,3)
                for i in range(mim_orden, max_orden):
                    if i in orden_array:
                        match i:
                            case 1:
                                linea+=str(c)
                            case 2:
                                linea+= str(random.choice(listas.tipoGasto)["value"])
                            case 3:
                                linea+= str(random.choice([i for i in range(1000, 10000, 10)]))
                            case 4:
                                linea+= str(random.choice(["S", "N"]))
                        linea+='|'
                    else:
                        linea+='|'
                if c != 100:
                    linea+='\n'
                texto+=linea
        return texto