# TODO:Crear una función que calcule el factorial de un numero que se le pide por pantalla
""" Ojo: En los bucles for en python cuando se les pasa solo el parametro de rango final, que es por defecto cuando se le pasa
un parametro dentro de range, es como el bucle de do-while en c++ ya que siempre se ejecuta la menos una vez, en cambio en javascript en el bucle
for primero ve la condicion y luego se ejecuta: python: >=, javascript == """

numero = int(input("Ingrese numero entero a calcular: "))
print(type(numero))
res = 1
for num in range(numero):
    res = res*(num+1)
    print("This is into for:", res)
print(res)

# res = "hola" if res == 1 else None
