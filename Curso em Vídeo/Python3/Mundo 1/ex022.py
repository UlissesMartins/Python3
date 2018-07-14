""" Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome. """

name = str(input('Digite seu nome completo: ')).strip()

nameUpper = name.upper()
nameMin = name.lower()
nameLen = len(name) - name.count(' ')
nameFirst = name.split()[0]
nameFirstLen = len(nameFirst)

print('Analisando seu nome...')
print('Seu nome em maiúsculoas é {}.'.format(nameUpper))
print('Seu nome em minúsculas é {}.'.format(nameMin))
print('Seu nome tem ao todo {} letras.'.format(nameLen))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nameFirst, nameFirstLen))
