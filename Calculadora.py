"""
Implicados:
    ~ Jorge
    ~ Javier
    ~ Fabritzio
    ~ Pedro
#Esqueleto
"""

#Clase meta---------------------------------------------------------------------------------------
class Goal:
    def __init__(self, name, unit, time, final_inv):
        self.name = name
        self.unit = unit
        self.time = time
        self.money = final_inv

    #mostrar_meta
    def show_goal(self):
        return f"|Nombre: {self.name} |Tiempo: {self.time} {self.unit} |Dinero por acumular: Q{self.money} |"


#Clase PlanAhorro------------------------------------------------------------------------------------
class SavingPlan:
    def __init__(self, frecuencia, cantidad_por_deposito, saldo_total, interes, interes_type):
        self.frecuencia = frecuencia
        self.cantidad_por_deposito = cantidad_por_deposito
        self.depositos_realizados = []
        self.saldo_total = saldo_total
        self.interest = interes
        self.interest_type = interes_type
    #Mostrar el avance del plan de ahorro
    def show_saving_plan(self):
        return f"|Periodo: {self.frecuencia} |Dinero Total: Q{self.saldo_total} |Tasa de interés: Q{self.interest*100:.2f} | Cantidad recomendada por deposito: Q{self.cantidad_por_deposito:.2f} |"

    #depositar
    def deposit(self,money_amount):
        self.depositos_realizados.append(money_amount)
        self.saldo_total += money_amount

    #total_acumulado (incluye intereses)
    def total_accumulated(self, unidad, tiempo):
        n = 0
        if unidad == 'años':
            if self.frecuencia == "semanal":
                n = tiempo * 52
            elif self.frecuencia == "quincenal":
                n = tiempo * 24
            elif self.frecuencia == "mensual":
                n = tiempo * 12
        elif unidad == 'meses':
            if self.frecuencia == "semanal":
                n = tiempo * 4
            elif self.frecuencia == "quincenal":
                n = tiempo * 2
            elif self.frecuencia == "mensual":
                n = tiempo

        if self.interest_type == "simple":
            return self.saldo_total + (self.saldo_total * self.interest * n)
        elif self.interest_type == "compound":
            return self.saldo_total * (1 + self.interest) ** n
        else:
            return self.saldo_total
    #evaluar_progreso
    """
    final_investment es un atributo de la clase "Goals" entonces para hacer el cálculo
    se necesita pasar ese atributo como parámetro.
    Además devolví un string, pero podemos también devolver progress_percentage por si es necesario para
    otro cálculo.
    """
    def progress_test(self, unidad, tiempo, final_investment):
        progress_percentage = ((self.total_accumulated(unidad, tiempo))/final_investment)*100
        if final_investment == 0:
            return "0%"
        return f"{progress_percentage}%"

def acc_busqueda():
    if cuentas:
        for i, metas in enumerate(cuentas, start=1):
            print(f'Meta y plan No. {i}\n'
            f"METAS:\n {metas['meta'].show_goal()}\n"
            f"PLAN DE AHORRO:\n {metas['plan'].show_saving_plan()}\n{metas['plan'].progress_test(metas['meta'].unit, metas['meta'].time, metas['meta'].money)}")
    else:
        print('No hay metas y planes registrados.\n')


def ingreso_num(mensaje, tipo='int'):
    while True:
        try:
            numero = float(input(f'{mensaje}'))
            if tipo == 'int':
                return int(numero)
            elif tipo == 'float':
                return round(numero, 2)
        except ValueError:
            print('Debe ser un número.\n')

def monto_por_deposito(unidad, tiempo,frecuencia,cantidad):
    total_depositos = 0
    if unidad == "años":
        if frecuencia == "semanal":
            total_depositos = tiempo * 52
        elif frecuencia == "quincenal":
            total_depositos = tiempo * 24
        elif frecuencia == "mensual":
            total_depositos = tiempo * 12
    elif unidad == "meses":
        if frecuencia == "semanal":
            total_depositos = tiempo * 4
        elif frecuencia == "quincenal":
            total_depositos = tiempo * 2
        elif frecuencia == "mensual":
            total_depositos = tiempo

    return cantidad / total_depositos


#Menu----------------------------------------------------------------------------------------------------
cuentas = []

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
                #Meta
                print('META:\n')
                while True:
                    nombre = input('Ingrese el nombre de la meta: ')
                    if not nombre:
                        print("El nombre no puede quedar vacio")
                    else:
                        break
                unidades = ['años', 'meses']
                print('\nUnidades: \n1. Años \n2. Meses')
                while True:
                    unidad = ingreso_num('Ingrese la unidad de tiempo en la que va a ahorrar: ')
                    if unidad == 1 or unidad == 2:
                        unidad = unidades[unidad-1]
                        break
                    else:
                        print('Número fuera de rango.\n')
                while True:
                    tiempo = ingreso_num(f'Ingrese la cantidad de {unidad} en los que desea ahorrar: ')
                    if tiempo <=0:
                        print("El tiempo debe ser mayor a 0")
                    else:
                        break
                while True:
                    cantidad = ingreso_num('Ingrese la cantidad de dinero que desea ahorrar: ', 'float')
                    if cantidad <=0:
                        print("La cantidad debe ser mayor a 0")
                    else:
                        break
                goal = Goal(nombre, unidad, tiempo, cantidad)

                #Plan de ahorro
                print('\nPLAN DE AHORRO:\n')
                frecuencias = ['semanal', 'quincenal', 'mensual']
                print('Frecuencia: \n 1. Semanal \n 2. Quincenal \n 3. Mensual')
                while True:
                    frecuencia = ingreso_num('Ingrese la frecuencia en la que va a ingresar dinero: ')
                    if 1 <= frecuencia <= 3:
                        frecuencia = frecuencias[frecuencia-1]
                        break
                    else:
                        print('Número fuera de rango.\n')

                monto_por_dep = monto_por_deposito(unidad, tiempo,frecuencia, cantidad)

                print('IMPORTANTE: Las tasas de interés van de 0.1% hasta 7%.')
                while True:
                    t_interes = ingreso_num('Ingrese la tasa de interés: ',"float")
                    if 0.1 <= t_interes <= 7:
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
                        print('Número fuera de rango.\n')

                plan = SavingPlan(frecuencia, monto_por_dep,0, t_interes, tipo) # Saldo total = 0, al ser saldo inicial.

                cuenta = {'meta': goal, 'plan': plan}
                cuentas.append(cuenta)

            case "2":
                if not cuentas:
                    print("No hay cuentas registradas...")
                else:
                    if not cuentas:
                        print("No hay cuentas registradas...")
                    else:
                        acc_busqueda()
                        try:
                            searched_id = int(input("Coloque el número de cuenta: "))
                            if 1 <= searched_id <= len(cuentas):
                                amount_to_deposit = ingreso_num("Coloque la cantidad que depositará: ", "float")
                                if amount_to_deposit > 0:
                                    cuentas[searched_id - 1]['plan'].deposit(amount_to_deposit)
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
                print("Gracias por usar el programa")
                key = False
            case _:
                print('Opción inválida. Intente nuevamente.\n')

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

