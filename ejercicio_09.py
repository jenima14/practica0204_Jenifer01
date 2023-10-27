numero_entero = int(input("Escribe un número entero: "))
for linea in range(1, numero_entero + 1):
    for i in range(2 * linea - 1, 0, -2):
        print(i, end=" ")
    print()
input()