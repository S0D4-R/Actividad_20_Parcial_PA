"""
Implicados:
    ~ Jorge
    ~ Javier
    ~ Fabritzio
    ~ Pedro
dawg
"""


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

