# TODO : Repasar bien el tema de las funciones en python


persona = ("eder", 23)


def saludar(name, edad):
    saludo = f"Hola {name}"
    # edad = None
    if edad:  
        print(f"{name} Usted tiene {edad} años")
    return saludo

print(saludar(*persona))





#  rrecorrer una lista o tupla normalmente sin usar el indice
# persona = ("eder", 23)

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