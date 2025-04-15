# Polimorfismo em Python é um conceito de programação orientada a objetos que permite que diferentes classes implementem métodos com o mesmo nome, mas com comportamentos diferentes. Isso significa que você pode usar o mesmo nome de método em diferentes classes, e o Python irá determinar qual método chamar com base no objeto que está sendo usado. 

class Passaro:
    def voar(self):
        print("O pássaro está voando.")

class Pardal(Passaro):
    def vborar(self):
        return super().voar() 
    
class Avestruz(Passaro):
    def voar(self):
        print("O avestruz não pode voar.")

#FIXME: Exemplo ruim de polimorfismo, pois o método voar não existe na classe Aviao.

class Aviao:
    def voar(self):
        print("O avião está decolando.")

def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())  # Saída: O pássaro está voando.
plano_voo(Avestruz())  # Saída: O avestruz não pode voar.
plano_voo(Aviao())  # Saída: O avião está decolando.