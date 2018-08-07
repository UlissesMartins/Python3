# Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números inteiros e devolve um número inteiro correspondente à soma dos elementos desta lista.
#
# Sua solução deve ser implementada utilizando recursão.
def soma_lista(lista):
    if (len(lista) == 1):
        return lista[0]
    else:
        n = lista[1:]
        soma = lista[0] + soma_lista(n)

    return soma