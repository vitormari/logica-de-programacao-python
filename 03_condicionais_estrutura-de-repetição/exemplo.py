from operator import truediv

nota = 6

if nota >= 7:
    print("passou de ano")
elif nota >= 5:
    print("recuperacao")
else:
    print("ewprovado")



idade = 20
ingresso = True

if idade >= 18 and ingresso:
    print("entrada permitida")
else:
    print("entrada nao permitida")


contador = 1
while contador <= 5:
    print(contador)
    contador += 1


for numero in range(1, 6):
    print(numero)


nomes = ["anacleto gomes", "sexista", "pinto maluquinho"]

for nome in nomes:
    print(nome)


for numero in range(1, 11):
    if numero == 7:
        pass

    if numero == 1:
        continue

    if numero == 8:
        break

    print(numero)


for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"{numero} e par")
    else:
        print(f"{numero} e impar")