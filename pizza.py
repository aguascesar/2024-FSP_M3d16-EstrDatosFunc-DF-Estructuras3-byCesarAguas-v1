# * my_pizza v1 (https://github.com/aguascesar/2024-FSP_M3d14-EstrDatosFunc-DF-Estructuras2-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d14-EstrDatosFunc-DF-Estructuras2-byCesarAguas-v1/LICENSE)
#  
#

#Proyecto parcial, aun no esta terminado, necesito entender la parte de modularizacion.

#Por favor se ruega tener paciencia, gracias.

#pip install tqdm

from time import sleep
from tqdm import tqdm


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

#   Otras variables necesarias
total = 0
pedido = []

m_tradicional = 7850
m_delgada = 9650
m_borde_queso = 8950

s_tomate = 1250
s_alfredo = 850
s_barbecue = 500
s_pesto = 1000

i_tomate = 1000
i_champignon = 1000
i_aceituna = 1000
i_cebolla = 1000
i_pollo = 1000
i_jamon = 1000
i_carne = 1000
i_tocino = 1000
i_queso = 1000



#   Iniciamos las rutinas
if comprar == "s":
    #   Seleccionamos un tipo de masa
    while True:

        print(f"1 - Masa tradicional - $ {m_tradicional}")
        print(f"2 - Masa delgada - $ {m_delgada}")
        print(f"3 - Masa con bordes de queso - $ {m_borde_queso}")

        masa = int(input("Hola, por favor, seleccione el tipo de masa: [1/2/3]\n"))

        match masa:
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

    #   Tambien debemos seleccionar la salsa
    while True:

        print(f" 1 - Salsa de tomate - $ {s_tomate}")
        print(f" 2 - Salsa Alfredo - $ {s_alfredo}")
        print(f" 3 - Salsa Barbecue - $ {s_barbecue}")
        print(f" 4 - Salsa Pesto - $ {s_pesto}")

        salsa = int(input("Si desea algun tipo de salsa por favor elija una alternativa [1/2/3/4]"))

        match salsa:
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

    while True:

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

            ingredientes = int(input("Si desea algun ingrediente extra por favor elija una alternativa [1/2/3/4/5/6/7/8/9/10]"))

            match ingredientes:
                case 1:
                    print(f"Ingrediente adicional: Tomates.\nExtra a pagar {i_tomate}")
                    total += i_tomate
                    print(f"Total a pagar: $ {total}")
                    pedido.append(f"1 - Tomates - $ {i_tomate}")
                case 2:
                    print(f"Ingrediente adicional: Champiñones.\nExtra a pagar {i_champignon}")
                    total += i_champignon
                    print(f"Total a pagar: $ {total}")
                    pedido.append(f"1 - Tomates - $ {i_champignon}")
                case 3:
                    print(f"Ingrediente adicional: Aceitunas.\nExtra a pagar {i_aceituna}")
                    total += i_aceituna
                    print(f"Total a pagar: $ {total}")
                    pedido.append(f"1 - Tomates - $ {i_aceituna}")
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

else:
    print("No se hace nada, y termina la aplicacion.")