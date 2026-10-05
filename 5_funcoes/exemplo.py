def saudacao():
    print("ola seja bem vindo")

saudacao()

def saudacoes(nome):
    print(f"ola {nome}")

saudacoes("ana")
saudacoes("joao")

def apresentar(nome, idade):
    print(f"nome{nome}")
    print(f"idade{idade}")

apresentar("joao", 18)
apresentar("ana", 1234)

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")

somar(2, 2)



def cadastrar_produto():
    nome = input("digite o nome do produto: ")
    preco = float(input("digite o preco do produto: "))
    return nome, preco

def exibir_produto(nome, preco):
    print("\n==== PRODUTO =====")
    print(f"nome: {nome}")
    print(f"preco: R$ {preco:.2f}")


nome, preco = cadastrar_produto()
exibir_produto(nome, preco)