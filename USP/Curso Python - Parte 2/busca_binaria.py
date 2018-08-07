'''Exercício 1: Busca binária
Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.

Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve imprimir cada um dos índices testados pelo algoritmo.'''

def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        metade = (primeiro + ultimo) // 2
        print(metade)
        if elemento == lista[metade]:
            return metade
        if elemento < lista[metade]:
            ultimo = metade - 1
        else:
            primeiro = metade + 1
    return False
