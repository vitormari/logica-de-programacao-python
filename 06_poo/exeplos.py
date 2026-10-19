class Celular:
    def __init__(self, marca, modelo, cor, bateria = 100):
         self.marca = marca
         self.modelo = modelo
         self.cor = cor
         self.bateria = bateria
         self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("sem bateria, bote pra carregar")
        else:
            self.ligado = True
            print(f"ligado com {self.bateria} por cento")

celular1 = Celular("samsung", "galaxy s23", "preto")
celular2 = Celular("motorola", "moto6", "azul", 30)

print(celular2.marca)

celular1.cor = "branco"
print(celular1.cor)

celular2.ligar()

