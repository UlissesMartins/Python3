# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input("Qual a é a distância da sua viagem? "))
print("Você está prestes a iniciar uma viagem de {} km.".format(distancia))
'''if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45'''
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print("E o preço de sua passagem será de R$ {:.2f}".format(preco))