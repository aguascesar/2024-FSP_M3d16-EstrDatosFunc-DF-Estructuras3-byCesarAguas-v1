# * my_pizza v1 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d16-EstrDatosFunc-DF-Estructuras3-byCesarAguas-v1/LICENSE)
#                                                           
#

#pip install tqdm
from time import sleep
from tqdm import tqdm

def pago(total, pedido):

    while True:
        pagar = input("Como desea cancelar su pizza [Efectivo/Debito/Credito/Otro]")
        if pagar != "":
            print("_____") 
            print(" \_&_/ Ticket de compra")
            print(" (n_n) No valido como boleta")
            print("<) )\_")
            print(f" | |   Total Pedido: $ {total}")
            print(f" |_|_  \n")

            print("Su pedido es: ")
            for i in pedido:
                print(f"{i}.")
            for i in tqdm(range(10)):
                sleep(3)
            print("\n ¡Provecho!")
            print()
            print("  \_(n_n)_/")      
            print()

            break
        else:
            print(f"Por favor elija una forma de pagar, adecuada.")

