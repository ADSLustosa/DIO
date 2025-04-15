# Uma Interface é um contrato que uma classe deve seguir.
# Interfaces definem o que uma classe deve fazer e não como ela deve fazer. Elas são usadas para garantir que uma classe implemente certos métodos e atributos, sem especificar a implementação desses métodos.
# Em Python, não há suporte nativo para interfaces como em outras linguagens de programação, como Java ou C#. No entanto, podemos simular o comportamento de interfaces usando classes abstratas e o módulo abc (Abstract Base Classes).
# # O módulo abc fornece a classe ABC (Abstract Base Class) e o decorador @abstractmethod, que podem ser usados para definir métodos abstratos que devem ser implementados por subclasses.
# Classes abstratas não podem ser instanciadas diretamente. Elas são usadas como base para outras classes que implementam os métodos abstratos definidos na classe abstrata.

# # Exemplo de uma interface em Python usando classes abstratas:

from abc import ABC, abstractmethod

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("A TV está ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("A TV está desligada!")

    @property
    def marca(self):
        return "LG"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar condicionado...")
        print("O ar condicionado está ligado!")

    def desligar(self):
        print("Desligando o ar condicionado...")
        print("O ar condicionado está desligado!")

    @property
    def marca(self):
        return "Samsung"   

controle = ControleTV()
controle.ligar() 
controle.desligar()  

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca) # Samsung
# # Resumo:
# - Uma interface é um contrato que uma classe deve seguir.
# - Interfaces definem o que uma classe deve fazer e não como ela deve fazer.
# - Em Python, podemos simular o comportamento de interfaces usando classes abstratas e o módulo abc.
# - Classes abstratas não podem ser instanciadas diretamente.
# - Elas são usadas como base para outras classes que implementam os métodos abstratos definidos na classe abstrata.
# - O módulo abc fornece a classe ABC (Abstract Base Class) e o decorador @abstractmethod, que podem ser usados para definir métodos abstratos que devem ser implementados por subclasses.
# - O decorador @abstractproperty pode ser usado para definir propriedades abstratas que devem ser implementadas por subclasses.
# - As classes que herdam de uma classe abstrata devem implementar todos os métodos e propriedades abstratas para serem instanciadas.
# - Se uma classe não implementar todos os métodos e propriedades abstratas, ela não poderá ser instanciada e gerará um erro.
# - O uso de interfaces e classes abstratas ajuda a garantir que as classes sigam um contrato específico, promovendo a consistência e a reutilização de código.
# - Isso é especialmente útil em projetos grandes e complexos, onde várias classes podem interagir entre si.
# - As interfaces também ajudam a definir uma API clara e consistente para as classes, facilitando a compreensão e o uso dessas classes por outros desenvolvedores.
# - Além disso, o uso de interfaces e classes abstratas pode ajudar a evitar problemas de dependência entre classes, tornando o código mais modular e fácil de manter.
# - As interfaces também podem ser usadas para implementar o princípio da inversão de dependência, que é um dos princípios SOLID de design de software.