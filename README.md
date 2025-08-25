# Parcial 1 Programación Avanzada
## Programa 4: Calculadora Financiera de Ahorros
###Integrantes:
Javier Huertas - 1505825\
Pedro Monroy - 1505625\
Fabritzio López - 1507525\
Jorge Rivera - 1511425
# **Contenido:**
### --------------------------1. Descripción del programa--------------------------
**Descripción:**
Este programa funciona como una calculadora de metas de ahorro\
y proyecciones a corto, mediano y largo plazo mediante un plan de ahorro.\
Ej: El usuario puede definir su meta y como va a llegar a esa meta, mediante\
pagos mensuales, quincenales o anuales en su cuenta de ahorro, además de poder ver\
el resumen y progreso.
### --------------------------------2. Instrucciones de uso-------------------------------
# Para la opción 1(Definir meta y plan de ahorro)
El usuario debe ingresar el nombre de la meta (Ej.: Carro).\
Luego mostrará en pantalla el tiempo (años o meses) y el usuario debe elegir en que rango de tiempo quiere ahorrar.\
Luego el programa le preguntará la cantidad de años o meses que desea ahorrar el usuario.\
El programa mostrara que el usuario ingrese la cantidad de dinero que desea ahorrar.\
El programa imprime mensaje plan de ahorro.\
El programa imprime la frecuencia (semanal, quincenal y mensual), el usuario debe elegir una de esas 3(Ej.:Mensual),\
si el usuario ingresa un número mayor a 3, el programa manda error y reinicia la opción.\
El programa imprime el interés, el cual el usuario debe ingresar un número mayor a 0.01 y 7%\
El programa muestra el mensaje "Ingrese el tipo de tasa de interés:"
El usuario define si quiere un interés simple o compuesto
luego de que el usuario defina sus objetivos, se agregan a la lista **"Cuentas"**

# ------------Para la opción 2 (Depositar):------------
Si el usuario no ha agregado ninguna cuenta, muestra el mensaje "No hay cuentas registradas"
si no, el programa pide un número de cuenta y de ahi que el usuario defina cuanto dinero quiere depositar.\
El programa muestra mensajes de error por si el usuario se equivoca al ingresar los datos necesarios.

# ----Para la opción 3 (Ver resumen de metas y planes)----
Esta opción es para mostrar las metas y planes que previamente ha ingresado el usuario\
Ej:'meta': Goal("Carro", "mes", 1, 150000)\
'plan': SavingPlan("mensual", 200, 0, 0.5, 'compuesto')

# ------------Para la opcion 4 (Salir)------------
El programa rompe el ciclo while y termina el proceso.


# Final