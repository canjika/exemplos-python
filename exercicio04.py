#Escreva um programa que leia uma matriz com n linhas e m colunas. Após isso, ordene os elementos em cada linha (ordem crescente). Importante: não utilize funções prontas da linguagem para ordenação! Escreva o seu algoritmo de ordenação.

#Para ler a matriz, primeiro será informado o número de linhas e depois o número de colunas. Após a leitura das dimensões da matriz, os elementos de cada linha da matriz estão dispostos linha por linha.

n = int(input())
sum2 = 0
sum3 = 0
mult = 0
value = 0

while n != 0:
    if n == 1:
        a = int(input())
        b = int(input())
        sum2 = a + b
        print(f"(a+b) = {sum2}")
        if value == 0:
            value = sum2
        else:
            if value > sum2:
                value = sum2
    elif n == 2:
        a = int(input())
        b = int(input())
        c = int(input())
        sum3 = a + b + c
        print(f"(a+b+c) = {sum3}")
        if value == 0:
            value = sum3
        else:
            if value > sum3:
                value = sum3
    elif n == 3:
        a = int(input())
        b = int(input())
        mult = a * b
        print(f"(a*b) = {mult}")
        if value == 0:
            value = mult
        else:
            if value > mult:
                value = mult

    n = int(input())

if sum2 == sum3 == mult == 0:
    print("Nenhum calculo foi realizado!")
else:
    print(f"Menor resultado: {value}")
