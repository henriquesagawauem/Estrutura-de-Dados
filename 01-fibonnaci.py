n = int(input("Digite um número: "))

a = 0
b = 1
soma = 0

for i in range(n - 1):

    soma = soma + b
    if i == n - 2:
        print(str(a) + " + " + str(b) + " =", + soma)
    else:
        print(str(a) + " + ", end="")
    temp = b
    b = a + b
    a = temp