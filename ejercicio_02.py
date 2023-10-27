num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
if num2 != 0:
    resultado = num1 / num2
    print("La división de", num1, "entre", num2, "es igual a", resultado)
else:
    print("Error: No se puede dividir entre cero")
input()