# Refaça o desafio 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for.
c = int(input('Digite um número para ver sua tabuada: '))
for num in range(1, 11):
    print('{} x {:2} = {}'.format(c, num, num*c))