# Métodos de classe estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro de classe como primeiro argumento. Isso significa que eles podem acessar e modificar atributos de classe. Eles são definidos usando o decorador @classmethod e são chamados na classe, não em uma instância da classe.

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_da_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

# p = Pessoa ("João", 30)
# print(p.nome, p.idade)  # Saída: João 30


p = Pessoa().criar_da_data_nascimento(1990, 1, 21, "Maria")
print(p.nome, p.idade)  # Saída: Maria 35

print(Pessoa.maior_idade(17))  # Saída: False
print(Pessoa.maior_idade(18))  # Saída: True
# Métodos estáticos não recebem um primeiro argumento explícito. Ele também é um método vinculado à classe, mas não tem acesso ao estado da classe ou do objeto. Eles são definidos usando o decorador @staticmethod e são chamados na classe ou em uma instância da classe.

# MÉTODOS DE CLASSE X MÉTODOS ESTÁTICOS:
# Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.
# Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo.

# Quando utilizar métodos de classe ou estáticos?
# Geralmente usamos o método de classe para criar métodos de fábrica.
# Geralmente usamos métodos estáticos para criar funções utilitárias.