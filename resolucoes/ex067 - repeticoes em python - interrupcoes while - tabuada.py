'''
Faça um programa que mostre a tabuada de vários números, um de
cada vez, para cada valor digitado pelo usuário. O programa
será interrompido quando o número solicitado for negativo.
'''
print("")

while True:
    valor = int(input("Quer ver a tabuada de qual valor? "))
    if valor < 0:
        print("Você digitou um valor negativo. Programa finalizado!")
        break
    print(20 * "-")
    i = 1
    while i <= 10:
        print(f"{valor} x {i} = {valor * i}")
        i = i + 1
    print(20 * "-")
    

