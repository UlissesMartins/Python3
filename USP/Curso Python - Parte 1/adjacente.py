n = int(input("Digite um numero inteiro: "))
antes = n % 10
n = n // 10;
nIguais = False;
y = 0
while n > 0 and not nIguais:
    novo = n % 10
    if novo == antes:
        nIguais = True
    else:
        y = y + 1
    antes = novo
    n = n // 10

if nIguais:
    print("sim")
else:
    print("não")
