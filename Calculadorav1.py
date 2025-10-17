print("----- CALCULADORA DE NUMEROS -----")
a = int(input("Ingrese el Numero A: "))
b = int(input("Ingrese el Numero B: "))

operacion = (input("( + )( - )( / )( x ) :"))

if operacion == "+":
    print(f"La suma entre {a} y {b} es: {a + b}")
elif operacion == "-":
    print(f"La resta entre {a} y {b} es: {a - b}")

elif operacion == "/":
    if b != 0:
        print(f"La division entre {a} y {b} es: {a / b}")
    else:
        print("Error: no se puede dividir por cero.")
elif operacion == "x":
    print(f"La multiplicacion entre {a} y {b} es: {a * b}")
else:
    print("Comando Invalido, Intente nuevamente")