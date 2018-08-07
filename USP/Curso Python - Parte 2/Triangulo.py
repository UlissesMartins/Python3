'''Exercício 1: Uma classe para triângulos
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos lados a, b e c de um triângulo.

A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.'''

class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.a = lado1
        self.b = lado2
        self.c = lado3

    def perimetro(self):
        return self.a + self.b + self.c


def main():
    t = Triangulo(1, 2, 3)
    print(t.a)
    print(t.b)
    print(t.c)
    print(t.perimetro())


main()
