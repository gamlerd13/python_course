frutas = ["manzana","pere", "mango", "limon"]
print(len(frutas))

#list constructor

newlist = list(("eder", "maycon", "anival"))
print(dir(newlist))

# TODO:Métodos de las listas
    
# append(elemento): Agrega un elemento al final de la lista.
frutas = ["manzana", "banana", "naranja"]
frutas.append("uva")
print(frutas)  # Output: ["manzana", "banana", "naranja", "uva"]


# insert(indice, elemento): Inserta un elemento en una posición específica de la lista.
frutas = ["manzana", "banana", "naranja"]
frutas.insert(1, "uva")
print(frutas)  # Output: ["manzana", "uva", "banana", "naranja"]

# remove(elemento): Elimina el primer elemento con el valor especificado de la lista.
frutas = ["manzana", "banana", "naranja"]
frutas.remove("banana")
print(frutas)  # Output: ["manzana", "naranja"]

# pop(indice): Elimina y devuelve el elemento en la posición especificada. Si no se proporciona un índice, elimina y devuelve el último elemento.
frutas = ["manzana", "banana", "naranja"]
eliminado = frutas.pop(1)
print(eliminado)  # Output: "banana"
print(frutas)     # Output: ["manzana", "naranja"]

# del: Elimina un elemento de la lista en función de su índice.
frutas = ["manzana", "banana", "naranja"]
del frutas[1]
print(frutas)  # Output: ["manzana", "naranja"]


# extend(iterable): Agrega los elementos de otro iterable (como otra lista) al final de la lista actual.
frutas = ["manzana", "banana"]
otras_frutas = ["naranja", "uva"]
frutas.extend(otras_frutas)
print(frutas)  # Output: ["manzana", "banana", "naranja", "uva"]

# index(elemento): Devuelve el índice del primer elemento con el valor especificado.
frutas = ["manzana", "banana", "naranja"]
indice = frutas.index("banana")
print(indice)  # Output: 1

# count(elemento): Devuelve la cantidad de elementos con el valor especificado en la lista.
frutas = ["manzana", "banana", "manzana", "naranja"]
conteo = frutas.count("manzana")
print(conteo)  # Output: 2

# sort(): Ordena la lista en orden ascendente (modifica la lista original).
numeros = [4, 2, 7, 1, 5]
numeros.sort()
print(numeros)  # Output: [1, 2, 4, 5, 7]

# sorted(): Devuelve una nueva lista ordenada a partir de los elementos de la lista original.
numeros = [4, 2, 7, 1, 5]
ordenados = sorted(numeros)
print(ordenados)  # Output: [1, 2, 4, 5, 7]


# reverse(): Invierte el orden de los elementos en la lista (modifica la lista original).
frutas = ["manzana", "banana", "naranja"]
frutas.reverse()
print(frutas)  # Output: ["naranja", "banana", "manzana"]

# clear(): Elimina todos los elementos de la lista, dejándola vacía.
frutas = ["manzana", "banana", "naranja"]
frutas.clear()
print(frutas)  # Output: []

# copy(): Crea una copia superficial (shallow copy) de la lista.
frutas = ["manzana", "banana", "naranja"]
copia_frutas = frutas.copy()
print(copia_frutas)  # Output: ["manzana", "banana", "naranja"]

# len(): Devuelve la longitud (número de elementos) de la lista.
frutas = ["manzana", "banana", "naranja"]
longitud = len(frutas)
print(longitud)  # Output: 3

# min(), max(): Devuelve el elemento mínimo o maximo en la lista (si todos los elementos son comparables).
numeros = [4, 2, 7, 1, 5]
minimo = min(numeros)
maximo = max(numeros)
print(minimo)  # Output: 1
print(maximo)  # Output: 7

# sum(): Devuelve la suma de todos los elementos en la lista (si todos los elementos son numéricos).
numeros = [4, 2, 7, 1, 5]
suma = sum(numeros)
print(suma)  # Output: 19

# join(iterable): Une elementos de una lista en una cadena utilizando un separador.
frutas = ["manzana", "banana", "naranja"]
cadena = ", ".join(frutas)
print(cadena)  # Output: "manzana, banana, naranja"

# any(): Devuelve True si al menos uno de los elementos de la lista es True.
valores = [False, True, False]
resultado = any(valores)
print(resultado)  # Output: True

# all(): Devuelve True si todos los elementos de la lista son True.
valores = [True, True, True]
resultado = all(valores)
print(resultado)  # Output: True



# zip(): Combina elementos de varias listas en tuplas.
nombres = ["Alice", "Bob", "Charlie"]
edades = [25, 30, 28]
combinados = list(zip(nombres, edades))
print(combinados)  # Output: [("Alice", 25), ("Bob", 30), ("Charlie", 28)]
