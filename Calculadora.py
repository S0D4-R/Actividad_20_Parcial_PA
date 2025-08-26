"""
Implicados:
    ~ Jorge
    ~ Javier
    ~ Fabritzio
    ~ Pedro
#Esqueleto
"""

#Clase meta---------------------------------------------------------------------------------------
class Goal: #----------------------Primera clase----------------------
    def __init__(self, name, unit, time, final_inv):
        self.name = name #-----------Para mostrar el titular-----------
        self.unit = unit #-----------Para mostrar la unidad de tiempo (AÑOS//MESES)-----------
        self.time = time #-----------Para mostrar el tiempo-----------
        self.money = final_inv #-----------Para mostrar el dinero que queremos ahorrar-----------

    def show_goal(self): #-----------Mostrar meta-----------
        return f"|Nombre: {self.name} |Tiempo: {self.time} {self.unit} |Dinero por acumular: Q{self.money} |" #-----------RETORNA LA META

#---------------------------------SEGUNDA CLASE----------------------
class SavingPlan:
    def __init__(self, frecuencia, depositos_esperados, cantidad_por_deposito, saldo_total, interes, interes_type):
        self.frecuencia = frecuencia #-----------Para mostrar la frecuencia de depositos-----------
        self.depositos_esperados = depositos_esperados #-----------Cuantos depositos se van a realizar-----------
        self.cantidad_por_deposito = cantidad_por_deposito #-----------Cuanto dinero se hará por depósito-----------
        self.depositos_realizados = [] #-----------LISTA-----------
        self.saldo_total = saldo_total #-----------Para mostrar la cantidad de dinero que se lleva en el plan de ahorro-----------
        self.interest = interes #-----------INTERÉS A MOSTRAR-----------
        self.interest_type = interes_type #-----------El tipo de interes disponibles (SIMPLE//COMPUESTO)-----------

    def show_saving_plan(self): #-----------Mostrar nuestro progreso del plan de ahorro-----------.
        return f"|Periodo: {self.frecuencia.capitalize()} |Dinero Total: Q{self.saldo_total} |Tasa de interés: {self.interest*100:.2f}% | Cantidad recomendada por deposito: Q{self.cantidad_por_deposito:.2f} |"
        #Retorna nuestro progreso en nuestro plan de ahorro

    def deposit(self,money_amount, meta): #-----------opción 2 (DEPOSITAR)-----------
        self.depositos_realizados.append(money_amount)
        self.saldo_total += money_amount

        if meta.unit == "meses":
            dep_por_periodo = {"semanal": 4, "quincenal": 2, "mensual": 1}[self.frecuencia]
        elif meta.unit == "años":
            dep_por_periodo = {"semanal": 52, "quincenal": 24, "mensual": 12}[self.frecuencia]
        if len(self.depositos_realizados) % dep_por_periodo == 0:
            self.apply_interest()
        #Agrega en "money_amount" a saldo_total (Ej.: tenemos Q300 y agregamos Q100, nuestro saldo total sería Q400
        #Los intereses se aplican anual o mensualmente dependiendo de la unidad de tiempo elegida por el usuario.

    def apply_interest(self):#-------aplicar interés (simple y compuesto)--------
        if self.interest_type == "simple":
            interes_ganado = sum(self.depositos_realizados) * self.interest
            self.saldo_total = sum(self.depositos_realizados) + interes_ganado
        elif self.interest_type == "compuesto":
            self.saldo_total = self.saldo_total * (1 + self.interest)

    def progress_test(self, final_investment): #------------evaluar_progreso-------------
        progress_percentage = (self.saldo_total/final_investment)*100
        if final_investment == 0:
            progress_percentage = 0
        return f"|Progreso: {progress_percentage:.2f}% |Depositos: {len(self.depositos_realizados)}/{self.depositos_esperados} |"

def acc_busqueda(): #-----------Opción 3(Mostrar metas y planes de ahorro)-----------
    if cuentas:
        for i, metas in enumerate(cuentas, start= 1):
            meta = metas['meta']
            plan = metas['plan']
            print(f'Cuenta No. {i}\n'
            f"META:\n {meta.show_goal()}\n" #EJEMPLO: |Nombre: viaje a Madrid| |Tiempo: 2 Años| |Dinero por acumular: Q100,000|
            f"PLAN DE AHORRO:\n {plan.show_saving_plan()}\n" #EJEMPLO: |Periodo: Años| |Dinero total: Q40,987| |Tasa de interes: 0.2%| |Cantidad recomendada por depósito: Q2,083.33 x mes|
            f'PROGRESO:\n {plan.progress_test(meta.money)}\n\n') #EJEMPLO: |Progreso: 40.98%| |Depositos: 20 Depositos|
    else:
        print('No hay metas y planes registrados.\n')

def ingreso_num(mensaje, tipo='int'): #Esto es para verificar el numero que el usuario agrega, y si no agrega ningun numero
    #El programa lanza el mensaje de error.
    while True:
        try:
            numero = float(input(f'{mensaje}'))
            if tipo == 'int':
                return int(numero)
            elif tipo == 'float':
                return round(numero, 2)
        except ValueError:
            print('Debe ser un número.\n')

