'''
Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km
para viagens de até 200 Km e R$ 0,45 para viagens mais longas.
'''

d = float(input("Distância da viagem em Km? "))
if d <= 200:
    preco = d * 0.50
else:
    preco = d * 0.45
print(f"Preço da Passagem: R$ {preco:.2f}")
