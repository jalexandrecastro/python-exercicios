'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada (flag). No final, mostre quantos
números foram digitados e qual foi a soma entre eles desconsiderando
o flag.
'''

print("")
soma = 0
cont = 0
while True:
    num = int(input("Digite um valor (999 para parar): "))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print("")
print("A soma dos {} valores foi {}!".format(cont, soma))


