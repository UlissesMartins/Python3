# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O progama vai perguntar o valor da casa, o salário do comprador e em quanto anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
valor = float(input("Qual o valor da casa? R$"))
salário = float(input("Qual o salário do comprador? R$"))
anos = int(input("Em quantos anos ele vai pagar? "))
prestacao_maxima = salário * 0.30
prestacao = valor / (anos * 12)
print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(valor, anos, prestacao))
if prestacao <= prestacao_maxima:
    print("Emprestimo pode ser CONCEDIDO!")
else:
    print("Emprestimo NEGADO!")