numero_entero = int(input("Escribe un número entero : "))
if numero_entero <= 0:
    print("Escribe una altura válida (mayor que 0).")
else:
    print("Triángulo rectángulo:")
for triangulo in range(1, numero_entero + 1):
    print('*' * triangulo)
input()