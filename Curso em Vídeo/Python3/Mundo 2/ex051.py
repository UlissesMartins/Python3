# Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final mostre os 10 primeiros
# termos dessa progressão.
primeiro_termo = int(input('Entre com primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
    print('{}'.format(c), end = ' → ')
print('ACABOU')