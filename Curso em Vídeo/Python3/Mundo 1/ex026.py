# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()

letraA = frase.count('A')
primeiraLetraA = frase.find('A') + 1
ultmimaLetraA = frase.rfind('A') + 1

print('A letra A aparece {} vezes na frase'.format(letraA))
print('A primeira letra A apareceu na posição {}'.format(primeiraLetraA))
print('A última letra A apareceu na posição {}'.format(ultmimaLetraA))
