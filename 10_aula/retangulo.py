from formaa import Forma
class Retangulo(Forma):
     def __init__(self,nome,base,altura):
         super().__init__ (nome)
         self.lado = altura
 
     def calculaArea(self,base,altura):
             return base * altura

     def __str__(self):
            return f"{super(). __str__()} com medida de base * altura = {self.base}"