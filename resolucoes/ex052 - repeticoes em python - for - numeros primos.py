'''
Faça um programa que leia um número inteiro e diga se ele é ou
não um número primo.
'''

print("")
num = int(input("Digite um número inteiro: "))
cont = 0
for i in range(1,num+1):
    if (num % i == 0):
        cont = cont + 1
if (cont == 2):
    print(f"O número {num} É PRIMO!")
else:
    print(f"O número {num} NÃO É PRIMO!")
    
