class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    def aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"aumento invalido para {self.nome}")
            return
        self.__salario = self.__salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {20}% de aumento")
    def apresentar(self):
        print(f"sou {self.nome} e ganho {self.__salario}")

ana = Funcionario('ana', 2500)

#ana.salario = 4000
print(ana.salario)


ana.apresentar()

ana.aumento(-20)

ana.apresentar()


try:
    ana.salario = 10000
except AttributeError:
    print("nao e permitido alterar o salario diretamente")

try:
    print(ana.__salario)
except AttributeError:
    print("o atributo __salario nao pode ser acesado de fora")


ana.salario = 6567235243

print(ana.__salario)