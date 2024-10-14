class Pessoa:
    def __init__(self, nome, peso, idade, ):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = False
        self.comendo = False
        self.dormindo = False


    def comer(self,alimento):
        if self.comendo == False:
            if self.dormindo == False:
                if self.falando == False:
                    print(f"{self.nome} está comendo")
                    self.comendo = True
                else:
                    (f"{self.nome} não pode falar pois está comendo")
            else:
                (f"{self.nome} não pode dormir pois está comendo")
        else:
            (f"{self.nome} ja estava  comendo")

    def dormir(self):
        if self.dormindo == False:
            if self.comendo == False:
                if self.falando == False:
                    print(f"{self.nome} está dormindo")
                    self.dormindo = True
                else:
                    (f"{self.nome} não pode dormir pois está falando")
            else:
                (f"{self.nome} não pode dormir pois está comendo")
        else:
            (f"{self.nome} ja estava dormindo")

    def falar(self,lingua):
        if self.falando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    print(f"{self.nome} está falando")
                    self.falando = True
                else:
                    (f"{self.nome} não pode falar pois está dormindo")
            else:
                (f"{self.nome} não pode falar pois está comendo")
        else:
            (f"{self.nome} ja estava está falando")

    def notcomendo(self):
        if self.comendo:
            self.comendo = False
            print(f"{self.nome} parou de comer")
        else:
            print(f"{self.nome} não está comendo")

    def notfalando(self):
        print(f"{self.nome} parou de falar")
        self.falando=False


    def notdormindo(self):
        print(f"{self.nome} acordou")
        self.dormindo=False


class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer")

class Gato(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"O {self.nome} foi miando")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(f"A {self.nome} está mugindo")
class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f"O {self.nome} está latindo")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def desmaiou(self):
        print(f"A {self.nome} desmaiou")

class Atleta:
    def __init__(self,nome,peso):
        self.nome=nome
        self.aposentado= False
        self.peso = peso
        self.aquecer= False
    def aposentado(self):
        print("O atleta está aposentado")
        self.aposentado=True
    def desaposentou(self):
        print("O atleta não está mais aposentado")
        self.aposentado=False
    def aquecer(self):
        print("O atleta está aquecendo")
        self.aquecer=True

class Corredor(Atleta):
    def __init__(self, nome,peso):
        super().__init__(nome,peso)

    def correr(self):
        if self.aquecer ==  True:
            if self.aposentado == False:
                print(f"O atleta {self.nome} foi correr")
            else:
               print(f"O atleta {self.nome} não pode correr porque está aposentado")
        else:
           print(f"O atleta {self.nome} não pode correr porque não aqueceu")


class Nadador(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def nadar(self):
        if self.aquecer == True:
            if self.aposentado == False:
                print(f"O atleta {self.nome} foi nadar")
            else:
                print(f"O atleta {self.nome} não pode nadar porque está aposentado")
        else:
            print(f"O atleta {self.nome} não pode nadar porque não aqueceu")
class Ciclista (Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)
    def pedalar(self):
        if self.aquecer == True:
            if self.aposentado == False:
                print(f"O atleta {self.nome} foi pedalar")
            else:
                print(f"O atleta {self.nome} não pode pedalar porque está aposentado")
        else:
            print(f"O atleta {self.nome} não pode pedalar porque não aqueceu")

class Triatleta(Ciclista,Corredor,Nadador,Atleta):
    def __init__(self, aposentado,peso):
        super().__init__(aposentado,peso)