# FUNÇÕES SÃO BLOCOS DE CÓDIGO QUE SÃO EXECUTADOS QUANDO CHAMADOS. ELAS PODEM RECEBER PARÂMETROS E RETORNAR VALORES.

# Exemplo:
def exibir_mensagem():
    print("Olá, mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo, {nome}!")
def exibir_mensagem_3(nome="João"):
    print(f"Seja bem-vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_2(nome="Chappie") # Seja bem-vindo, Chappie!

# RETORNANDO VALORES:
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucecssor(numero):
    return numero - 1, numero + 1
    return antecessor, sucessor

def func3():
    print("Olá, mundo!")
    return None

print(calcular_total([10, 20, 34])) # 
print(retorna_antecessor_e_sucecssor(10)) # (9, 11)
print(func3()) # Olá, mundo! None

# ARGS E KWARGS:
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n". join(args)
    meta_dados = "\n".join([f"{chave}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sexta-feira, 26 de agosto de 2022",
    "Zen of Python", 
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano="1999")
