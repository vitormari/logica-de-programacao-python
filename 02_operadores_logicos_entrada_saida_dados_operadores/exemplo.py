idade = 20

possui_carteira = True

resultado = idade >= 18 and possui_carteira
print(resultado)


idade = 16

acompanhado = True
resultado = idade >= 18 or acompanhado
print(resultado)



aluno_matriculado = True

print(not aluno_matriculado)

idade = 18

print(idade == 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)
print(idade != 18)

if idade >= 18:
    print("maior de idade")


idade = 16

if idade >= 18:
    print("maior de idade")
else:
          print("menor de idade")