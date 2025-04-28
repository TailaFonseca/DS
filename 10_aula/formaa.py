class Forma:
    def __init__(self,nome): 
        self.nome = nome

    def calcula_area(self): 
            raise NotImplementedError("o metado deve ser implementado em subclasse  ")

    def calcula_perimetro(self): 
            raise NotImplementedError("o metado deve ser implementado em subclasse  ")

    def __str__(self):
            return f"nome da forma geometrica: {self.nome}"