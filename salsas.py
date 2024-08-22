# * my_pizza v1 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1/LICENSE)
#                                                           
#

import os
import sys




s_tomate = 1250
s_alfredo = 850
s_barbecue = 500
s_pesto = 1000

def salsa(t_m):
    total = t_m
    pedido = []
    while True:

        print(f" 1 - Salsa de tomate - $ {s_tomate}")
        print(f" 2 - Salsa Alfredo - $ {s_alfredo}")
        print(f" 3 - Salsa Barbecue - $ {s_barbecue}")
        print(f" 4 - Salsa Pesto - $ {s_pesto}")

        tipo = int(input("Si desea algun tipo de salsa por favor elija una alternativa [1/2/3/4]"))

        match tipo:
            case 1:
                print(f"Ha elegido salsa de tomate.\nExtra a pagar {s_tomate}")
                total += s_tomate
                print(f"Total a pagar: $ {total}")
                print()
                pedido.append(f" 1 - Salsa de tomate - $ {s_tomate}")
                break
            case 2:
                print(f"Ha elegido salsa Alfredo.\nExtra a pagar {s_alfredo}")
                total += s_alfredo
                print(f"Total a pagar: $ {total}")
                pedido.append(f" 2 - Salsa Alfredo - $ {s_alfredo}")
                break
            case 3:
                print(f"Ha elegido la salsa Barbecue.\nExtra a pagar {s_barbecue}")
                total += s_barbecue
                print(f"Total a pagar: $ {total}")
                pedido.append(f"3 - Salsa Barbecue - $ {s_barbecue}")     
                break
            case 4:
                print(f"Ha elegido la salsa Pesto.\nExtra a pagar {s_pesto}")
                total += s_pesto
                print(f"Total a pagar: $ {total}")
                pedido.append(f"4 - Salsa Pesto - $ {s_pesto}")     
                break                
            case _:
                print(f"Por favor elija una alternativa [1/2/3/4]")
    #print(f"Salsas:::salsa::total= {total}")
    return total, pedido                