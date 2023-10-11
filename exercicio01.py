#Implemente um algoritmo que LEIA, com valores reais, uma matriz com n LINHAS e m COLUNAS, definidas pelo usuário, e:
#a) Imprima a matriz criada;
#b) Imprima a SOMA dos elementos, com DUAS casas decimais, de CADA COLUNA ÍMPAR;
#c) Imprima a MÉDIA ARITMÉTICA, com UMA casa decimal, considerando TODOS os elementos que estão armazenados na SEGUNDA e QUARTA colunas;
#d) Substitua os valores da SEXTA coluna pela SOMA, com uma casa decimal, dos valores das COLUNAS 1 e 2;
#e) Imprima a matriz modificada.

n = int(input())
m = int(input())

#criando a matriz
M = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(float(input()))
    M.append(linha)

#printando a matriz   
for k in range(n):
    for g in range(m):
        if g == m-1:
            print(M[k][g])
        else:
            print(M[k][g], end=" ")

print()

#soma das colunas impares
for x in range(m):
    somaI = 0
    for z in range(n):
        if x%2 == 0:
            somaI+=M[z][x]
    if somaI != 0:
        print("{:.2f}".format(somaI))
        
print()

#media da segunda e quarta coluna      
somaS_Q = 0
for c in range(m):
    for l in range(n):
        if c == 1 or c == 3:
            somaS_Q+=M[l][c]

media = somaS_Q/(n*2)
print("{:.1f}".format(media))

print()

#soma primeira e segunda coluna
somaP_S = 0
for c in range(m):
    for l in range(n):
        if c == 0 or c == 1:
            somaP_S+=M[l][c]

#substituindo na matriz
for s in range(n):
    for t in range(m):
        if t == 5:
            M[s][t] = somaP_S

#printando a matriz
for k in range(n):
    for g in range(m):
        if g == m-1:
            print("{:.1f}".format(M[k][g]))
        else:
            print("{:.1f}".format(M[k][g]), end=" ")
