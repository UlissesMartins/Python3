#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
# de três e que se encontram no intervalo de 1 até 500
c = 0
cont = 0
for soma in range(1, 501, 2):
    if soma % 3 == 0:
        cont += 1
        c += soma
print('A soma de todos os {} valores solicitados é {}'.format(cont, c))