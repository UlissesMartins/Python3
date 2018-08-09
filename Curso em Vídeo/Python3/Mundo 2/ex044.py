'''Exercicio 44 - Gerenciador de pagamentos
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''
print("{:=^40}".format(" LOJAS TABAJARA "))
valor = float(input("Valor das compras: R$"))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input("Qual é a opção? "))
if opcao == 1:
    pagamento = valor - (valor * 0.1)
elif opcao == 2:
    pagamento = valor - (valor * 0.05)
elif opcao == 3:
    pagamento = valor
    parcelas = pagamento / 2
    print("Sua compra será parcelada em 2 vezes de R${:.2f} SEM JUROS".format(parcelas))
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    pagamento = valor + (valor * 0.2)
    valor_parcela = pagamento / parcelas
    print("Sua compra será parcelada em {} vezes de R${:.2f} COM JUROS".format(parcelas, valor_parcela))
else:
    pagamento = valor
    print("Opção inválida. Tente novamente!")
print("Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.".format(valor, pagamento))
