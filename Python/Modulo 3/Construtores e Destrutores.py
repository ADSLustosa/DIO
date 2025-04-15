# Método Construtor é executado quando uma nova classe é instanciada. Ele inicializa o estado do objeto. 
    # Para declarar um Método Construtor, criamos um método com o nome __init__.
    # O Método Construtor é sempre chamado com a palavra-chave super.
class Cachorro:
    def __init__(self, nome, cor, acordado= True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

# Método Destrutor é sempre executado quando uma instância (objeto) é destruída.
    # Destrutores em Python não são tão necessários quando em C++ ou Java, porque o Python tem um coletor de lixo que gerencia a memória automaticamente.
    # Para declarar um Método Destrutor, criamos um método com o nome __del__.
    # O Método Destrutor é sempre chamado com a palavra-chave super.
    
    def __del__(self):
        print("Removendo a instância da classe.")
    
    def falar(self):
        print("Auau")

def criar_cachorro():
        c = Cachorro("Zeus", "Branco e preto", False)
        print(c.nome)
    
c = Cachorro ("Chappie", "Amarelo")
c.falar()

print("Olá, Mundo!")
del c
print("Olá, Mundo!")
print("Olá, Mundo!")
print("Olá, Mundo!")
print("Olá, Mundo!")

criar_cachorro()