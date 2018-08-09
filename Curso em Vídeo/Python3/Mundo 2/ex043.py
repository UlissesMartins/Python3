'''Exercicio 43 - Índice de Massa Corporal
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''
peso = float(input("Qual é o seu peso? (kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc <= 18.5:
    print("Você está na ABAIXO DO PESO normal")
elif imc <= 25:
    print("PARABÉNS, você está na faixa de PESO IDEAL")
elif imc <= 30:
    print("Você está na faixa de SOPREPESO")
elif imc <= 40:
    print("Você está em OBESIDADE!")
else:
    print("Você está em OBESIDADE MÓRBIDA, cuidado!")