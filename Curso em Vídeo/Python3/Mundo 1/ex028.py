# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

cores = {
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxa': '\033[35m',
    'cinza': '\033[36m',
    'vermelho': '\033[31m',
    'verde': '\033[32m'
    }


computador = randint(0, 5)  # Faz o computador "Pensar"
print("{}=-=".format(cores['amarelo']) * 20)
print("{}Vou pensar em um número entre 0 e 5. Tente descobrir...".format(cores['vermelho']))
print("{}=-=".format(cores['amarelo']) * 20)
jogador = int(input("Em que número eu pensei? "))# Jogador tenta advinhar
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("{}PARABÉNS!!! Você acertou o número que pensei".format(cores['verde']))
else:
    print("{}ERROU!!! O número que pensei foi {} e não no {}!" .format(cores['vermelho'], computador, jogador))
