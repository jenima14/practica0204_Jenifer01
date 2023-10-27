frase = input("Escribe una frase: ")
letra = input("Escribe una letra: ")
num_veces = 0
for caracter in frase:
    if caracter == letra:
        num_veces += 1
print("La letra '" + letra + "' aparece " + str(num_veces) + " veces en la frase.")
input()