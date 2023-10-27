nombre = input("Escribe tu nombre: ")
sexo = input("Escribe tu sexo (Mujer/Hombre): ")
nombre = nombre.lower()
casa = ""
if (sexo.lower() == "mujer" and nombre < "m") or (sexo.lower() == "hombre" and nombre > "n"):
    casa = "Gryffindor"
else:
    casa = "Slytherin"
print("La casa que te corresponde es: " + casa)
input()