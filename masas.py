# * my_pizza v1 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1/LICENSE)
#                                                           
#
import os
import sys
from validador import validate
op_sys = 'cls' if sys.platform == 'win32' else 'clear'

m_tradicional = 7850
m_delgada = 9650
m_borde_queso = 8950

def masa():
    total = 0
    pedido = []
    while True:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Tenemos las siguientes Masas disponibles.")
        print()
        print(f"1 - Masa tradicional - $ {m_tradicional}")
        print(f"2 - Masa delgada - $ {m_delgada}")
        print(f"3 - Masa con bordes de queso - $ {m_borde_queso}")

        tipo = int(input("\nHola, por favor, seleccione el tipo de masa: [1/2/3]\n"))
        valido = validate([1, 2, 3], tipo)
        os.system(op_sys)
        match valido:
            case 1:
                print(f"Ha elegido la masa tradicional.\nTotal a pagar= $ {m_tradicional}")
                print()
                total += m_tradicional
                pedido.append(f"1 - Masa tradicional - $ {m_tradicional}")
                break
            case 2:
                print(f"Ha elegido la pizza de masa delgada.\nTotal a pagar= $ {m_delgada}")
                total += m_delgada
                pedido.append(f"2 - Masa delgada - $ {m_delgada}")
                break
            case 3:
                print(f"Ha elegido la pizza con bordes de queso.\nTotal a pagar= $ {m_borde_queso}")
                total += m_borde_queso
                pedido.append(f"3 - Masa con bordes de queso - $ {m_borde_queso}")
                break
            case _:
                print(f"Por favor elija una alternativa [1/2/3]")

    return total, pedido