edad = input("ingrese edad: ")

if (int(edad) > 45):
    print("Pueda entrar al bar")
elif int(edad) > 17:
    print("puedes entrar al bar acompañado de un adulto mayor de 45 años")
else:
    print("No puede ingresar, es menor de edad.")
