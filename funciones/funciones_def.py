# TODO : Repasar bien el tema de las funciones en python


persona = ("eder", 23)


def saludar(name, edad):
    saludo = f"Hola {name}"
    # edad = None
    if edad:  
        print(f"{name} Usted tiene {edad} años")
    return saludo

print(saludar(*persona))

