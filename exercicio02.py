#Escreva um programa que leia um número inteiro positivo N e em seguida imprima N linhas do chamado triângulo de Floyd.

n = int(input())
linhas = 1
a = 1
i = 1

while linhas <= n:
    while a <= linhas:
        if a != linhas:
            print(i, end="    ")
        else:
            print(i)
        a += 1
        i += 1
    a = 1
    linhas += 1
