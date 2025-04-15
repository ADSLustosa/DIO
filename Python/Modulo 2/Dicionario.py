# Um dicionário é uma coleção desordenada, mutável e indexada. Em Python, os dicionários são escritos com chaves e têm chaves e valores.
# Exemplo
pessoa = { "nome": "João", "idade": 25, "cidade": "São Paulo" }
pessoa2 = dict(nome="João", idade=25)
pessoa3["telefone"] = "11999999999" # { "nome": "João", "idade": 25, "cidade": "São Paulo", "telefone": "11999999999" }

dados = {"nome": "João", "idade": 25, "telefone": "11999999999"}
dados["nome"] # João
dados["idade"] # 25
dados["telefone"] # 11999999999

dados["nome"] = "Maria"
dados["idade"] = 28
dados["telefone"] = "11988888888"
dados # { "nome": "Maria", "idade": 28, "telefone": "11988888888" }

# DICIONÁRIOS ANINHADOS:
contatos= {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "11999999999"},
    "giovanna@gmail.com" : {"nome": "Giovanna", "telefone": "11988888888"},
    "chappie@gmail.com" : {"nome": "Chappie", "telefone": "11977777777"},
    "melaine@gmail.com" : {"nome": "Melaine", "telefone": "11966666666"},
    }
contatos["giovanna@gmail.com"] # { "nome": "Giovanna", "telefone": "11988888888" }

#ITERAR SOBRE DICIONÁRIOS:
for chave, valor in contatos.items():
    print(chave) #

# MÉTODOS DA CLASSE DICT:
{}.copy() # Retorna uma cópia do dicionário
{}.fromkeys("a", "b") # Retorna um dicionário com a chave e o valor especificados
{}.get("a") # Retorna o valor da chave especificada
{}.items() # Retorna uma lista contendo uma tupla para cada par de chave-valor
{}.keys() # Retorna uma lista contendo as chaves do dicionário
{}.pop("a") # Remove a chave especificada e retorna o valor
{}.popitem() # Remove o último par de chave-valor inserido
{}.setdefault("a") # Retorna o valor da chave especificada. Se a chave não existir, insere a chave com o valor especificado
{}.update({"a": "b"}) # Atualiza o dicionário com a chave e o valor especificados
{}.values() # Retorna uma lista contendo os valores do dicionário -