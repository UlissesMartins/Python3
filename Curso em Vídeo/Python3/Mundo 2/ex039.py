'''Exercicio 39 - Alistamento Militar
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''
from datetime import date
nascimento = int(input("Informe sua data de nascimento:"))
ano_atual = date.today().year
idade = ano_atual - nascimento
print("Quem nasceu em {} tem {} anos em {}".format(nascimento, idade, ano_atual))
if idade < 18:
    falta = 18 - idade
    ano = ano_atual + falta
    print("Ainda falta(m) {} ano(s) para o alistamento".format(falta))
    print("Seu alistamento será em {}".format(ano))
elif idade > 18:
    ano = nascimento + 18
    passou = ano_atual - ano
    print("Você já deveria ter se alistado há {} ano(s).".format(passou))
    print("Seu alistamento foi em {}.".format(ano))
else:
    print("Você tem que se alistar IMEDIATAMENTE!")
