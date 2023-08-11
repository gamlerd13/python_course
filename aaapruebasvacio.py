datos = input("Enter you name and your age separate by one spacing: \n")

# THERE IS A METHOD FOR STRINGs, it IS IMPORTANT TO KNOW it TOO
mensaje = "El pollo estaba vivo o muerto"
mensaje = mensaje.split(' ')

datos = datos.split(" ")

#  Desectruccturacion directamente para ahorrar memoria
datos2 = {
    'name':datos[0],
    'edad':int(datos[1])
}
#  Desectruccturacion para mejor legibilidad
nombre, edad = datos
datos3 = {
    'name':nombre,
    'edad':int(edad)
}


## First Form
# def saludar(datitos):
#     datitos[1]= int(datitos[1])
#     if datitos[1] > 18:
#         print(f"Hola {datitos[0]} usted es mayor de edad")
#     else:
#         print("Oye mocose que haces acá")
# saludar(datos)

## Second Form
# def saludar(name, edad):
#     edad= int(edad)
#     if edad > 18:
#         print(f"Hola {name} usted es mayor de edad")
#     else:
#         print("Oye mocose que haces acá")
# saludar(*datos)

def saludar(name, edad):
    edad= int(edad)
    if edad > 18:
        print(f"Hola {name} usted es mayor de edad")
    else:
        print("Oye mocoso, no deberias estas aca")
saludar(**datos2)