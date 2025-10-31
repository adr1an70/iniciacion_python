"""Estoy creando una calculador que pueda realizar las operaciones siguientes"""
while True:
    while True:
        print("Mostrar menu de operaciones: \n Suma (+) (1) \n Resta (-) (2) \n Multiplicación (*) (3) \n División (/) (4) \n División entera (//) (5) \n Potencia (**) (6) \n Resto módulo (%) (7) ")
        operacion = int(input("Que operacion quiere realizar: "))
        if operacion not in range(1,8) :
            print("No es valido, elija un numero que se determine en el menú de seleccion")
        else : #Aqui le añado la condición a que si el usuario digita un numero en el rango (1,8) proceda a hacer el calculo determinado
            print(f"Has escogido {operacion}, perfecto.")
            break #El break sirve para romper el loop en el caso de que el numero seleccionado no este en el menu de operaciones
        
    """Definir los calculos que se realizaran"""
    while True: #Bucle en el cual entra los numeros elegidos por el usuario para realizar la operacion
            try:
                num1 = float(input("Introduce el primer número: ")) #Preguntar el primer numero que quiere usar para la operacion
                num2 = float(input("Introduce el segundo número: ")) #Preguntar el segundo numero que quiere usar para la operacion

                # Verificar división por cero en las operaciones 4, 5, 7
                if operacion in [4, 5, 7] and num2 == 0:
                    print("Error: No se puede dividir entre 0. Elige otro número.")
                    continue
                break #Usado para romper el loop en caso de que el numero sea divido entre 0
            except ValueError:
                print("Error: Debes introducir solo números (usa punto para decimales).")
    """Una vez creada la parte de los errores de operaciones entre 0 entraremos en las operaciones que si se pueden realizar"""
    """Aqui asignamos condiciones de que si el usuario digita un numero que concuerde con la operacion que quiere realizar, la maquina hara la operacion y dara el resultado"""

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
    print(f"El resultado de tu operacion es: {resultado}.")
    #Preguntar al usuario si quiere seguir con otra operacion
    continuar = input("¿Desea continuar? (s/N): ")
    if continuar not in ("s, si, y, yes, Si, Yes, Y, S"):
        print("!Hasta la proxima, espero que te haya podido ayudar¡")