valor = ("12", 23, False, 'a, b, c', [12], (12))
entero  = int(valor[0])
cadena = str(valor[1])
boleano = int(valor[2])
lista = valor[3].split(",")
print(type(entero), entero)
print(type(cadena), cadena)
print(type(boleano), boleano)
print(type(lista), lista)



# # Ver que tipo de datos sale de esto
# frutas = ["manzana", "banana", "naranja"]
# print(enumerate(frutas)) # <enumerate object at 0x7f876c38e700>
# print(type(enumerate(frutas))) # <class 'enumerate'>
# print(dict(enumerate(frutas))) # {0: 'manzana', 1: 'banana', 2: 'naranja'}
# print(list(enumerate(frutas))) # [(0, 'manzana'), (1, 'banana'), (2, 'naranja')]
# print(tuple(enumerate(frutas))) # ((0, 'manzana'), (1, 'banana'), (2, 'naranja'))


persona = {
    'name': 'eder',
    'edad':12
}
print(type(persona.items())) # <class 'dict_items'>
print(persona.items()) # dict_items([('name', 'eder'), ('edad', 12)])
print(list(persona.items())) # [('name', 'eder'), ('edad', 12)]
print(tuple(persona.items())) # (('name', 'eder'), ('edad', 12))
print(list(enumerate(persona.items()))) # (('name', 'eder'), ('edad', 12))


# recorrer un diccionario