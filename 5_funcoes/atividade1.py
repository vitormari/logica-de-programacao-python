def cakcyka_naedua():
    nome = input("Digite seu nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    soma = nota1 + nota2 + nota3
    media = soma / 3

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "recuperacao"
    else:
        situacao = "Reprovado"

    print(f"nome: {nome}")
    print(f"nota1: {nota1}")
    print(f"nota2: {nota2}")
    print(f"nota3: {nota3}")
    print(f"media: {media}")
    print(f"situacao: {situacao}")


cakcyka_naedua()