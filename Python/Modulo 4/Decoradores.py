# Decoradores em Python são funções que permitem modificar o comportamento de outras funções ou métodos. Eles são frequentemente usados para adicionar funcionalidades, como autenticação, registro em log, verificação de permissões, entre outros.
# Decoradores são uma maneira de aplicar um padrão de design chamado "decorator pattern", que permite adicionar funcionalidades a objetos de forma dinâmica, sem alterar sua estrutura original.
# Decoradores são definidos usando a sintaxe `@decorador` antes da definição de uma função ou método. Quando a função ou método é chamado, o decorador é aplicado automaticamente.
# Decoradores podem ser usados em funções, métodos de classe e métodos estáticos.
# Eles podem receber argumentos e retornar funções ou métodos modificados.
# Decoradores são frequentemente usados em frameworks web, como Flask e Django, para adicionar funcionalidades a rotas e views.
# Decoradores podem ser encadeados, ou seja, você pode aplicar vários decoradores a uma única função ou método.
# Isso permite combinar várias funcionalidades de forma modular e reutilizável.
# Decoradores são uma parte importante da linguagem Python e são amplamente utilizados na comunidade Python.
# Eles ajudam a tornar o código mais legível, modular e reutilizável.

def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar a função")
        funcao()
        print("faz algo depois de executar a função")
    return envelope


@meu_decorador # Decorador aplicado à função ola_mundo
def ola_mundo():
    print("Olá, mundo!")


ola_mundo() # Olá, mundo!