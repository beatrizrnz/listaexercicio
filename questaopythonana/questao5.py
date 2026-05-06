a = int(input("digite primeiro numero: "))
b = int(input("digite segundo numero: "))
c = int(input("digite terceiro numero: "))
d = int(input("digite quarto numero: "))
e = int(input("digite quinto numero: "))
f = int(input("digite sexto numero: "))
i = print("a soma dos numeros é: ", a + b + c + d + e + f)  
numeros = [a, b, c, d, e, f]

soma = 0
for i in numeros:
    soma += i

media = soma / 6

print("a media dos numeros é:", media)