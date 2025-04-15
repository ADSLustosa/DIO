# Retornando valores da função decorada
def duplicar(funcao):
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
        return funcao(*args, **kwargs)
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()

tecnologia = aprender("Python")
print(tecnologia) # Retorna o valor da função decorada
