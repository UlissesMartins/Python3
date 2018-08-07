n = int(input("Digite um número inteiro: "))
x = 2
Primo = True
while(x < n and Primo):
	Primo = not ((n % x) == 0)
	x = x + 1
if(Primo):
	print("primo")
else:
	print("não primo")
