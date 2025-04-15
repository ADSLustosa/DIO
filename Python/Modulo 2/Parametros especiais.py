# ARGUMENTOS PODEM SER PASSADOS PARA FUNÇÕES DE DIFERENTES FORMAS. O PYTHON PERMITE QUE VOCÊ CRIE FUNÇÕES QUE RECEBAM ARGUMENTOS DE FORMA DINÂMICA. ISSO É POSSÍVEL ATRAVÉS DO USO DE PARÂMETROS ESPECIAIS, COMO *ARGS E **KWARGS. *ARGS PERMITE QUE VOCÊ PASSE UM NÚMERO VARIÁVEL DE ARGUMENTOS POSICIONAIS PARA UMA FUNÇÃO. **KWARGS PERMITE QUE VOCÊ PASSE UM NÚMERO VARIÁVEL DE ARGUMENTOS NOMEADOS PARA UMA FUNÇÃO.

# POSITIONAL ONLY:
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio \n", 1999, " \nABC-1234 \n", "Fiat \n", "1.0 \n", "Gasolina \n")

# KEYWORD ONLY
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Valido
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") # Invalido

# POSITIONAL ONLY E KEYWORD ONLY
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Valido
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") # Invalido

# OBJETOS DE PRIMEIRA CLASSE
# FUNÇÕES SÃO OBJETOS DE PRIMEIRA CLASSE EM PYTHON. ISSO SIGNIFICA QUE VOCÊ PODE PASSAR FUNÇÕES COMO ARGUMENTOS PARA OUTRAS FUNÇÕES, ATRIBUÍ-LAS A VARIÁVEIS E RETORNÁ-LAS DE OUTRAS FUNÇÕES.
def somar (a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar) # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair) # O resultado da operação 10 - 10 = 0
exibir_resultado(10, 10, multiplicar) # O resultado da operação 10 * 10 = 100
exibir_resultado(10, 10, dividir) # O resultado da operação 10 / 10 = 1.0

op = somar
print(op(10, 10)) # 20

