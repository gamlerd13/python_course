class Perro:
    #constructor
    def __init__(self, tamano, edad, color, raza, nombre):
        self.tamano = tamano
        self.edad = edad
        self.color = color
        self.raza = raza
        self.nombre = nombre
    # Metodos
    # Those are a getter method
    def ladrar(self):
        print(f"{self.nombre}esta ladrando")
    def comer(self):
        print(f"{self.nombre} esta comiendo")
    def jugar(self):
        print("El perro esta comiendo")
    # This a setter method
    def cambiar_nombre(self, nombre):
        self.nombre = nombre
        print(f"El perro ahora se llama {nombre}")

# Instanciar un objeto

tommy = (1.2, 13, "blanco", "pitbull", "tommy")
cody = [1.2, 13, "negro", "cocker", "cody"]

# Instanciar con un objeto

simon = {
    'tamano': 1.32,
    'edad': 48,
    'color': 'verde',
    'raza': 'chiwuwa',
    'nombre': 'simon'
}

# El operador de desempaquetado (*) en Python es una característica muy útil que te permite tomar elementos de una estructura (como una lista o una tupla) y pasarlos como argumentos individuales a una función o constructor que espera varios argumentos por separado.
# mi_perro = Perro(*tommy)

mi_perro = Perro(**simon)
mi_perro.comer()
mi_perro.cambiar_nombre("terminator")
print(mi_perro.nombre)