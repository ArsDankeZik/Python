# -*- coding: utf-8 -*-

"""
3. Pedir dos números y decir si uno es múltiplo del otro.
"""

nr1 = int(input("Introduzca el primer número entero: "))
nr2 = int(input("Introduzca el segundo número entero: "))

if nr1 % nr2 == 0:
    print (nr1, "es múltiplo de", nr2)
else:
    print (nr1, "no es múltiplo de", nr2)
print("Espero que vuelva pronto")
