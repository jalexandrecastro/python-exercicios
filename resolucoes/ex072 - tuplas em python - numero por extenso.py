'''
Crie um programa que tenha uma tupla totalmente preenchida com
uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.
'''
print("")

tupla = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis",
         "Sete", "Oito", "Nove", "Dez", "Onze",
         "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis",
         "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    while True:
        if num < 0 or num > 20:
            num = int(input("Tente novamente. Digite um número entre 0 e 20: "))
        if num >= 0 and num <= 20:
            break
    print(f"Você digitou o número {tupla[num]}.")
    resp = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    if resp in "Nn":
        print("Finalizando ... Até a próxima!")
        break