def total_depositos(unidad, tiempo,frecuencia): #Esta funcion es para mostrar el total dependiendo la frecuencia que elija el usuario
    total = 0
    if unidad == "años":
        if frecuencia == "semanal":
            total = tiempo * 52
        elif frecuencia == "quincenal":
            total = tiempo * 24
        elif frecuencia == "mensual":
            total = tiempo * 12
    elif unidad == "meses":
        if frecuencia == "semanal":
            total = tiempo * 4
        elif frecuencia == "quincenal":
            total = tiempo * 2
        elif frecuencia == "mensual":
            total = tiempo
    return total
#---------------------------------PROGRAMA FUNCIONAL---------------------------------
cuentas = [] #Lista para agregar las cuentas que el usuario agregue
key = True
while key:
    try:
        operations = input("----------MENU----------\n\n"
                           "1. Crear Meta y Plan de Ahorro\n"
                           "2. Hacer un Depósito\n"
                           "3. Ver Resumen de Metas y Planes\n"
                           "4. Salir\n\n"
                           "Opción: ")
        match operations:
            case "1":
                print("-"*15 + "NUEVA META Y PLAN DE AHORRO"+ "-"*15)
                print('META:\n')
                while True:
                    nombre = input('Ingrese el nombre de la meta: ') #EJEMPLO: Carro, Viaje, PC, Guitarra, etc
                    if not nombre:
                        print("El nombre no puede quedar vacio")
                    else:
                        break
                unidades = ['años', 'meses']
                print('\nUnidades: \n1. Años \n2. Meses')
                while True:
                    unidad = ingreso_num('Ingrese la unidad de tiempo en la que va a ahorrar: ') #1 = Años----- 2 = Meses
                    if unidad == 1 or unidad == 2:
                        unidad = unidades[unidad-1]
                        break
                    else:
                        print('Número fuera de rango.\n') #SI EL USUARIO PONE 3 o "tres" o "dos"
                while True:
                    tiempo = ingreso_num(f'Ingrese la cantidad de {unidad} en los que desea ahorrar: ') #EJEMPLO: 4 años//5 meses
                    if tiempo <=0:
                        print("El tiempo debe ser mayor a 0") #ERROR SI EL USUARIO PONE (EJ.-3)
                    else:
                        break
                while True:
                    cantidad = ingreso_num('Ingrese la cantidad de dinero que desea ahorrar: ', 'float')
                    if cantidad <=0:
                        print("La cantidad debe ser mayor a 0")
                    else:
                        break
                goal = Goal(nombre, unidad, tiempo, cantidad)
                print('\nPLAN DE AHORRO:\n')
                frecuencias = ['semanal', 'quincenal', 'mensual']
                print('Frecuencia: \n 1. Semanal \n 2. Quincenal \n 3. Mensual')
                while True:
                    frecuencia = ingreso_num('Ingrese la frecuencia en la que va a ingresar dinero: ') #EJEMPLO== semanal
                    if 1 <= frecuencia <= 3:
                        frecuencia = frecuencias[frecuencia-1]
                        break
                    else:
                        print('Número fuera de rango.\n') #ERROR

                depositos_esp = total_depositos(unidad, tiempo, frecuencia)

                monto_por_dep = cantidad / depositos_esp

                print('IMPORTANTE: Las tasas de interés van de 0.1% hasta 3%.')
                while True:
                    t_interes = ingreso_num('Ingrese la tasa de interés: ',"float")
                    if 0.1 <= t_interes <= 3:
                        t_interes = t_interes / 100
                        break
                    else:
                        print('La tasa de interés debe estar dentro del rango establecido.\n')

                tipos_tasas = ['simple', 'compuesto']
                print('Tipos de interés: \n1. Simple \n2. Compuesto')
                while True:
                    tipo = ingreso_num('Ingrese el tipo de tasa de interés: ')
                    if tipo == 1 or tipo == 2:
                        tipo = tipos_tasas[tipo-1]
                        break
                    else:
                        print('Número fuera de rango.\n') #ERROR

                plan = SavingPlan(frecuencia, depositos_esp, monto_por_dep,0, t_interes, tipo) # Saldo total = 0, al ser saldo inicial.

                cuenta = {'meta': goal, 'plan': plan}
                cuentas.append(cuenta)

            case "2":
                if not cuentas:
                    print("No hay cuentas registradas...")
                else:
                    print("-"*10+ "HACER UN DEPOSITO"+ "-"*10)
                    acc_busqueda()
                    try:
                        searched_id = int(input("Coloque el número de cuenta: "))
                        if 1 <= searched_id <= len(cuentas):
                            amount_to_deposit = ingreso_num("Coloque la cantidad que depositará: ", "float")
                            if amount_to_deposit > 0:
                                cuentas[searched_id - 1]['plan'].deposit(amount_to_deposit, cuentas[searched_id - 1]['meta'])
                                print(
                                    f"!Deposito exitoso! Saldo total: Q{cuentas[searched_id - 1]["plan"].saldo_total}")
                            else:
                                print("El monto debe ser mayor a 0.")
                        else:
                            print("Número de cuenta inválido")
                    except ValueError:
                        print("Debe ingresar un número válido.")
            case "3":
                print("-"*15 + "RESUMEN METAS Y PLANES"+ "-"*15)
                acc_busqueda()
            case "4":
                print("-"*10 + "Gracias por usar el programa"+ "-"*10)
                key = False
            case _:
                print('Opción inválida. Intente nuevamente.\n')

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")