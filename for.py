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

# This is a common mistake 'cause we were trying to use the element and index of the frutas string without using the enumerate method
# for e,i in frutas:
#     print(e)

print(enumerate(frutas))

# for indice, valor in enumerate(frutas):
#     print(f"Índice {indice}: {valor}")