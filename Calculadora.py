"""
Implicados:
    ~ Jorge
    ~ Javier
    ~ Fabritzio
    ~ Pedro
dawg
"""
#Clase meta---------------------------------------------------------------------------------------
class Goal:
    def __init__(self, name, time, initial_inv):
        self.name = name
        self.time = time
        self.money = initial_inv

    #mostrar_meta
    def show_goal(self):
        return f"|Nombre: {self.name}|Tiempo: {self.time}|Dinero: {self.money}|"
    #porcentaje_avance
    def porcentage_process(self):
        pass

#Clase PlanAhorro------------------------------------------------------------------------------------
class SavingPlans:
    def __init__(self, periodo, cantidad_periodo, depositos_realizados, suma_depositos, interes, interes_type):
        self.periodo = periodo
        self.cantidad_periodo = cantidad_periodo
        self.deposito_realizado = depositos_realizados
        self.suma_d = suma_depositos
        self.interest = interes
        self.interest_type = interes_type

    #depositar
    def deposit(self):
        pass
    #total_acumulado (incluye intereses)
    def total_acumulated(self):
        pass
    #calcula_interés_simple
    def simple_interest_calculus(self):
        pass
    #calcula_interés_compuesto
    def compund_interest_calculus(self):
        pass
    #evaluar_progreso
    def progress_test(self):
        pass


#Menu----------------------------------------------------------------------------------------------------
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
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                print("Gracias por usar el programa")
                key = False

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

