import json

# Se abre el archivo desde la ruta donde se encuentre
with open('./datos/datos.json') as datos:
    datos = json.load(datos)


print(list(datos.items()))
print("\n")
print(datos.items())


# recorrer un diccionario en for

for clave, valor in datos.items():
    print(f"{clave} ==> {valor}")

print(type(datos.items()))
# print(list(datos.items()))



