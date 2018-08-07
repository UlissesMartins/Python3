'''Exercício 1: Lista ordenada
Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro e devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada.'''

def ordenada(lista):
    atual = lista[0]
    for i in range(len(lista)):
        if atual > lista[i]:
            return False
        atual = lista[i]
    return True
