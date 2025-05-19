import tkinter as tk



class App:
    def __init__(self, root):
       self.frame1 = Frame(root)
       self.frame1.pack()
      Label(self.frame1,text="conversão de centímetro para polegada"
      font=("verdana","14","bolt"), height=3).pack()

      Label(self.frame1,text="centímetros(s):").pack(side=LEFT)
      self.centimetro=Entry(self.frame1)
      self.centimetro.focus_force()
      self.centimetro.pack(side=LEFT)
      Button(self.frame1,text="Converter",command=self.converter)



      Label(self.frame1,text="Polegada(s):").pack(side=LEFT)
      self.centimetro=Entry(self.frame1)
      self.centimetro.focus_force()
      self.centimetro.pack(side=LEFT)











