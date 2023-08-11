import json

with open('./datos/datos.json') as datos:
    datos = json.load(datos)
d = list(datos.items())
print(type(d))

# rrecorrer un diccionario en for

for clave, valor in datos.items():
    print(f"{clave} ==> {valor}")

print(type(datos.items()))



# Ver que tipo de datos sale de esto
frutas = ["manzana", "banana", "naranja"]
print(enumerate(frutas)) # <enumerate object at 0x7f876c38e700>
print(type(enumerate(frutas))) # <class 'enumerate'>
print(dict(enumerate(frutas))) # {0: 'manzana', 1: 'banana', 2: 'naranja'}
print(list(enumerate(frutas))) # [(0, 'manzana'), (1, 'banana'), (2, 'naranja')]
print(tuple(enumerate(frutas))) # ((0, 'manzana'), (1, 'banana'), (2, 'naranja'))


persona = {
    'name': 'eder',
    'edad':12
}
print(type(persona.items())) # <class 'dict_items'>
print(persona.items()) # dict_items([('name', 'eder'), ('edad', 12)])
print(list(persona.items())) # [('name', 'eder'), ('edad', 12)]
print(tuple(persona.items())) # (('name', 'eder'), ('edad', 12))

