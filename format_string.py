##format() : sirve para ingresar dates dentro de una cadena de texto



name = "gamlerd13"
age = 23


##Antiguamente

##forma más antigua: Aqui tienes que especificar el tipo de datos con la inicial del tipo de dato
print("El cliente %s tiene %d años" %(name, age))

##forma antigua 2: Aqui solo poner las llaves, luego antes del cierre la funcion format con todos de datos a ingresar
print("El cliente {} es puntual en sus pagos".format(name))


##forma reciente no tan buena, tiene que importar una libreria
from string import Template
cadena = Template("My name is $name and I'am $age years hold").substitute(name=name,age=age)
print(cadena)

##forma moderna mas simple y mejor visto
print(f"mi nombre es {name} y tendré {age} años")