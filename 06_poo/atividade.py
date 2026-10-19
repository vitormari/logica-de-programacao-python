class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: au au")

    def info(self):
        print(f"{self.nome}, {self.raca}, {self.idade}")



cachorro1 = Cachorro("cupcake", "pitbull", 8)
cachorro1.info()
cachorro1.latir()

cachorro2 = Cachorro("devorador", "golden retriver", 6)
cachorro2.info()
cachorro2.latir()

cachorro1.idade = 10

cachorro1.info()