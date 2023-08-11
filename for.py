datos = {
    "name": "eder",
    "edad": 30,
    "gustos": [
        "futbol",
        "natacion",
        "basquetball"
    ]
}

amount_gustos = len(datos["gustos"])

#method 1
for e in datos["gustos"]:
    print(f"me gusta el/la {e}")

#method 2
for i in range(amount_gustos):
    print(datos["gustos"][i], "i like it")




# enumerate(): Devuelve un objeto enumerado que produce pares de índice y valor mientras recorres la lista.
frutas = ["manzana", "banana", "naranja"]

#  rrecorrer una lista o tupla normalmente sin usar el indice
persona = ("eder", 23)

for a in persona:
    print(a)

#  rrecorrer una lista o tupla usando indices
# enumerate(persona) : [(0, 'eder'), (1, 23)]
for i, e in enumerate(persona):
    print(f"{i} ==> {e}")


# LEER: enumerate lo que hace es agregarle un valor adelante de una lista o tupla, de modo que vada elemento pareciera que tenga un indice
# Entonces lo que quiero probar es que si creo una lista o tupla ya con indice deberia funcionar son enumerate
# Conclusin: Solo tiene que haber en cada sub lista o sub tupla siempre la misma cantidad de elemtos, es indistinto el tipo de dato

paises = [(0, 'peru', 'lima'),("undice 1", 'USA', ["neva york", "washinstong"])]
for i, e, c in paises:
    print(f"{i} => de {e} su capital es {c}")