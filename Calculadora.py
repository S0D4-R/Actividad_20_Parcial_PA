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


#Clase PlanAhorro------------------------------------------------------------------------------------
class SavingPlan:
    def __init__(self, periodo, cantidad_periodo, suma_depositos, interes, interes_type):
        self.periodo = periodo
        self.cantidad_periodo = cantidad_periodo
        self.depositos_realizados = []
        self.suma_d = suma_depositos
        self.interest = interes
        self.interest_type = interes_type
    #Mostrar el avance del plan de ahorro
    def show_saving_plan(self):
        return f"|Periodo: {self.periodo} |suma de deposito: {self.suma_d} |Interes: {self.interest} |"

    #depositar
    def deposit(self,money_amount):
        self.depositos_realizados.append(money_amount)
        self.suma_d += money_amount
    #total_acumulado (incluye intereses)
    def total_accumulated(self,total):
        capital= sum(self.depositos_realizados)
        if self.interest_type == "simple":
            total = capital+ (capital * self.interest * self.periodo)
        elif self.interest_type == "compound":
            total= capital * (1+ self.interest)**self.periodo
        return total
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

def acc_busqueda():
    for i, metas in enumerate(cuentas):
        print(f"Metas: {i}. {metas.show_goal()}\n"
              f"Plan de ahorro: {i}. {metas.show_saving_plan()}\n")
#Menu----------------------------------------------------------------------------------------------------
cuentas = [
    {
        'meta': Goal("Carro", 1, 150000),
        'plan': SavingPlan("mensual", 200, 0, 0.5, 'compuesto')
    }
]

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
                if not cuentas:
                    print("No hay cuentas registradas...")
                else:
                    acc_busqueda()
                    searched_id = input("Coloque el número de cuenta: ")
                    if searched_id in cuentas:
                        cuentas[searched_id]['plan'].deposit()
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

