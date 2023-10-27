edad = int(input("Escribe tu edad: "))
ingresos_mensuales = float(input("Escribe tus ingresos mensuales en euros: "))
if edad > 16 and ingresos_mensuales >= 1000:
    print("Debes tributar.")
else:
    print("No debes tributar.")
input()