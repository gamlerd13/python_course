# TODO:Crear una función que calcule el factorial de un numero que se le pide por pantalla


numero = int(input("Ingrese numero entero a calcular: "))
print(type(numero))
res = 1
for num in range(numero):
    res = res*(num+1)
    print("This is into for:", res)
print(res)

# res = "hola" if res == 1 else None
