### Dictionaries ### es la misma manera de los sets pero referenciamos los valores al diccionario

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Luis",
                 "Apellido": "Bustos", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Luis",
    "Apellido": "Bustos",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("Luis" in my_dict) #para refernciar debemos agregar la categoria a la que pertenece no el valor
print("Apellido" in my_dict)

# Inserción

my_dict["Calle"] = "Calle Centenary"
print(my_dict)

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]
print(my_dict)

# Otras operaciones

print(my_dict.items()) #te muestra los valores junto con la categoria o referencia
print(my_dict.keys())  # te muestra las categorias o referencias
print(my_dict.values()) # solo te muestra los valores sin las categorias o referencias

my_list = ["Nombre", 1, "Piso"] 
print(my_list)

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Centenary")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict)) #el set "tuple" sale en {} 
print(set(my_new_dict)) #el list en []