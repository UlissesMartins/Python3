# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Qual é seu nome completo? ')).strip()

nameContains = 'SILVA' in name.upper()

print('Seu nome tem silva? {}'.format(nameContains))
