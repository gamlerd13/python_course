animal = "shAAanchito feliz"

print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title())
# borra todos los espacios de la izquierda y derecha lstrip() : solo quita espacios de la derecha  rstrip() : solo quita de la derecha.
print(animal.strip())

print(animal.find("feliz"))
print(animal.replace("feliz", "triste"))
print("feliz" in animal)  # Para ver si se encuentra
print("feliz" not in animal)
