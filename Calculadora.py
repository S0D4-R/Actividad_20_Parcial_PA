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
    def __init__(self, name, time, final_inv):
        self.name = name
        self.time = time
        self.money = final_inv

    #mostrar_meta
    def show_goal(self):
        return f"|Nombre: {self.name}|Tiempo: {self.time}|Dinero: {self.money}|"
    #porcentaje_avance
    def percentage_process(self):
        pass

#Clase PlanAhorro------------------------------------------------------------------------------------
class SavingPlan:
    def __init__(self, account_number, periodo, cantidad_periodo, deposito_realizado, suma_depositos, interes, interes_type):
        self.periodo = periodo
        self.cantidad_periodo = cantidad_periodo
        self.deposito_realizado = deposito_realizado
        self.suma_d = suma_depositos
        self.interest = interes
        self.interest_type = interes_type

    #depositar
    def deposit(self):
        pass
    #total_acumulado (incluye intereses)
    def total_accumulated(self):
        pass
    #calcula_interés_simple
    def simple_interest_calculus(self):
        pass
    #calcula_interés_compuesto
    def compound_interest_calculus(self):
        pass
    #evaluar_progreso
    """
    final_investment es un atributo de la clase "Goals" entonces para hacer el cálculo
    se necesita pasar ese atributo como parámetro.
    Además devolví un string, pero podemos también devolver progress_percentage por si es necesario para
    otro cálculo.
    """
    def progress_test(self, final_investment):
        progress_percentage = ((self.suma_d + self.interest)/final_investment)*100
        string_percentage = f"{progress_percentage}%"
        return string_percentage

#
#Menu----------------------------------------------------------------------------------------------------
goals = {}
save_plan =  {}

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
                if not save_plan:
                    print("No hay cuentas registradas...")
                else:
                    searched_id = input("Coloque el número de cuenta: ")
                    if searched_id in save_plan:
                        save_plan[searched_id].deposit()
            case "3":
                pass
            case "4":
                print("Gracias por usar el programa")
                key = False
            case _:
                print('Opción inválida. Intente nuevamente.\n')

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

