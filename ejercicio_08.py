for multiplicando in range(1, 11):
    print("La tabla del", multiplicando)
    for multiplicador in range(1, 11):
        resultado = multiplicando * multiplicador
        print(multiplicando, "x", multiplicador, "=", resultado)
    print()