len: Retorna o tamanho de um objeto
    linguagens = ["Python", "Js", "C", "Java", "Ruby"]
    print(len(linguagens)) # 5


[]. append: Serve para incluir valores em uma lista
    lista = []
    lista.append(1)
    lista.append("Python")
    lista.append([40, 30, 20])
    print(lista) # [1, "Python", [40, 30, 20]]

[]. clear: Limpa a lista
    lista = [1, "Python", [40, 30, 20]]
    print(lista) # [1, "Python", [40, 30, 20]]
    lista.clear[]
    print(lista) # []

[]. copy: Copia a lista mas os IDs são diferentes
    lista = [1, "Python", [40, 30, 20]]
    lista.copy()
    print(lista) # [1, "Python", [40, 30, 20]]

[]. count: Conta a quantidade de vezes que um valor aparece na lista
    cores = ["vermelho", "azul", "verde", "azul"]
    cores.count("vermelho") # 1
    cores.count("azul") # 2
    cores.count("verde") # 1

[]. extend: Adiciona valores de uma lista em outra, mesmo que hajam valores repetidos
    linguagens = ["Python", "Js", "C"]
    print(linguagens) # ["Python", "Js", "C"]
    linguagens.extend(["Java", "Ruby"])
    print(linguagens) # ["Python", "Js", "C", "Java", "Ruby"]

[]. index: Retorna o índice de um valor na lista
    linguagens = ["Python", "Js", "C", "Java", "Ruby"]
    print(linguagens.index("Java")) # 3
    print(linguagens.index("Python")) # 0

[]. pop: Remove um valor da lista1 e retorna o valor removido
    linguagens = ["Python", "Js", "C", "Java", "Ruby"]
    print(linguagens.pop(3)) # Java
    print(linguagens) # ["Python", "Js", "C", "Ruby"]

[]. remove: Remove um valor da lista
    linguagens = ["Python", "Js", "C", "Java", "Ruby"]
    linguagens.remove("Java")
    print(linguagens) # ["Python", "Js", "C", "Ruby"]

[]. reverse: Inverte a ordem dos valores da lista
    linguagens = ["Python", "Js", "C", "Java", "Ruby"]
    linguagens.reverse()
    print(linguagens) # ["Ruby", "Java", "C", "Js", "Python"]

[]. sort: Ordena os valores da lista
    numeros = [10, 3, 5, 1, 8]
    numeros.sort()
    print(numeros) # [1, 3, 5, 8, 10]

[]. sorted: Retorna uma lista ordenada sem alterar a lista original
    numeros = [10, 3, 5, 1, 8]
    print(sorted(numeros)) # [1, 3, 5, 8, 10]
    print(numeros) # [10, 3, 5, 1, 8]