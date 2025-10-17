print("----- PROMEDIADOR DE NOTAS -----")

nota1 = int(input("Ingrese su primer nota: "))
nota2 = int(input("Ingrese su segunda nota: "))
nota3 = int(input("Ingrese su tercer nota: "))

notas = nota1 + nota2 + nota3
print(f"Tus 3 notas suman {notas}")

promedio = notas / 3
print(f"Tu promedio es de {promedio}")

if promedio > 6:
    print("Felicidades, Pasaste el año")
else:
    print("No pasaste el año, Suerte la proxima vez")