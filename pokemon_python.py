#Pokemon python.
"""Voy a recrear el inicio de pokemon rojo fuego, pero con algunas expeciones a mi gusto y conocimiento."""
nombre_pj= input("Bienvenido a pokemon rojo fuego, soy el profesor Oak. Antes de empezar, dime tu nombre: ")
print(f"Encantado de conocerte {nombre_pj}, este es un mundo habitado por criaturas llamadas pokemons. Son seres que coexisten con los humanos.")
print("Tu misión es convertirte en un maestro pokemon. Para ello, primero debes elegir tu pokemon inicial.")
print("Tienes tres opciones: Bulbasaur, Charmander o Squirtle.")
#Elección del tu pokemon inicial. 
pokemon_inicial= input("¿Cuál eliges?  1 (Bulbasaur) , 2 (Charmander) o 3 (Squirtle): ")
if int(pokemon_inicial) == 1:
    print("Has elegido a Bulbasaur, un pokemon de tipo planta/veneno. ¡Buena elección!")
    print("Quieres ponerle a Bulbasaur un apodo? (Digita 1 = Si o Digita 2 = No)")
    respuesta_apodo = input("Tu respuesta: ")
    if int(respuesta_apodo) == 1:
        apodo = input("¿Cuál es el apodo que le quieres poner a Bulbasaur? ")
        print(f"Has puesto a Bulbasaur el apodo de {apodo}.")
    if int(respuesta_apodo) == 2:
           print("Vale, Bulbasaur se quedo igual.")
elif int(pokemon_inicial) == 2:
    print("Has elegido a Charmander, un pokemon de tipo fuego. ¡Buena elección!")
    print("¿Quieres ponerle a Charmander un apodo?(Digita 1 = SI o Digita 2 = NO)")
    respuesta_apodo = input("Tu respuesta: ")
    if int(respuesta_apodo) == 1:
        apodo = input("¿Cuál es el apodo que le quieres poner a Charmander?")
        print(f"Has puesto a Charmander el apodo de {apodo}.")
        if int(respuesta_apodo) == 2:
           print("Vale, Charmander se quedo igual.")
elif pokemon_inicial == 3:
    print("Has elegido a Squirtle, un pokemon de tipo agua. ¡Buena elección!")
    print("¿Quieres ponerle a Squirlte un apodo?(Digita 1 = SI o Digita 2 = NO)")
    respuesta_apodo = input("Tu respuesta: ")
    if int(respuesta_apodo) == 1 :
        apodo = input("¿Cuál es el apodo que le quieres poner a Squirtle?")
        print(f"Has puesto a Squirtle el apodo de {apodo}.")
    if int(respuesta_apodo) == 2:
           print("Vale, Squirtle se quedo igual.")
elif int(pokemon_inicial) == 4:
    print("Has elegido a Pikachu, un pokemon de tipo eléctrico. ¡Buena elección!")
    print("¿Quieres ponerle a Pikachu un apodo?(Digita 1 = SI o Digita 2 = NO)")
    respuesta_apodo = input("Tu respuesta: ")
    if int(respuesta_apodo) == 1:
        apodo = input("¿Cuál es el apodo que le quieres poner a Charmander?")
        print(f"Has puesto a Charmander el apodo de {apodo}.")
    if int(respuesta_apodo) == 2:
           print("Vale, Charmander se quedo igual.")
else:
    print("Opción no válida. Por favor, elige entre Bulbasaur, Charmander o Squirtle.")


print(f"Buenas {nombre.pj}, han pasado varios años desde que comenzaste tu camino, has conseguido derrotar al alto mando, ahora te falta derrotar al campeón de la Liga Pokemon Azul...")
print("Para enfrentar a Azul, necesitas que tu pokemon inicial alcance un nivel determinado. Me podrias decir a qué nivel has entrenado a tu pokemon inicial?")

nivel_pokemon = input("Introduce el nivel de tu pokemon inicial: ")
if nivel_pokemon >= "50":
    print("¡Felicidades! Tu pokemon inicial ha alcanzado el nivel 50, ahora puedes enfrentarte a Azul. ¡Buena suerte en tu batalla!")
    
elif nivel_pokemon < "50":
    print("Tu pokemon inicial no ha alcanzado el nivel necesario. Necesitas seguir entrenando antes de enfrentarte a Azul.")

