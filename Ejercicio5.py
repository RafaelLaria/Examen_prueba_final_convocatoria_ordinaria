import numpy as np

class Alumno:
    def __init__(self):
        self.notas = []
    
    def leer_notas(self):
        with open('fichero.txt', 'r') as f:
            for linea in f:
                linea = float(linea)
                return self.notas.append(linea)
    
    def calcular_promedio(self):
        media = np.mean(self.notas)
        return media

alumno = Alumno()
alumno.leer_notas()
print('La media es:', alumno.calcular_promedio())