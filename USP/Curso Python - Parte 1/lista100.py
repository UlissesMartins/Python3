lista = list(range(1, 101))
for x in lista:
    if (x % 3 == 0) and (x % 5 == 0):
        print("FizzBuzz")
    elif (x % 3 == 0):
        print("Fizz")
    elif (x % 5 == 0):
        print("Buzz")
    else:
        print(x)