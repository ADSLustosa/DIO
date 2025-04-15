class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {"\n".join([f"{chave}= {valor}\n" for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)

    def __str__(self):
        return ""

class Aves(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)



class Gato(Mamifero):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(cor_pelo, **kwargs)


class Ornitorrinco(Mamifero, Aves):
    def __init__(self, cor_pelo, cor_bico, numero_patas):
        print(Ornitorrinco.__mro__) # Method Resolution Order: Ordem de Resolucao de Metodos.
        super().__init__(cor_pelo= cor_pelo, cor_bico= cor_bico, numero_patas= numero_patas)


#gato = Gato (numero_patas= 4, cor_pelo= "Preto")
#print(gato)
ornitorrinco = Ornitorrinco(numero_patas= 2, cor_pelo= "Vermelho", cor_bico= "Laranja")
print(ornitorrinco)
