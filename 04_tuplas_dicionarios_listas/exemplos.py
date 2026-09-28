# LISTAS / TUPLAS E DICIONÁRIOS

# 1. Listas

nomes = ["Ana", "Carlos", "João", "Maria"]

print(nomes)

# 2. Acessando elementos da lista

print(nomes[3])

# Podemos acessar o último elemento da tabela usando o -1
print(nomes[-1])

# 3. Alternando Elementos

nomes[0] = "Pedro"

#insert() adiciona um elemento em uma posição espécífica

# 4. Adicionar elementos

nomes.append("Lucas")
print(nomes)

nomes.insert(1, "Mariana")
print(nomes)

# 5. Removendo Elementos
#remove um elemento pelo valor

nomes.remove("Lucas")
print(nomes)

#pop() remove um elemento pelo indice
nomes.pop(0)
print(nomes)

# 6. Tamanho da Lista
#len() informa a quantidade de elementos
print(len(nomes))

# 7. Percorrendo uma Lista
for nome in nomes:
    print(nome)

# 8. Verificando se um elemento existe

if "joão" in nomes:
    print("joão está na lista")
else:
    print("joão não está na lista")

# 9. Lista com diferentes tipos de dados
dados = ["João", 18, 1.76]
print(dados)

# 10. Lista de números
notas = [7.5, 5.0, 6.5, 9.0]

soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média: {media}")

# 11. Tuplas
#Tuplas são semelhantes as listas
#As tuplas não se alteram

coordenadas = (10, 20)
print(coordenadas)

print(coordenadas[0])

# 12. Dicionários

#Dicionarios armazenam informações no formato: Chave: valor
aluno = {
    "nome": "Carlos",
    "idade": 67,
    "nota": 6.7
}
print(aluno)

# 13. Acessando valores do dicionário

print(aluno["nota"])
print(aluno["idade"])
print(aluno["nota"])

# 14. Alterando valores

aluno["nota"] = 9.0
print(aluno)

# 15. adicionando novos dados

aluno["curso"] = "informatica"
print(aluno)

# 16. removendo dados
del aluno["curso"]
print(aluno)

# 17. percorrendo um dicionario
for chave in aluno:
    print(chave)

#podemos acessar a chave e o valor ao mesmo temo
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# 18. verificando uma chave
if "nome" in aluno:
    print("a chave nome existe")

# 19. dicionario com lista
aluno = {
    "nome": "Ana",
    "notas": [8.0, 7.5, 9.0]
}