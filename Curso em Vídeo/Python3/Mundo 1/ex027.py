# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()

primeiroNome = nome.split()[0]
ultimoNome = nome.rsplit()[-1]

print('Seu primeiro nome é {}'. format(primeiroNome))
print('Seu último nome é {}'.format(ultimoNome))
