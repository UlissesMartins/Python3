n = int(input("Digite um número inteiro: "))
s = 0
while(n != 0):
	r = n % 10
	n = (n - r) // 10
	s = s + r
print(s)
	
