class Lista:
    def __init__(self):
        self.lista = []
    def __str__(self):
        return f'LISTA: {self.lista}'
    
    def dar_lista(self):
        while len(self.lista) < 10:
            elemento = float(input('Escriba un elemento:'))
            self.lista.append(elemento)

class Suma:
    def __init__(self, l1st  : Lista):
        self.lista = l1st.lista
        self.resultado = self.sumar()

    def sumar(self):
        suma = 0
        for e in self.lista:
            suma += e
        return suma
        

lista = Lista()
lista.dar_lista()
print(lista)
resultado = Suma(lista)
print(resultado.resultado)
