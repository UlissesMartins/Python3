# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
valor = input('Digite algo: ')

typeValue = type(valor)
print('O tipo primitivo desse valor é {}'.format(typeValue))

space = valor.isspace()
print('Só tem espaços? {}'.format(space))

number = valor.isnumeric()
print('É um numero? {}'.format(number))

alfa = valor.isalpha()
print('E alfabético? {}'.format(alfa))

maiusculo = valor.isupper()
print('Esta em maiúsculas? {}'.format(maiusculo))

min = valor.islower()
print('Esta em minúscalas? {}'.format(min))

capi = valor.isprintable()
print('Esta capitalizada? {}'.format(capi))
