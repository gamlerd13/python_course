datos_persona = list(("Eder", "Miraval", 23, True))

datos_persona2 = dict(zip(['name', 'apellido', 'edad', 'is_pobre'],datos_persona))
print(datos_persona2)

llaves_datos_persona2 = tuple(datos_persona2.keys())
print(llaves_datos_persona2)
valores_datos_persona2 = tuple(datos_persona2.values())
print(valores_datos_persona2)

# First Form
# def saludar(datitos):
#     datitos[2]= int(datitos[2])
#     if datitos[2] > 18 and datitos[len(datos_persona)-1]:
#         print(f"Hola {datitos[0]}, {datitos[1]} usted es mayor de edad y esta pobre")
#     else:
#         print("Oye mocose que haces acá, haz dinero")
# saludar(datos_persona)

## Second Form
# def saludar(name,apellido, edad, is_pobre):
#     edad= int(edad)
#     if edad > 18 and is_pobre==True:
#         print(f"Hola {name} {apellido} usted es mayor de edad y esta pobre")
#     else:
#         print("Oye mocoso, no deberias estas aca")
# saludar(*datos_persona)



# third form
def saludar(name,apellido, edad, is_pobre):
    edad= int(edad)
    if edad > 18 and is_pobre==True:
        print(f"Hola {name} {apellido} usted es mayor de edad y esta pobre")
    else:
        print("Oye mocoso, no deberias estas aca")
saludar(**datos_persona2)


