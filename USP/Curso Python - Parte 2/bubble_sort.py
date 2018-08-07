'''Exercício 2: Ordenação com bubble sort
Implemente a função bubble_sort(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo bubble sort.

Além de devolver uma lista ordenada, ao longo do processamento sua função deve imprimir o estado atual da lista toda vez que fizer uma alteração em seus elementos.'''

def bubble_sort(lista):
    for num in range(len(lista)-1, 0, -1):
        for i in range(num):
            if lista[i] >lista[i+1]:
                muda = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = muda
                print(lista)
    return lista
