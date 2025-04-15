# Atributos do objeto: todo objeto tem atributos, que são as características do objeto. Por exemplo, um carro pode ter atributos como cor, modelo e ano. Esses atributos podem ser acessados e modificados usando a notação de ponto. Por exemplo, se tivermos um objeto carro, podemos acessar seu atributo cor usando carro.cor.
class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

Aluno1 = Estudante("João", 12345)
Aluno2 = Estudante("Maria", 67890)
mostrar_valores(Aluno1, Aluno2)  # Saída: João - 12345 - DIO, Maria - 67890 - DIO
# Atributos de classe: são atributos que pertencem à classe em si, e não a uma instância específica da classe. Eles são compartilhados por todas as instâncias da classe. Por exemplo, se tivermos uma classe Carro com um atributo de classe chamado numero_de_rodas, todas as instâncias da classe Carro terão o mesmo valor para esse atributo.

Estudante.escola= "Python"  # Mudando o valor do atributo de classe escola

Aluno1.matricula = 54321
Aluno2.matricula = 98765
mostrar_valores(Aluno1, Aluno2)  # Saída: João - 54321 - DIO, Maria - 98765 - DIO
# Atributos de classe são definidos fora do método __init__ e são acessados usando a notação de ponto. Por exemplo, se quisermos acessar o atributo de classe escola, podemos fazer isso usando Estudante.escola.
