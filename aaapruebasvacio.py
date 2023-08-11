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

