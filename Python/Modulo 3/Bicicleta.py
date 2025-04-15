class Bicicleta: # Criar a classe principal
    def __init__(self, cor, modelo, ano, valor): # Método construtor
        self.cor = cor # Self é uma referência a própria classe. Também é usado para acessar variáveis e métodos da classe. Pode ser substituído por this.
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Buzinando...")
    
    def parar(self):
        print("Parando...")
    
    def correr(self):
        print("Correndo...")

    def trocar_marcha(numero_marcha):
        print(numero_marcha)
        print("Marcha alterada...")

    #def __str__(self):
        #return f"Bicicleta: cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', ' .join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}" # {Chama o nome da classe}:
        #{', ' separa os atributos da classe e os valores dos atributos.}
        # .join {chama o método join para juntar os atributos e valores da classe.} 
        # [f'{chave}= {valor}' for chave, valor in self.__dict__.items()] {itera sobre os atributos e valores da classe.} 
        # self.__dict__.items() {chama o dicionário da classe.}

b1 = Bicicleta("Azul", "Caloi", 2020, 500.00) # Instanciar a classe Bicicleta
b1.buzinar()
b1.parar()
b1.correr()
print("Cor da bicicleta:", b1.cor, "\nModelo da biciclleta: ", b1.modelo, "\nAno de fabricação da bicicleta: ", b1.ano, "\nValor da bicicleta: ", b1.valor) # Acessar os atributos da classe

b2 = Bicicleta("Vermelha", "Monark", 2021, 600.00)
print(b2)
b2.trocar_marcha()
