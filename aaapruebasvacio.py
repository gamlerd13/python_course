# enumerate(): Devuelve un objeto enumerado que produce pares de índice y valor mientras recorres la lista.
frutas = ["manzana", "banana", "naranja"]
for e,i in frutas:
    print(e)

print(enumerate(frutas))

# for indice, valor in enumerate(frutas):
#     print(f"Índice {indice}: {valor}")