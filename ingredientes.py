
# * my_pizza v1 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1/LICENSE)
#                                                           
#

import os
import sys
from validador import validate
op_sys = 'cls' if sys.platform == 'win32' else 'clear'

i_tomate = 1000
i_champignon = 1000
i_aceituna = 1000
i_cebolla = 1000
i_pollo = 1000
i_jamon = 1000
i_carne = 1000
i_tocino = 1000
i_queso = 1000

def ingrediente(t_s):
    total = t_s
    pedido = []
    while True:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Tenemos los siguientes Ingredientes disponibles.")
        print()
        print(f"  1 - Tomates - $ {i_tomate}")
        print(f"  2 - Champiñones - $ {i_champignon}")
        print(f"  3 - Aceitunas - $ {i_aceituna}")
        print(f"  4 - Aros de cebolla - $ {i_cebolla}")
        print(f"  5 - Pollo - $ {i_pollo}")
        print(f"  6 - Jamon - $ {i_jamon}")
        print(f"  7 - Carne - $ {i_carne}")
        print(f"  8 - Tocino - $ {i_tocino}")
        print(f"  9 - Queso extra - $ {i_queso}")
        print(f" 10 - No añadir nada extra y pagar.")

        ingredientes = int(input("\nSi desea algun ingrediente extra por favor elija una alternativa [1/2/3/4/5/6/7/8/9/10]"))
        valido = validate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ingredientes)
        os.system(op_sys)
        match valido:
            case 1:
                print(f"Ingrediente adicional: Tomates.\nExtra a pagar {i_tomate}")
                total += i_tomate
                print(f"Total a pagar: $ {total}")
                pedido.append(f"1 - Tomates - $ {i_tomate}")
            case 2:
                print(f"Ingrediente adicional: Champiñones.\nExtra a pagar {i_champignon}")
                total += i_champignon
                print(f"Total a pagar: $ {total}")
                pedido.append(f"2 - Champiñones - $ {i_champignon}")
            case 3:
                print(f"Ingrediente adicional: Aceitunas.\nExtra a pagar {i_aceituna}")
                total += i_aceituna
                print(f"Total a pagar: $ {total}")
                pedido.append(f"2 - Aceitunas - $ {i_aceituna}")
            case 4:
                print(f"Ingrediente adicional: Aros de cebolla.\nExtra a pagar {i_cebolla}")
                total += i_cebolla
                print(f"Total a pagar: $ {total}")
                pedido.append(f"4 - Aros de cebolla - $ {i_cebolla}")
            case 5:
                print(f"Ingrediente adicional: Pollo.\nExtra a pagar {i_pollo}")
                total += i_pollo
                print(f"Total a pagar: $ {total}")
                pedido.append(f"5 - Pollo - $ {i_pollo}")
            case 6:
                print(f"Ingrediente adicional: Jamon.\nExtra a pagar {i_jamon}")
                total += i_jamon
                print(f"Total a pagar: $ {total}")
                pedido.append(f"6 - Jamon - $ {i_jamon}")
            case 7:
                print(f"Ingrediente adicional: Carne.\nExtra a pagar {i_carne}")
                total += i_carne
                print(f"Total a pagar: $ {total}")
                pedido.append(f"7 - Carne - $ {i_carne}")
            case 8:
                print(f"Ingrediente adicional: Tocino.\nExtra a pagar {i_tocino}")
                total += i_tocino
                print(f"Total a pagar: $ {total}")
                pedido.append(f"8 - Tocino - $ {i_tocino}")
            case 9:
                print(f"Ingrediente adicional: Queso extra.\nExtra a pagar {i_queso}")
                total += i_queso
                print(f"Total a pagar: $ {total}")
                pedido.append(f"9 - Queso extra - $ {i_queso}")
            case 10:
                break
            case _:
                print(f"Por favor elija una alternativa [1/2/3/4]")    
    return total, pedido