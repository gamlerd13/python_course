import json
from pprint import pprint, pp # Pretty print

# Se abre el archivo desde la ruta donde se encuentre
with open('./datos/datos.json') as datos:
    datos = json.load(datos)


pprint(datos, width=500, depth=2, indent=4, compact=True) # EL pprint da un estilo bonito cuando imprime en pantalla
# pp(datos)  # Por ahora se que ordena los datos de acuerdo al abecedario


# print(list(datos.items()))
# print("\n")
# print(datos.items())


# # recorrer un diccionario en for

# for clave, valor in datos.items():
#     print(f"{clave} ==> {valor}")

# print(type(datos.items()))
# # print(list(datos.items()))



