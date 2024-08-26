#Funcion reutilizada del desafio fundamentos de python
def validate(opciones, eleccion):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    while eleccion not in opciones:
        print('Por favor ingrese una alternativa:', opciones)
        eleccion = input('Ingrese la alternativa: ').lower()
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    return eleccion