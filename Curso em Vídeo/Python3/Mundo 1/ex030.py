# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

cores = {
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxa': '\033[35m',
    'cinza': '\033[36m',
    'vermelho': '\033[31m',
    'verde': '\033[32m'
    }

num = int(input("{}Entre com um número qualquer: ".format(cores['roxa'])))

resultado = num % 2

if resultado == 0:
    print("{}O número {} é par".format(cores['azul'], num))
else:
    print("{}O numero {} é impar".format(cores['vermelho'], num))
