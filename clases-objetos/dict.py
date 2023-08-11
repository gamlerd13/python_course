perro = {
    'tamano': 1.32,
    'edad': 48,
    'color': 'verde',
    'raza': 'chiwuwa',
    'nombre': 'simon'
}

# Cantidad de elementos del diccionario
numero_elemento = len(perro)
print(numero_elemento)

# Get Keys and values in a list
claves_perro = tuple(perro.keys())
valores_perro = tuple(perro.values())
print(claves_perro)
print(valores_perro)


name = "eder"
edad = 12
is_casado = False

persona = dict(name=name,edad=edad, is_casado=is_casado)
print(persona)