import random

# 1. Diccionario de palabras organizadas por categorías
palabras_categorias = {
    'Hogar': ['CASA', 'DORMITORIO', 'COCINA', 'SALA', 'COMEDOR', 'BAÑO'],
    'Tecnología': ['COMPUTADORA', 'INTERNET', 'TECLADO', 'CELULAR', 'MONITOR'],
    'Mascotas': ['PERRO', 'GATO', 'HAMSTER', 'CANARIO', 'TORTUGA'],
    'Naturaleza': ['BOSQUE', 'MONTAÑA', 'RIVER', 'OCÉANO', 'SELVA']
}

def obtener_palabra():
    """Selecciona una categoría y una palabra al azar."""
    categoria = random.choice(list(palabras_categorias.keys()))
    palabra = random.choice(palabras_categorias[categoria]).upper()
    return categoria, palabra

def mostrar_ahorcado(intentos):
    """Dibuja la figura del ahorcado según los intentos restantes."""
    etapas = [
        # 0 intentos (6 errores)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               -
        """,
        # 1 intento (5 errores)
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               -
        """,
        # 2 intentos (4 errores)
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               -
        """,
        # 3 intentos (3 errores)
        """
           -----
           |   |
           O   |
          /|   |
               |
               -
        """,
        # 4 intentos (2 errores)
        """
           -----
           |   |
           O   |
           |   |
               |
               -
        """,
        # 5 intentos (1 error)
        """
           -----
           |   |
           O   |
               |
               |
               -
        """,
        # 6 intentos (0 errores)
        """
           -----
           |   |
               |
               |
               |
               -
        """
    ]
    return etapas[intentos]

def jugar(categoria, palabra):
    """Función principal del juego con soporte para categorías."""
    palabra_completa = "_" * len(palabra)
    adivinada = False
    letras_incorrectas = []
    intentos = 6

    print("--- ¡A Jugar al Ahorcado! ---")
    print(f"PISTA: La categoría es '{categoria.upper()}'")
    print(mostrar_ahorcado(intentos))
    print(f"La palabra tiene {len(palabra)} letras: {palabra_completa}\n")

    while not adivinada and intentos > 0:
        intento_usuario = input("Adivina una letra o la palabra completa: ").upper()
        
        # Validación de entrada
        if len(intento_usuario) == 1 and intento_usuario.isalpha():
            if intento_usuario in letras_incorrectas or intento_usuario in palabra_completa:
                print(f"Ya intentaste con la letra '{intento_usuario}'.")
            elif intento_usuario not in palabra:
                print(f"La letra '{intento_usuario}' NO está en la palabra.")
                intentos -= 1
                letras_incorrectas.append(intento_usuario)
            else:
                print(f"¡Bien! La letra '{intento_usuario}' SÍ está en la palabra.")
                palabra_lista = list(palabra_completa)
                indices = [i for i, letra in enumerate(palabra) if letra == intento_usuario]
                for indice in indices:
                    palabra_lista[indice] = intento_usuario
                palabra_completa = "".join(palabra_lista)

        elif len(intento_usuario) == len(palabra) and intento_usuario.isalpha():
            if intento_usuario == palabra:
                adivinada = True
                palabra_completa = palabra
            else:
                print(f"'{intento_usuario}' no es la palabra correcta.")
                intentos -= 1

        else:
            print("Entrada no válida. Introduce una letra o la palabra completa.")

        # Muestra el estado actual
        print(mostrar_ahorcado(intentos))
        print(f"Palabra: {palabra_completa}")
        print(f"Intentos restantes: {intentos}")
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}\n")

        if "_" not in palabra_completa:
            adivinada = True
    
    # Resultado final
    if adivinada:
        print(f"¡Felicidades! Ganaste. La palabra era: {palabra}")
    else:
        print(f"¡Perdiste! Se acabaron los intentos. La palabra era: {palabra}")

if __name__ == "__main__":
    cat, pal = obtener_palabra()
    jugar(cat, pal)
