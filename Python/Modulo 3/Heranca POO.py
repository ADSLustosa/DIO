# Herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentois da classe pai.
# Benefícios da Herança:	
    # Representa bem os relacionamento do mundo real.
    # Reutilização de código.
    # Extensibilidade.
    # Facilita a manutenção.
    # Natureza transitiva, ou seja, se B herda de A e C herda de B, então C herda de A.

# Herança Simples: Uma classe herda de uma única classe.
class A:
    pass

class B(A):
    pass
    # A classe B herda da classe A.

# Herança Múltipla: Uma classe herda de várias classes.
class A:
    pass 
class B:
    pass
class C(A, B):
    pass
    # A classe C herda das classes A e B.