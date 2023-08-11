# Function to convert number from string type a int
datos = ("12", "34", "gacia", "34", 145, True, 45, "Peru", 1, "brazil", 34, 55)
def to_int(dato):
    if isinstance(dato, str): # con el try/except esto se puede obviar ya que tambien manejaria los errores de que tiene que ser solo string
        try:
            return int(dato)
        except:
            return dato

res_int = map(to_int, datos)
print(tuple(res_int))


# edad = "12"
# try:
#     edad = int(edad)
# except:
#     edad = edad

# print(type(edad), edad)

