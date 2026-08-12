n = int(input("Digite um número para calcular a sequencia de fibonacci: "))

a = 0
b = 1
soma = 0

for i in range(n):
    print(a)
    soma = soma + a

    proximo = a + b
    a = b
    b = proximo

print("Soma:", soma)