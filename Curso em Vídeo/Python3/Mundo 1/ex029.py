# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

cores = {
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxa': '\033[35m',
    'cinza': '\033[36m',
    'vermelho': '\033[31m',
    'verde': '\033[32m'
    }

velocidade = float(input("Qual a velocidade atual o carro?"))
if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80 km/h")
    multa = (velocidade - 80) * 7
    print("{}Você deve pagar uma multa de R${:.2f} ".format(cores['vermelho'], multa))
print("{}Tenha um bom dia! Dirija com segurança".format(cores['verde']))
