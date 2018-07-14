# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

num = float(input('Digite um valor: '))

numInt = trunc(num)

print('Valor digitado foi {} e a sua porção inteira é {}'.format(num, numInt))
