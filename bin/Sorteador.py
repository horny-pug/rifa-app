import pandas as pd

class Sorteador():
    def __init__(self, archivo):
        self.archivo = archivo
        
    def start(self):
        self.df = pd.read_csv(self.archivo)
        self.ganadores = self.df.sample(3)
        self.tercerLugar = str(self.ganadores.iloc[0, 0])
        self.segundoLugar = str(self.ganadores.iloc[1, 0])
        self.primerLugar = str(self.ganadores.iloc[2, 0])
