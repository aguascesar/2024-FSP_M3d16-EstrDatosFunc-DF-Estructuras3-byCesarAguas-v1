# * my_pizza v1 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1/LICENSE)
#                                                           
#
import os
import sys
from masas import masa
from salsas import salsa
from ingredientes import ingrediente
from pagos import pago
from validador import validate


op_sys = 'cls' if sys.platform == 'win32' else 'clear'

os.system(op_sys)
#         En consola se necesita un titulo alucivo.
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|                    JAT Pizza                       |")
print("|                                                    |")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("                     Bienvenido                      ")
print()
#   Declaracion de variables del programa

comprar = input('''Hola, desea hacer su pedido ahora? [s/n]
        
    S. Si quiero mi pizza ahora.
    N. Salir
        
> ''')

#   Variables necesarias
total = 0
msas = []
ssas = []
ingr = []
pedido = []

#   Definiendo funciones necesarias
#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   Las funciones han sido escritas en los 
#modulos adyacentes, son invocadas mediante la orden:
#   funcion()
#   funcion(argumento)
#   funcion(argumento1, argumento2)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

os.system(op_sys)

valido = validate(['s', 'n'], comprar)
#   Iniciamos las rutinas
if valido == "s":
    #   Seleccionamos un tipo de masa
    t_m, p_m = masa()
    total += t_m
    msas.append(p_m)
    #print(f"masa reporto:::{total}")
    #   Tambien debemos seleccionar la salsa
    t_s, p_s = salsa(total)
    total = t_s
    ssas.append(p_s)
    #print(f"salsa reporto:::{total}")
    #   Tambien podemos seleccionar algunos extras
    t_i, p_i = ingrediente(total)
    total = t_i
    ingr.append(p_i)
    #print(f"ingrediente reporto:::{total}")
    pago(total, msas, ssas, ingr)

else:
    print("No se hace nada, y termina la aplicacion.")