# Exercício 2: Encontrando ímpares em uma lista
# Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista de números inteiros e devolve uma outra lista apenas com os números ímpares da lista dada.
#
# Sua solução deve ser implementada utilizando recursão.
def encontra_impares(lista):
    '''extrai números impares da lista de entrada  utilizando recursão '''

    if (len(lista) <= 0):
        return []
    else:

        if (lista[0] % 2 > 0):
            n = [lista[0]]
        else:
            n = []

        return n + encontra_impares(lista[1:])