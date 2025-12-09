import random

# Lista de palabras para el juego
palabras = ['casa', 'familia', 'hogar', 'dormitorio', 'computadora', 'cocina', 'mascota', 'sala']

def obtener_palabra():
    """Selecciona una palabra al azar de la lista."""
    return random.choice(palabras).upper()

def jugar(palabra):
    """
    Función principal del juego del ahorcado.
    """
    # Inicialización de variables
    palabra_completa = "_" * len(palabra)
    adivinada = False
    letras_incorrectas = []
    intentos = 6  # Número máximo de intentos (cabeza, cuerpo, 2 brazos, 2 piernas)

    print("--- ¡A Jugar al Ahorcado! ---")
    print(mostrar_ahorcado(intentos))
    print(f"La palabra tiene {len(palabra)} letras: {palabra_completa}\n")

    while not adivinada and intentos > 0:
        # Pide la entrada del usuario
        intento_usuario = input("Adivina una letra o la palabra completa: ").upper()
        
        # Validación de entrada
        if len(intento_usuario) == 1 and intento_usuario.isalpha():
            # El usuario adivinó una sola letra
            if intento_usuario in letras_incorrectas or intento_usuario in palabra_completa:
                print("Ya intentaste con esta letra.")
            elif intento_usuario not in palabra:
                print(f"La letra '{intento_usuario}' NO está en la palabra.")
                intentos -= 1
                letras_incorrectas.append(intento_usuario)
            else:
                print(f"¡Bien! La letra '{intento_usuario}' SÍ está en la palabra.")
                # Reemplaza los guiones con la letra correcta
                palabra_lista = list(palabra_completa)
                indices = [i for i, letra in enumerate(palabra) if letra == intento_usuario]
                for indice in indices:
                    palabra_lista[indice] = intento_usuario
                palabra_completa = "".join(palabra_lista)

        elif len(intento_usuario) == len(palabra) and intento_usuario.isalpha():
            # El usuario adivinó la palabra completa
            if intento_usuario == palabra:
                adivinada = True
            else:
                print("Esa no es la palabra correcta.")
                intentos -= 1

        else:
            print("Entrada no válida. Introduce una sola letra o la palabra completa.")

        # Muestra el estado actual del juego
        print(mostrar_ahorcado(intentos))
        print(palabra_completa)
        print(f"Intentos restantes: {intentos}")
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}\n")

        # Comprueba si la palabra ha sido adivinada
        if "_" not in palabra_completa:
            adivinada = True
    
    # Resultado final
    if adivinada:
        print(f" ¡Felicidades! Adivinaste la palabra: **{palabra}**")
    else:
        print(f" ¡Se acabaron los intentos! La palabra era **{palabra}**")
        print(mostrar_ahorcado(0)) # Muestra la figura completa al perder

def mostrar_ahorcado(intentos):
    """
    Dibuja la figura del ahorcado según los intentos restantes.
    El índice 0 (intentos=6) es el estado inicial (sin errores).
    El índice 6 (intentos=0) es el estado final (pierde).
    """
    etapas = [
        # 6 intentos restantes (0 errores)
        """
           -----
           |   |
               |
               |
               |
               -
        """,
        # 5 intentos restantes (1 error - cabeza)
        """
           -----
           |   |
           O   |
               |
               |
               -
        """,
        # 4 intentos restantes (2 errores - cuerpo)
        """
           -----
           |   |
           O   |
           |   |
               |
               -
        """,
        # 3 intentos restantes (3 errores - brazo)
        """
           -----
           |   |
           O   |
          /|   |
               |
               -
        """,
        # 2 intentos restantes (4 errores - otro brazo)
        """
           -----
           |   |
           O   |
          /|\  |
               |
               -
        """,
        # 1 intento restante (5 errores - pierna)
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               -
        """,
        # 0 intentos restantes (6 errores - otra pierna - PERDIDO)
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               -
        """
    ]
    # Retorna la figura correspondiente al número de intentos restantes.
    return etapas[6 - intentos]

# Bloque de ejecución principal
if __name__ == "__main__":
    palabra = obtener_palabra()
    jugar(palabra)
