# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informa a temperatura em °C: '))

f = 9 * c / 5 + 32

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(c, f))
