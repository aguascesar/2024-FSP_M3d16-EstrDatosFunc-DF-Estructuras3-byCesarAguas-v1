# * my_pizza v1 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1/LICENSE)
#                                                           
#

#pip install tqdm
from time import sleep
from tqdm import tqdm
import os
import sys
from validador import validate
op_sys = 'cls' if sys.platform == 'win32' else 'clear'

def pago(total, msas, ssas, ingr):

    while True:

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Como desea cancelar su pizza?")
        print()
        print(f"1 - Efectivo ")
        print(f"2 - Debito ")
        print(f"3 - Credito ")
        print(f"4 - Cheque ")

        pagar = int(input("\nElija una de las opciones [1/2/3/4]"))
        valido = validate([1, 2, 3, 4], pagar)
        os.system(op_sys)

        if valido != "":
            print("_____") 
            print(" \_&_/ Ticket de compra")
            print(" (n_n) No valido como boleta")
            print("<) )\_")
            print(f" | |   Total Pedido: $ {total}")
            print(f" |_|_  \n")

            print(f"Su pedido es: ")
            print(f"{msas}")
            print(f"{ssas}")
            for i in ingr:
                print(f"{i}\n")
            print()
            for i in tqdm(range(10)):
                sleep(3)

            os.system(op_sys)
            print("\n ¡Provecho!")
            print()
            print("  \_(n_n)_/")      
            print()

            break
        else:
            print(f"Por favor elija una forma de pagar, adecuada.")

