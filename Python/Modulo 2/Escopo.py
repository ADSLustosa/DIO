# Escopo local é o que está dentro de uma função.
# Escopo global é o que está fora de uma função.

salario = 2000


def salario_bonus(bonus, lista):
    global salario
    
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"Lista aux: {lista_aux}")
    salario += bonus
    return salario

lista = [1]

salario_com_bonus = salario_bonus(500, lista) # 3000
print(salario_com_bonus) # 3000
print(lista) # [1]