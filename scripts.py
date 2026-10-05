print('Hola estoy aprendiendo python')

name = "Sofía"
print(name)

print("Hola " + name + ", ¿cómo estás?")

print (f"Hola {name}, ¿cómo estás?")


nombre = "Lola"
apellido = "Bonet"
print(f"soy {nombre} y mi apellido es {apellido}")

age = 87
numero = 10
print(age + numero)

print(type(age))

edad = 22
ciudad = "Valencia"
tengo_carnet = True
print(tengo_carnet)

print(ciudad[0])
print(len(ciudad))


nombre = nombre.upper()
apellido = apellido.lower()
print(f"{nombre} {apellido} ")

print(len(nombre))
print(nombre[0])
print(apellido[len(apellido)-1])

dic = {
    "nombre": "Lola",
    "edad": 22,
    "ciudad": "Valencia",
    "soltero": True
} 
print(dic["nombre"])

frutas = ["manzana", "pera", "plátano"]

compra = ["pan", "leche", "huevos"]
compra.append("aceite")
compra.append("verdura")
compra.insert(2, "pan")
compra.pop(len(compra)-1)
print(compra)
print(compra[0])


culpable = False

if culpable:
    print("Eres culpable")
else:
    print("Eres inocente")