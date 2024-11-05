nome = "João Pedro"
idade = 24
profissao = "Programador"
linguagem = "Python"
saldo = 45.435
PI = 3.14159

dados = {"nome": "Guilherme", "idade": 28}


# FORMATAÇÃO UTILIZANDO "%; ()".
print("Olá, me chamo %s! Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# FORMATAÇÃO UTILIZANDO "f; {}"
print (f"Olá, me chamo {nome}! Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}. ")

# FORMATAÇÃO DE DECIMAIS
print(f"Valor de PI: {PI:.2f}")

# FORMATAÇÃO DE DECIMAIS ADICIONANDO ESPAÇOS ANTERIORMENTE
print(f"valor de PI: {PI:10.2f}")

# FORMATAÇÃO UTILIZANDO "{}; .format()"
print("Nome: {} Idade: {}" .format(nome, idade))

# FORMATAÇÃO UTILIZANDO "{}; .format()" COM REPETIÇÃO
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(idade, nome))

# FORMATAÇÃO UTILIZANDO "{}; .format(parametro=parametro)" 
print("Nome: {nome} Idade: {idade}".format(idade= idade, nome= nome))

# PYTHON TAMBÉM RECONHECE O INGLÊS.
print("Nome: {name} Idade: {age}".format(age= idade, name= nome))

# FORMATAÇÃO COM IMPORTAÇÃO DE DADOS
print("Nome: {nome} Idade: {idade}".format(**dados))

# FORMATAÇÃO (f"String") com estilização
print(f"Nome: {nome} Idade: {idade} Saldo {saldo:20.1f}")
