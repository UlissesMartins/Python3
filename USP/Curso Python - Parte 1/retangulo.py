def retangulo(width, heigh):
    i = 0
    j = 0

    for j in range(heigh):

        for i in range(width):
            print('#', end="")

        print()


width = int(input('digite a largura: '))
heigh = int(input('digite a altura: '))

retangulo(width, heigh)