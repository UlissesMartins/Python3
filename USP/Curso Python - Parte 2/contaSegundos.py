entrada = int(input("Por favor, entre com o número de segundos que deseja converter:"))
dias = entrada // 86400
entrada1 = entrada % 86400
horas = entrada1 // 3600
entrada2 = entrada1 % 3600
minutos = entrada2 // 60
entrada3 = entrada2 % 60
print(dias, "dias,", horas, "horas,", minutos, "minutos e", entrada3, "segundos")
