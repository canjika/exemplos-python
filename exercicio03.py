#Implemente um algoritmo que leia um Código de Operação: 

       #1: soma dois números (a + b);
       #2: soma três números (a + b + c);
       #3: multiplicação de dois números (a * b); 
       #0: sair. 

#Se o usuário digitar a operação SAIR (0), o programa mostra o MENOR resultado obtido, considerando SOMENTE as operações realizadas, e ENCERRA. Entretanto, se nenhuma operação for realizada e a operação SAIR (0) seja selecionada, a seguinte mensagem deve ser impressa "Nenhum calculo foi realizado!".  Caso contrário (operação <=3 e !=0), o sistema deve solicitar a ENTRADA dos números (a e b OU a, b e c) e imprimirá o resultado da operação (soma ou multiplicação). Após isso, o programa volta a SOLICITAR o Código de Operação para o usuário digitar uma NOVA OPERAÇÃO.

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
