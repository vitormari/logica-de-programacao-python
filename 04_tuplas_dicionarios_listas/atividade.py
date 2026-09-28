#1.
filmes = ["velocipastor", "megashark versus kolossus", "gente grande", "pixels", "mega shark versus mecha shark"]

print(filmes)

print(filmes[0])

print(filmes[-1])

filmes.append("minions")

filmes.remove("gente grande")

filmes[2] = "mega shark versus crocossaurus"

print(len(filmes))

#2

notas = [9.0, 3.2, 6.2, 10.0, 5.8]
print(notas)
soma = 0
menor = 4673284362
maior = -2647823
notadez = False
passou = False

for nota in notas:
    soma += nota
    if nota < menor:
        menor = nota

    if nota > maior:
        maior = nota

    if nota == 10.0:
        notadez = True

media = soma / len(notas)
if media >= 7:
    passou = True

print(soma)
print(media)
print(maior)
print(menor)
print(notadez)
print(passou)

#3.

prod = ("sabonete", "limpeza", 6.79, 67696769)
print(prod[0])
print(prod[1])
print(prod[2])
print(prod[3])

for a in prod:
    print(a)


print(len(prod))


#prod[2] = 7.69

#nao e possivel fazer uma alteraçao pois a tupla nao suporta uma alteraçao direta

#4.

funcionario = {
    "nome": "raniweg",
    "idade": 67,
    "profissao": "garoto de progama(programador)",
    "salario": 67900.00,
    "setor": "eletronico"
}

for chave, valor in funcionario.items():
    print(f"{chave}: {valor}")

funcionario["salario"] = 0.0002

funcionario["sexo"] = "masculino"

funcionario.pop("setor")
print(funcionario)

if "Setor" in funcionario:
    print("O dicionário possui a chave Setor.")
else:
    print("O dicionário não possui a chave Setor.")

for chave, valor in funcionario.items():
    print(f"{chave}: {valor}")


#5.
produtos = [
    {"Nome": "Celular", "Categoria": "Eletrônico", "Preço": 3000, "Quantidade": 10},
    {"Nome": "Laptop", "Categoria": "Eletrônico", "Preço": 5000, "Quantidade": 5},
    {"Nome": "Teclado", "Categoria": "Periférico", "Preço": 300, "Quantidade": 15},
    {"Nome": "Mouse", "Categoria": "Periférico", "Preço": 200, "Quantidade": 20},
    {"Nome": "Mousepad", "Categoria": "Acessório", "Preço": 80, "Quantidade": 30}
]

print("=== PRODUTOS DISPONÍVEIS ===")
print("\nCelular")
print("Laptop")
print("Teclado")
print("Mouse")
print("Mousepad")

print("\nProduto 1:", produtos[0])
print("Produto 2:", produtos[1])
print("Produto 3:", produtos[2])
print("Produto 4:", produtos[3])
print("Produto 5:", produtos[4])

soma = 0
for produto in produtos:
    soma += produto["Quantidade"]
print("\nQuantidade total do estoque:", soma)

preco = 0
for produto in produtos:
    preco += produto["Preço"]
print("Preço do estoque:", preco)

for produto in produtos:
    if produto["Quantidade"] < 10:
        print(f"\nO produto {produto['Nome']} está com baixo estoque.\n ")

if "Celular" not in produtos:
     print("O produto Celular está cadastrado.")

produtos[1]["Quantidade"] = 7
print("\nProduto 1:", produtos[0])
print("Produto 2:", produtos[1])
print("Produto 3:", produtos[2])
print("Produto 4:", produtos[3])
print("Produto 5:", produtos[4])

novo_cadastro = {"Nome": "Gabinete", "Categoria": "Componente", "Preço": 1500, "Quantidade": 20}
produtos.append(novo_cadastro)

print("\nProduto 1:", produtos[0])
print("Produto 2:", produtos[1])
print("Produto 3:", produtos[2])
print("Produto 4:", produtos[3])
print("Produto 5:", produtos[4])
print("Produto 6:", produtos[5])