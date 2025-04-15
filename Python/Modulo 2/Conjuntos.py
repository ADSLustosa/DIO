# COMO CRIAR CONJUNTOS EM PYTHON:
# Conjuntos são coleções de itens não ordenados e não indexados. Em Python, os conjuntos são escritos com chaves.
# Exemplo:
# conjunto = {"maçã", "laranja", "uva", "pera"}
# print(conjunto) # {'uva', 'maçã', 'laranja', 'pera'} - A ORDEM DOS ELEMENTOS PODE VARIAR.

# Criando sets:
set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  
set("abacaxi") # {'a', 'c', 'b', 'i', 'x'}
set(("palio", "gol", "celta", "palio")) # {'palio', 'gol', 'celta'}
set({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set({"nome": "João", "idade": 25}) # {'nome', 'idade'}
set(range(10)) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Métodos da classe set:
# add() # add(elemento) - adiciona um elemento ao conjunto.
# update() # update(iterável) - adiciona vários elementos ao conjunto.
# remove() # remove(elemento) - remove um elemento do conjunto. Se o elemento não existir, gera um erro.
# copy() # copy() - retorna uma cópia do conjunto.
# discard() # discard(elemento) - remove um elemento do conjunto. Se o elemento não existir, não gera erro.
# pop() # pop() - remove um elemento aleatório do conjunto. Se o conjunto estiver vazio, gera um erro.
# clear() # clear() - remove todos os elementos do conjunto.
# len() # len(conjunto) - retorna o número de elementos do conjunto.
# in # elemento in conjunto - verifica se um elemento está presente no conjunto.
# not in # elemento not in conjunto - verifica se um elemento não está presente no conjunto.

# Exemplo:
sorteio = {1,2, 3, 4, 5, 6, 7, 8, 9}

sorteio.add(10) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sorteio.update([11, 12, 13]) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
sorteio.remove(13) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
sorteio.copy() # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
sorteio.discard(12) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
sorteio.pop() # {2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
sorteio.clear() # set()
len(sorteio) # 0
10 in sorteio # False
10 not in sorteio # True



# Operações com conjuntos:
{}.union # une os conjuntos: conjunto1 | conjunto2
{}.intersection # interseção: conjunto1 & conjunto2
{}.difference # diferença: conjunto1 - conjunto2
{}.symmetric_difference # diferença simétrica: conjunto1 ^ conjunto2
{}.issubset # subconjunto: conjunto1 <= conjunto2
{}.issuperset # superconjunto: conjunto1 >= conjunto2
{}.isdisjoint # disjunto: conjunto1.isdisjoint(conjunto2)
# Exemplo:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {2, 3, 4}

conjunto1.union(conjunto2), conjunto1 | conjunto2 # {1, 2, 3, 4, 5}
conjunto1.intersection(conjunto2), conjunto1 & conjunto2 # {2, 3, 4}
conjunto1.difference(conjunto2), conjunto1 - conjunto2 # {1, 5}]
conjunto1.symmetric_difference(conjunto2), conjunto1 ^ conjunto2 # {1, 5}
conjunto1.issubset(conjunto2), conjunto1 <= conjunto2 # False
conjunto1.issuperset(conjunto2), conjunto1 >= conjunto2 # True
conjunto1.isdisjoint(conjunto2) # False

