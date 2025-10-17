secreto = int(input("Ingrese el numero a adivinar"))

intento = int(input("Adivina el numero: "))

while intento != secreto:
    if intento < secreto:
        print("Mas Alto")
    elif intento > secreto:
        print("Mas Bajo")
    intento = int(input("Intenta de nuevo: "))
print("iFelicitaciones! Adivinaste el numero.")
    