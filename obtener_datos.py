import listas
import random
import faker
import datos
from generar_json import generar_profesionales_json, obtener_profesionales_by_filtro

from datetime import datetime, timedelta
# Obtener la fecha actual
fecha_actual = datetime.now()

# Formatear la fecha en formato dd/mm/yyyy
formato_fecha = fecha_actual.strftime('%d/%m/%Y')

fake = faker.Faker('es')

def fecha_aleatoria():
    # Definir las fechas de inicio y fin
    inicio = datetime(2000, 1, 1)
    fin = datetime(2024, 12, 31)

    # Generar un número aleatorio de días entre las fechas
    delta_dias = (fin - inicio).days
    dias_aleatorios = random.randint(0, delta_dias)

    # Calcular la fecha aleatoria
    fecha = inicio + timedelta(days=dias_aleatorios)

    # Formatear la fecha como DDMMYYYY
    return fecha.strftime('%d%m%Y')

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
                            linea+= str(random.choice(listas.nivelEducativo)["value"])
                        case 7:
                            linea+= str(random.choice(listas.sexo)["value"])
                        case 9:
                            linea+= str(random.choice(listas.estadoCivil)["value"])
                        case 12:
                            linea+= c['NOMBRE']
                        case 13:
                            linea+= 'NINGUNA'
                        case 14:
                            linea+= '1'
                        case 15:
                            linea+= c['FECHA_NACIMIENTO']
                        case 16:
                            linea+= str(c['CODIGO_CLIENTE'])
                    linea+='|'
                else:
                    linea+='|'
            if c != datos.clientes[-1]:
                linea+='\n'
            texto+=linea
        return texto

    def profesionales(orden_array, mim_orden, max_orden):
        profesionales = []
        
        
        texto = ''
        for c in range(1,100):
            linea = ''
            profesional = {}
            for i in range(mim_orden, max_orden):
                if i in orden_array:
                    match i:
                        case 2:
                            te_profesional = random.choice(listas.tipoProfesional)["value"] 
                            linea+= te_profesional 
                            profesional["te_profesional"] = te_profesional     
                        case 3:
                            id_profesional = ObtenerDatos.generar_cedula_cr().replace('-','')
                            linea+= id_profesional
                            profesional["id_profesional"] = id_profesional
                        case 4:
                            nombre = fake.name().upper()
                            linea+= nombre 
                            profesional["nom_profesional"] = nombre
                    linea+='|'
                else:
                    linea+='|'
                
            if c != datos.clientes[-1]:
                linea+='\n'
            texto+=linea
            profesionales.append(profesional)
        generar_profesionales_json(profesionales)
        return texto
    
    def estados(orden_array, mim_orden, max_orden):
        texto = ''
        cont=0
        for c in datos.clientes:
            cont+=1
            linea = ''
            for i in range(mim_orden, max_orden):
                if i in orden_array:
                    match i:
                        case 1:
                            linea+= str(cont)
                        case 4:
                            linea+= 'RL'
                        case 5:
                            linea+= formato_fecha
                    linea+='|'
                else:
                    linea+='|'
            if c != datos.clientes[-1]:
                linea+='\n'
            texto+=linea
        return texto
    
    def operaciones(orden_array, mim_orden, max_orden):
        texto = ''
        for c in range(1,len(datos.clientes)):
            P = random.choice([i for i in range(1000, 150000, 1000)])  # Monto del préstamo
            tasa_anual = (random.randint(4, 18))/100 #0.12  # Tasa anual en porcentaje (12%)
            tasa = tasa_anual*100
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
                            linea+= str(tasa)
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
            if c !=len(datos.clientes)-1:
                linea+='\n'
            texto+=linea
        return texto
    
    def nucleos(orden_array, mim_orden, max_orden):
        texto = ''
        cont = 0
        cont2 = 1
        for n in range(1,len(datos.clientes)):
                linea = ''
                cont +=1
                if n%4 == 0:
                    cont2+=1
                for i in range(mim_orden, max_orden):
                    if i in orden_array:
                        match i:
                            case 1:
                                linea+=str(cont2)
                            case 2:
                                linea+= datos.clientes[cont]['IDENTIFICACION']
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
                texto+=linea+'\n'            
        return texto
    
    def lotes(orden_array, mim_orden, max_orden):
        texto = ''
        
        for c in range(1,len(datos.clientes)):
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
                            linea+= fake.address().upper().replace('\n','')
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
    
    def construccion(orden_array, mim_orden, max_orden):
        texto = ''
        
        for c in range(1,len(datos.clientes)):
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
                            linea+= ObtenerDatos.generar_cedula_cr().replace('-','')
                    linea+='|'
                else:
                    linea+='|'
            if c != 99:
                linea+='\n'
            texto+=linea
        return texto
    

    def piezas(orden_array, mim_orden, max_orden):
        texto = ''
        for c in range(1,len(datos.clientes)):
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
        for c in range(1,len(datos.clientes)):
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
        for c in range(1,len(datos.clientes)):
            linea = ''
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
        for c in range(1,len(datos.clientes)):
            linea = ''       
            for i in range(mim_orden, max_orden):
                valores = random.sample(range(500, 10000), 50)
                valor = str(random.choice(valores))
                if i in orden_array:
                    match i:
                        case 1:
                            linea+=str(c)
                        case 3:
                            linea+= str(random.choice(listas.tipoGasto)["value"])
                        case 4:
                            linea+=valor
                        case 5:
                            linea+= str(random.choice(["S", "N"]))
                    linea+='|'
                else:
                    linea+='|'
            if c != 100:
                linea+='\n'
            texto+=linea
        return texto
    
    def casos(orden_array, mim_orden, max_orden):
        texto = ''
        cont = 0
        for  c in datos.clientes:
            linea = ''
            cont+=1
            # Ruta del archivo
            ruta = "json/profesionales.json"
            ingeniero = random.choice(obtener_profesionales_by_filtro(ruta, 'I'))
            contador = random.choice(obtener_profesionales_by_filtro(ruta, 'CO'))
            analista = random.choice(obtener_profesionales_by_filtro(ruta, 'A'))
            for i in range(mim_orden, max_orden):
                if i in orden_array:
                    match i:
                        case 1:
                            linea+=str(cont)
                        case 2:
                            linea+='1'
                        case 4:
                            linea+=str(random.choice(listas.prioridad)["value"])
                        case 6:
                            linea+=str(random.choice(listas.solicitud)["value"])
                        case 8:
                            linea+=str(random.choice(listas.proposito)["value"])
                        case 10:
                            linea+=str(random.choice(listas.postulacion)["value"])
                        case 12:
                            linea+=str(random.choice(listas.programa)["value"])
                        case 16:
                            linea+=str(random.choice(listas.garantia)["value"])
                        case 17:
                            linea+='1'
                        case 18:
                            linea+='1'
                        case 19:
                            linea+='1'
                        case 20:
                            linea+=str(cont)
                        case 21:
                            linea+=c['IDENTIFICACION']
                        case 22:
                            linea+=str(random.choice([i for i in range(400, 2000, 100)]))
                        case 24:
                            linea+=str(random.choice([i for i in range(400, 1000, 100)]))
                        case 25:
                            linea+=str(random.choice(listas.tipoAprobacion)["value"])
                        case 26:
                            linea+=str(random.choice([i for i in range(0, 400, 1)])/100)
                        case 28:
                            linea+= ingeniero['te_profesional']
                        case 29:
                            linea+='30'
                        case 30:
                            linea+= ingeniero['id_profesional']#ObtenerDatos.generar_cedula_cr().replace('-','')
                        case 32:
                            linea+= contador['te_profesional']
                        case 33:
                            linea+= contador['id_profesional']#ObtenerDatos.generar_cedula_cr().replace('-','')
                        case 35:
                            linea+= analista['te_profesional']
                        case 36:
                            linea+= analista['id_profesional']#ObtenerDatos.generar_cedula_cr().replace('-','')
                        case 39:
                            linea+=''
                        case 41:
                            linea+= fecha_aleatoria()
                        case 42:
                            linea+= fecha_aleatoria()
                        case 43:
                            linea+= fecha_aleatoria()
                        case 44:
                            linea+= fecha_aleatoria()
                        case 45:
                            linea+= fecha_aleatoria()
                        case 48:
                            linea+= fake.address().replace('\n','')
                        case 50:
                            linea+= '3'
                        case 51:
                            linea+= str(random.choice([i for i in range(1, 3, 1)]))
                        case 52:
                            linea+= str(random.choice([i for i in range(500, 1000, 10)]))   
                        case 53:
                            linea+= ''     
                        case 62:
                            linea+= ''  
                        case 63:
                            linea+= ''                   
                    linea+='|'
                else:
                    linea+='|'
            if c != datos.clientes[-1]:
                linea+='\n'
            texto+=linea
        return texto