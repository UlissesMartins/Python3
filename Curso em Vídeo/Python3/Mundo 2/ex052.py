# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num = int(input('Entre com um número: '))
primo = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        primo += 1
    else:
        print('\033[35m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'. format(num, primo))
if primo == 2:
    print('O número é primo!')
else:
    print('O número não é primo!')