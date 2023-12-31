#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


while True:
   nome = input("Digite seu nome completo: ")
   ano_nascimento = input("Digite seu ano de nascimento: ")

   if ano_nascimento.isdigit():
       ano_nascimento = int(ano_nascimento)
       if 1922 <= ano_nascimento <= 2021:
           idade = 2022 - ano_nascimento
           print(f"{nome}, você completou {idade} anos em 2022.")
           break
       else:
           print("O ano de nascimento deve estar entre 1922 e 2021.")
   else:
       print("O ano de nascimento deve ser um número.")

