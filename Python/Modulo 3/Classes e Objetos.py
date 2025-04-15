# Uma Classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente.
# Os Objetos podem ser utilizados diretamente e eles possuem as características e comportamentos definidos pela classe.

class Cachorro:
    def __init__(self, nome, cor, acordado= True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("Au Au")

    def dormir(self):
        self.acordado = False
        print("Zzzzz")

cao_1 = Cachorro("Chappie", "Amarelo", False)
cao_2 = Cachorro("Aladim,", "Branco e preto")

cao_1.latir()

print(cao_1.acordado)

cao_2.dormir()
print(cao_2.acordado)