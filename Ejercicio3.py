class Nota:
    def __init__(self, nota : float):
        self.nota = nota
    def __str__(self):
        return f'NOTA: {self.nota}'
    
    def evaluar(self):
        if self.nota >= 5:
            return 'Aprobado'
        else:
            return 'Suspenso'
    
alumno = Nota(4.5)
print(alumno)
print(alumno.evaluar())
