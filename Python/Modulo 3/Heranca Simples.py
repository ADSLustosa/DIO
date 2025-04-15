class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor.")


    def __str__(self):
        return self.cor


class Motocicleta(Veiculo):
    pass
    

class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim!' if self.carregado else 'Não estou carregado!'}")


# moto = Motocicleta("Vermelha", "ABC-1234", 2)
# moto.ligar_motor()

# carro = Carro("Azul", "XYZ-9876", 4)
# carro.ligar_motor()

caminhao = Caminhao("Branco", "DEF-4567", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
