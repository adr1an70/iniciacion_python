"""Estoy creando una calculador que pueda realizar las operaciones siguientes"""
print("Mostrar menu de operaciones: \n Suma (+) (1) \n Resta (-) (2) \n Multiplicación (*) (3) \n División (/) (4) \n División entera (//) (5) \n Potencia (**) (6) \n Resto módulo (%) (7) ")
operacion = int(input("Que operacion quiere realizar: "))
if operacion not in range(1,8) :
    print("No es valido, elija un numero que se determine en el menú de seleccion")
if operacion in range(1,8) :
    print(f"Has escogido {operacion}, perfecto.")

"""Definir los calculos que se realizaran"""
while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            # Verificar división por cero en las operaciones 4, 5, 7
            if operacion in [4, 5, 7] and num2 == 0:
                print("rror: No se puede dividir entre 0. Elige otro número.")
                continue
            break
        except ValueError:
            print("Error: Debes introducir solo números (usa punto para decimales).")
"""Una vez creada la parte de los errores de operaciones entre 0 entraremos en las operaciones que si se pueden realizar"""
if operacion == 1:
    resultado = num1 + num2
if operacion == 2:
     resultado = num1 - num2
if operacion == 3:
     resultado = num1 * num2
if operacion == 4:
     resultado = num1 / num2
if operacion == 5:
     resultado = num1 // num2
if operacion == 6:
     resultado = num1 ** num2
if operacion == 7:
     resultado = num1 % num2

"""Escribir el resultado de la operacion realizada"""
print(f"El resultado de tu operacion es: {resultado}. ¿Es correcto?")
#Preguntar al usuario si quiere seguir con otra operacion
continuar = input("¿Desea continuar? (s/N): ")
if continuar not in ("s, si, y, yes, Si, Yes, Y, S"):
     print("!Hasta la proxima, espero que te haya podido ayudar¡")