class Perro:
    #constructor
    def __init__(self, tamano, edad, color, raza, nombre):
        self.tamano = tamano
        self.edad = edad
        self.color = color
        self.raza = raza
        self.nombre = nombre
    # Metodos
    def ladrar(self):
        print(f"{self.nombre}esta ladrando")
    def comer(self):
        print(f"{self.nombre} esta comiendo")
    def jugar(self):
        print("El perro esta comiendo")
    def cambiar_nombre(self, nombre):
        self.nombre = nombre
        print(f"El perro ahora se llama {nombre}")

# Instanciar un objeto

carlos = (1.2, 13, "blanco", "pitbull", "carlos")
sergio = [1.2, 13, "blanco", "pitbull", "carlos"]



mi_perro = Perro(carlos)
mi_perro.comer()
mi_perro.cambiar_nombre("tommy")
print(mi_perro.nombre)