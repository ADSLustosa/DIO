frutas = ("maçã", "laranja", "uva", "pera")
frutas[0] # maçã
frutas[1] # laranja
frutas[-1] # pera
frutas[-2] # uva

# As tuplas são imutáveis, ou seja, não é possível alterar o valor de um elemento da tupla.

# Métodos da classe tupla:
().count # count(valor) - retorna o número de vezes que um valor ocorre na tupla.
().index # index(valor) - retorna o índice da primeira ocorrência de um valor na tupla. 
len() # len(tupla) - retorna o número de elementos da tupla.
max() # max(tupla) - retorna o maior valor da tupla.
min() # min(tupla) - retorna o menor valor da tupla.
sum() # sum(tupla) - retorna a soma dos valores da tupla.
sorted() # sorted(tupla) - retorna uma lista ordenada com os valores da tupla.
tuple() # tuple(lista) - converte uma lista em uma tupla.
# Exemplo:
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla.count(2) # 1
tupla.index(2) # 1
len(tupla) # 10
max(tupla) # 10
min(tupla) # 1
sum(tupla) # 55
sorted(tupla) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla = tuple(lista) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
