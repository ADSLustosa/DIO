# Encapsulamento em Python é um conceito de programação orientada a objetos que permite ocultar os detalhes internos de uma classe e expor apenas o que é necessário para o uso da classe. Isso ajuda a proteger os dados e a manter a integridade do objeto.
# O encapsulamento é alcançado em Python usando modificadores de acesso, como público, protegido e privado.

# Modificadores de acesso:
# - Público: Atributos e métodos são acessíveis de qualquer lugar.
# - Privado: Atributos e métodos são acessíveis apenas dentro da classe. Em Python, isso é indicado por dois sublinhados antes do nome (ex: __atributo).

#Exemplo:

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("João", 2000)
print(f"Nome: {pessoa.nome} \nIdade: {pessoa.idade} anos")


