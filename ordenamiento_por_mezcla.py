import random

def ordenamiento_de_mezcla(lista):
    if len(lista) > 1: 
        medio = len(lista) //2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        #llamada recursiva en cada mitad


if __name__ == '__main__':
    tamano_lista = int(input('de que tamano es la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    print('')

    lista_ordenada = ordenamiento_de_mezcla(lista)
    print(lista_ordenada)