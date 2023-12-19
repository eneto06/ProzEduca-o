#Precisamos imprimir um número para cada andar de um hotel de 20 andares. 
# Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

#Imprimindo os número dos andares do 20 a ao 01

for i in range(20, 0, -1):
    if i==13:
        continue
    print(i)

#Imprimindo o numero de andares do 20 ao 01 com while
count = 20
while count >= 1:
    if count == 13:
        count -= 1
        continue
    print(count)
    count -= 1

    