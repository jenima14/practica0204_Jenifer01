contraseña = "M@ticorena123"
while True:
    entrada = input("Ecribe tu contraseña: ")
    if entrada == contraseña:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Intentalo de nuevo.")
input()