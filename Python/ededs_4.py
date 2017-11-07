# -*- coding: utf-8 -*-

"""
5. Pedir dos números y decir cuál es el mayor o si son iguales.
"""

nr1 = int(input("Introduzca el primer número entero: "))
nr2 = int(input("Introduzca el segundo número entero: "))

if nr1 > nr2:
    print (nr1, "es mayor que", nr2)
elif nr1 == nr2:
    print (nr1, "es igual que", nr2)
print("Espero que vuelva pronto")