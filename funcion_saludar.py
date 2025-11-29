class Nombre:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return f'NOMBRE: {self.nombre}'
    
    def saludar(self):
        return f'Hola {self.nombre}'
    
persona = Nombre('Pancho')
print(persona.saludar())