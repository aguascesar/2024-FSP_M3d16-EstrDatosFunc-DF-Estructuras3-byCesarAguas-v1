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

#         En consola se necesita un titulo alucivo.
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|                    JAT Pizza                       |")
print("|                                                    |")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("                     Bienvenido                      ")
print()
#   Declaracion de variables del programa
comprar = input("Hola, desea hacer su pedido ahora\n [s/n]")

#   Variables necesarias
total = 0
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


#   Iniciamos las rutinas
if comprar == "s":
    #   Seleccionamos un tipo de masa
    t_m, p_m = masa()
    total += t_m
    pedido.append(p_m)
    #print(f"masa reporto:::{total}")
    #   Tambien debemos seleccionar la salsa
    t_s, p_s = salsa(total)
    total = t_s
    pedido.append(p_s)
    #print(f"salsa reporto:::{total}")
    #   Tambien podemos seleccionar algunos extras
    t_i, p_i = ingrediente(total)
    total = t_i
    pedido.append(p_i)
    #print(f"ingrediente reporto:::{total}")
    pago(total, pedido)

else:
    print("No se hace nada, y termina la aplicacion.")