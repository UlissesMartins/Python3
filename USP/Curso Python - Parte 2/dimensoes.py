# Exercício 1: Tamanho da matriz
# Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.

def dimensoes(minha_matriz):
    for i in range(len(minha_matriz)):
        h = len(minha_matriz)
        for j in minha_matriz[i]:
            k = len(minha_matriz[i])

    print(str(h) + 'X' + str(k))
