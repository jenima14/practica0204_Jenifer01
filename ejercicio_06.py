edad = int(input("Escribe tu edad: "))
if edad <= 0:
    print("Escribe una edad válida.")
else:
    print("Los años que has cumplido son:")
for cumplido in range(1, edad + 1):
    print(cumplido)
input()